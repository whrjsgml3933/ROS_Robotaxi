"""Database configuration regression tests; never connect to a real database."""

import os
import runpy
import unittest
from pathlib import Path
from unittest.mock import patch

DB_FILE = Path(__file__).resolve().parents[1] / "server_core" / "db.py"
CONFIG = {
    "TASHO_DB_HOST": "localhost",
    "TASHO_DB_USER": "test-user",
    "TASHO_DB_PASSWORD": "test-only-not-a-real-password",
    "TASHO_DB_NAME": "test-database",
}


class DatabaseConfigurationTests(unittest.TestCase):
    def load_module(self, values):
        with patch.dict(os.environ, values, clear=True):
            return runpy.run_path(str(DB_FILE))

    def test_missing_configuration_never_connects(self):
        module = self.load_module({})
        with patch("pymysql.connect") as connect:
            with self.assertRaisesRegex(RuntimeError, "TASHO_DB_PASSWORD"):
                module["_get_conn"]()
        connect.assert_not_called()

    def test_each_required_value_is_checked(self):
        for missing in CONFIG:
            with self.subTest(missing=missing):
                values = dict(CONFIG)
                values.pop(missing)
                module = self.load_module(values)
                with patch("pymysql.connect") as connect:
                    with self.assertRaisesRegex(RuntimeError, missing):
                        module["_get_conn"]()
                connect.assert_not_called()

    def test_configured_values_are_passed_to_driver(self):
        module = self.load_module({**CONFIG, "TASHO_DB_PORT": "3307"})
        with patch("pymysql.connect") as connect:
            module["_get_conn"]()
        options = connect.call_args.kwargs
        self.assertEqual(options["port"], 3307)
        self.assertEqual(options["password"], CONFIG["TASHO_DB_PASSWORD"])
        self.assertEqual(options["database"], CONFIG["TASHO_DB_NAME"])
        self.assertTrue(options["autocommit"])
        self.assertEqual(options["connect_timeout"], 2)

    def test_default_port(self):
        self.assertEqual(self.load_module(CONFIG)["DB_PORT"], 3306)

    def test_invalid_ports_are_rejected_without_echoing_value(self):
        for value in ("invalid-sensitive-value", "", "0", "-1", "65536"):
            with self.subTest(value=value):
                with self.assertRaises(RuntimeError) as error:
                    self.load_module({**CONFIG, "TASHO_DB_PORT": value})
                self.assertEqual(
                    str(error.exception),
                    "TASHO_DB_PORT must be an integer from 1 to 65535.",
                )

    def test_password_whitespace_is_preserved(self):
        password = " test-only-password "
        module = self.load_module({**CONFIG, "TASHO_DB_PASSWORD": password})
        with patch("pymysql.connect") as connect:
            module["_get_conn"]()
        self.assertEqual(connect.call_args.kwargs["password"], password)


if __name__ == "__main__":
    unittest.main()
