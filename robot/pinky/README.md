# Pinky 노드와 ROS 설정

기존 foobar/의 파일을 역할이 드러나는 robot/pinky/로 모았습니다. 파일 내용과 파일 사이의 상대 위치는 그대로입니다.

| 파일 | 용도 |
| --- | --- |
| pinky_idle_start.py | 시작 대기 노드 |
| pinky_click_nav2_pid_docking.py | 목적지 주행·도킹 노드 |
| pinky_charge.py | 충전 이동 노드 |
| pinky_after_charge.py | 충전 후 이동 노드 |
| pinky_idle_origin.py | 원점 복귀 노드 |
| battery_publisher.py | 배터리 상태 발행 |
| cmd_vel_arbiter_yolo.py | 속도 명령 중재 |
| led.py | LED 제어 |
| bringup_launch.xml, navigation_launch.xml | ROS 내비게이션 launch 설정 |
| mapper_params.yaml, nav2_params.yaml | 매핑·내비게이션 파라미터 |
| pix_map.yaml, pix_map.pgm | 지도 설정과 이미지 |

Supervisor 진입점은 기존 [robot/pinky_supervisor.py](../pinky_supervisor.py)에 남겨두었습니다. 이 코드의 기본 실행 경로는 /home/pinky/pinky_agent/이므로, 저장소 안으로 옮긴 것만으로 로봇의 배포 경로가 바뀌지는 않습니다.

ROS 2, Pinky 관련 패키지와 장비 설정이 필요한 코드입니다. [저장소 구조와 배포 안내](../../docs/REPOSITORY_STRUCTURE.md)를 먼저 확인하세요.

