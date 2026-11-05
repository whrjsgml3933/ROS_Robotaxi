# DB 접속정보 분리와 교체

이 서버는 기존 MySQL을 계속 사용합니다. 새 DB·서비스·호스팅은 추가하지 않습니다.

## 설정
server/main_server/.env.example은 필요한 이름을 보여 주는 템플릿입니다.
.env 파일을 자동으로 읽는 기능이나 새 의존성은 추가하지 않았습니다.
기존 실행기 또는 서버를 시작하는 셸에서 환경변수를 전달하세요.

필수 항목: TASHO_DB_HOST, TASHO_DB_USER, TASHO_DB_PASSWORD, TASHO_DB_NAME
선택 항목: TASHO_DB_PORT (기본 3306, 1~65535)

PowerShell 예시:
```powershell
$env:TASHO_DB_HOST = Read-Host '기존 DB 호스트'
$env:TASHO_DB_USER = Read-Host '기존 DB 사용자'
$env:TASHO_DB_NAME = Read-Host '기존 DB 이름'
$securePassword = Read-Host '교체한 DB 비밀번호' -AsSecureString
$env:TASHO_DB_PASSWORD = ([System.Net.NetworkCredential]::new('', $securePassword)).Password
python -m uvicorn fastapi_server:app --host 127.0.0.1 --port 8000
```
이 명령은 server/main_server에서 실행합니다. 환경변수는 같은 셸에서 시작한 프로세스에 전달됩니다.
실제 값은 저장소·채팅·스크린샷에 넣지 마세요. 셸 종료 또는 환경변수 제거 시 다음 실행에는 다시 설정해야 합니다.
장비의 기존 실행기·서비스를 사용한다면 해당 프로세스에 같은 변수를 전달하세요.

설정이 누락되면 DB 연결 전에 변수 이름만 포함한 오류를 냅니다.
기존 서버의 startup 코드는 DB 초기화 실패를 기록하고 계속 진행할 수 있으므로,
서버가 켜졌거나 health 응답이 있다고 DB 연결 성공으로 판단하지 마세요.
이 변경에서 startup·라우트·SQL·로봇 명령 처리는 바꾸지 않습니다.

## 기존 비밀번호 대응
1. 공개 소스에 있던 비밀번호의 실제 사용 여부를 DB 관리자가 확인합니다.
2. 사용했다면 관리자의 승인과 접근 권한으로 비밀번호를 교체합니다.
3. 서버 실행 환경에 새 값을 설정하고, 승인된 시점에 기존 서버의 연결을 점검합니다.
4. 실패하면 노출된 비밀번호로 되돌리지 말고 새 인증정보와 실행 환경을 바로잡습니다.

코드 수정은 비밀번호를 폐기하지 않으며 과거 Git 이력도 정리하지 않습니다.
이력 재작성은 공동 작업자와 별도 승인 후 진행해야 합니다.

## 로컬 회귀 테스트
```bash
python -m unittest discover -s tests -v
```
PyMySQL의 connect를 대체하므로 실제 DB 접속이나 데이터 변경이 없습니다.
실제 MySQL 연결·로봇·API 통합 검증은 별도로 남아 있습니다.

