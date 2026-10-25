# 저장소 구조 안내

TASHO의 화면, 서버, 로봇 코드와 운영 자료를 역할별로 구분합니다.

```text
ROS_Robotaxi/
├── GUI/
│   ├── admin_ui/             # 관리자 GUI, UI·모델·보정 자료
│   │   ├── run_admin.py
│   │   ├── requirements.txt
│   │   └── admin_app/
│   └── user_gui/             # 승객 GUI, 지도·카메라 자료
│       ├── main.py
│       ├── camera/
│       └── user_ui/
├── robot/
│   ├── pinky/                # 주행·충전·배터리 노드와 지도·ROS 설정
│   ├── pinky_supervisor.py   # 기존 Pinky 실행 진입점 유지
│   └── jetcobot/             # 로봇팔 supervisor와 충전 worker
├── server/
│   ├── main_server/          # FastAPI, DB, 라우터
│   └── ai_server/            # 비전 프로세스와 모델·보정 파일
├── docs/
│   ├── REPOSITORY_STRUCTURE.md
│   └── operations/           # 기존 설치·터미널·연동 메모
└── archive/
    └── GUI/                  # 기존 .bak 백업 파일의 원래 디렉터리 구조
```

## 코드 찾기

| 영역 | 진입점·파일 | 주의사항 |
| --- | --- | --- |
| 관리자 GUI | [run_admin.py](../GUI/admin_ui/run_admin.py) | 기존 admin_ui 작업 디렉터리와 requirements.txt 유지 |
| 승객 GUI | [main.py](../GUI/user_gui/main.py) | UI·지도·카메라의 상대 배치를 유지 |
| 메인 서버 | [fastapi_server.py](../server/main_server/fastapi_server.py) | 기존 DB와 환경 설정 필요 |
| 비전 서버 | [ai_launcher.py](../server/ai_server/ai_launcher.py) | 기존 모델·카메라·네트워크 환경 필요 |
| Pinky | [노드와 설정 안내](../robot/pinky/README.md) | 기존 foobar/의 파일을 함께 이동 |
| Pinky supervisor | [pinky_supervisor.py](../robot/pinky_supervisor.py) | 기존 /home/pinky/pinky_agent/ 배포 경로 사용 |
| Jetcobot | [arm_supervisor.py](../robot/jetcobot/arm_supervisor.py) | 같은 폴더의 final_arm_charge.py 실행 |

## 변경된 경로

| 이전 | 현재 |
| --- | --- |
| foobar/ | robot/pinky/ |
| GUI/admin_ui/의 설치·연동·터미널 메모 4개 | docs/operations/admin-ui/ |
| server/ai_server/실행코드.txt | docs/operations/ai-server/실행코드.txt |
| GUI/admin_ui/admin_app/ 하위 .bak 파일 4개 | archive/GUI/admin_ui/admin_app/ 아래 동일한 경로 |

파일 내용과 이름은 보존했습니다. 관리자 GUI의 requirements.txt는 코드 옆에 그대로 있습니다. 모델 가중치, 카메라 보정 데이터와 GUI 리소스의 위치는 변경하지 않았습니다.

## 기존 실행 환경에서 적용

- 저장소의 foobar/를 참조하는 외부 터미널 명령·IDE 설정·배포 스크립트가 있다면 robot/pinky/로 경로를 바꿉니다. 저장소 내부의 실행 코드에는 foobar/ 참조가 없었습니다.
- Pinky 노드·launch·설정·지도 파일을 한 폴더 안에 유지했습니다. pix_map.yaml의 image: pix_map.pgm 상대 참조도 유지됩니다.
- Pinky supervisor의 /home/pinky/pinky_agent/*.py 절대경로는 기존 배포 규약입니다. 로봇에 배포할 때 robot/pinky/의 해당 노드들을 기존 배포 폴더에 배치합니다. supervisor의 기본 경로나 동작은 이번 정리에서 변경하지 않았습니다.
- ROS XML의 find-pkg-share는 설치된 pinky_navigation·nav2_bringup 패키지를 참조합니다. 저장소 폴더 이동이 설치 패키지의 launch·params 파일을 자동 교체하지는 않습니다.
- 비전 서버에 있는 /home/cwj/... 절대 모델 경로도 기존 설정을 유지합니다. 새 PC에서 실행하려면 해당 환경의 경로를 확인해야 합니다.
- 이 저장소는 여러 장비에 나누어 배포하는 소스 모음입니다. 저장소 전체를 한 번에 빌드하는 ROS 패키지로 바꾸지는 않았습니다.

## 검증 범위

이 정리는 파일 위치와 안내 문서만 바꿉니다. Python·XML의 구문과 파일 이동 전후 내용 보존을 확인하며, 실물 로봇 구동·ROS 런타임·카메라·MySQL 연결은 별도 장비 환경에서 검증해야 합니다.

