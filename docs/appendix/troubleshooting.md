# 🛠️ 문제 해결 (증상 → 원인 → 조치)

먼저 볼 것: ① Pwr LED ② Device Manager LED 색(녹 Run / 노 Config / 빨 오류·시작 중) ③ Configuration Studio 상태표시줄 Mode ④ 백업이 있는가

## 연결

| 증상 | 가능한 원인 | 조치 | 근거 |
|---|---|---|---|
| Device Manager 목록이 빔 | PC가 다른 어댑터/서브넷 | 상태표시줄 `IP 주소 (PC)` 확인 → 192.168.3.x, `추가`로 IP 직접 입력 | 매뉴얼 p.36, Help: sfaddfind |
| 전원 직후 안 보임 | 준비 지연 | 13 s 이상 대기 | 매뉴얼 p.395 |
| IP가 0.0.0.0 | DHCP 켰는데 서버 없음 | 직결 후 고정 IP로 재설정 | 매뉴얼 p.38 |
| `구성` 버튼 회색 | 비밀번호 보호 | 열쇠 아이콘 로그인 | Help: sfsimulation |
| Visualisation `보기`가 안 됨 | Interfaces에서 Visualisation Studio 체크 해제 | Output › Interfaces 체크 | Help: scoutputsettings |
| 웹 뷰어 안 열림 | SBSxWebViewer 미활성 / 다른 브라우저 연결 중 | 활성 + Start sensor, 다른 탭 닫기(연결 1개) | Help: svwebviewbase |

## 영상

| 증상 | 가능한 원인 | 조치 | 근거 |
|---|---|---|---|
| 영상이 안 바뀜 | Trigger 모드 또는 Single | Free run + Continuous | Help: sctrigger |
| 셔터를 올려도 밝기 그대로 | 내장 LED 펄스 최대 8 ms | 8 ms 이하 + 게인/외부 조명 | Help: scjobgeneral |
| 오후마다 판정이 바뀜 | 주변광 의존 | 내장 조명 On, 짧은 셔터 | M02 |
| 색이 틀어짐 | 조명 바꾼 뒤 WB 그대로 | 흰 종이로 Teach | Help: scjobwhitebalance |
| 흐림 | 초점, 거리 < 30 mm | 초점 나사(시계 = 먼 거리), 거리 확보 | 매뉴얼 p.30, 데이터시트 |
| 라이브 화면에 경고 아이콘 | PC 표시가 센서보다 느림 | 백그라운드 프로그램 종료 | Help: scjobtransmit |
| LED-Power < 100 % | 긴 셔터 + 짧은 최소 잡 시간 | Cycle time › Auto | Help: scjobtimeout |

## 설정·판정

| 증상 | 가능한 원인 | 조치 | 근거 |
|---|---|---|---|
| 검출기가 사라짐 | 해상도 변경 | 백업에서 복원, 해상도 먼저 확정 | Help: scjobgeneral |
| 검출기 추가가 막힘 | 최대 수(32 또는 2, V-01) / Flash 부족 | 검출기 정리, 다른 잡 삭제 | 매뉴얼 p.19, Help: scdetectoredit |
| 정렬 점수가 흔들림 | 그림자·반사 엣지 학습 | Min. contrast pattern ↑, Edit contour | Help: scalignmentcontourparameters |
| 정렬이 엉뚱한 곳 | 학습 윤곽이 고유하지 않음 | 특징적 부위로 재학습 | 〃 |
| 시료를 옮기면 NG | 검출기 Alignment 비활성 | 검출기 목록 Alignment = Active | Help: scalignmentedit |
| 설정이 센서에 반영 안 됨 | Start sensor 안 함 | Start sensor | Help: scstart |
| 모든 결과 NG | Max. cycle time 초과 | 실측 후 재설정 | Help: scjobtimeout |
| 버튼 한 번에 2회 판정 | 채터링 | Min. processing time ↑ | Help: scjobtimeout |

## 출력 (24 V)

| 증상 | 가능한 원인 | 조치 | 근거 |
|---|---|---|---|
| 판정 OK인데 0 V | Config 모드, 핀 Function 미할당 | Start sensor, I/O mapping = Result | Help: scoutputiosettings |
| 항상 24 V / 반대로 동작 | Invert, 논리식, NPN | 설정 확인, PNP | Help: scoutputlogic, scoutputsettings |
| 전압이 낮음 | 과부하, 공급 전압 낮음 | 부하 ≤ 50 mA(핀 12 ≤ 100 mA), 공급 18–26.4 V | 매뉴얼 p.395, 데이터시트 |
| Run→Config 시 출력 꺼짐 | 사양 | 정상 | Help: scoutputtiming |

## 운영

| 증상 | 가능한 원인 | 조치 | 근거 |
|---|---|---|---|
| 잡이 전부 사라짐 | Load job set / Job upload | 백업에서 복원 | Help: scjobset, svupload |
| 잡 전환 안 됨 | 어떤 잡이 Free run, 설정 불일치 | 모든 잡 Trigger + 같은 I/O 설정 | Help: scoutputiosettings |
| Active job 표시가 늦음 | 첫 트리거 후 갱신 | 정상 | 매뉴얼 p.323 |
| 레코더 이미지 사라짐 | 불러온 뒤 저장 안 함, 전원 차단 | 바로 Save all | Help: scimagerec |
| SMB 저장 안 됨 | 공유 이름·권한·게이트웨이 | 공유/계정 확인, 다른 서브넷이면 게이트웨이 | Help: scjobarchive |
| 보호 잡셋 비밀번호 분실 | 복구 불가 | 비보호 백업 사용 | Help: scprotectjobset |
