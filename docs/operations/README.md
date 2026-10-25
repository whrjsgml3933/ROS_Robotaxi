# 운영 자료

기존 작업 메모를 코드 폴더에서 분리했습니다. 원문의 명령·IP·환경 이름은 작성 당시 기록으로 보존했으며, 최신 실행 상태를 보장하는 안내서는 아닙니다.

- admin-ui/: 관리자 GUI의 가상환경 설치, 터미널 명령, 전체 구조와 FSM 연결 메모 4개.
- ai-server/: 비전 서버의 기존 실행 명령 메모.

메모가 이 폴더로 이동했다고 명령을 실행하는 작업 디렉터리까지 바뀌는 것은 아닙니다.

- run_admin.py와 requirements.txt를 사용하는 명령은 기존 GUI/admin_ui/에서 실행합니다.
- ai_launcher.py 명령은 기존 server/ai_server/에서 실행합니다.
- 장비 IP·카메라 포트·외부 설치 경로는 실제 배포 환경에 맞게 확인합니다.
- 일부 메모의 pinky_supervisor_fsm.py는 저장소에 없는 기존 배포 이름입니다. 저장소의 supervisor 파일은 robot/pinky_supervisor.py이며, 이 정리에서 두 파일이 동일하다고 가정하거나 명령을 바꾸지 않았습니다.

현재 파일 위치는 [저장소 구조 안내](../REPOSITORY_STRUCTURE.md)를 참고하세요.

