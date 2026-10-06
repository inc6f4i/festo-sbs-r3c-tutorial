# 🛠️ 문제 해결 (증상 → 원인 → 조치) — v2

> v2 (2026-10-06): 현장에서 실제로 일어난 **안전 사고 2건**과 최종 프로젝트 구성 중 문제를 추가했다. 이전 판: [troubleshooting.md](troubleshooting.md)

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


## 안전 (2026-10-06 실제 사고)

> [!CAUTION]
> 아래 두 건은 이 튜토리얼 작업 중 **실제로 일어난 일**이다. 다친 사람은 없었지만, 조건이 조금만 달랐으면 감전·화상·장비 손상으로 이어질 수 있었다.

| # | 일어난 일 | 원인 | 위험 | 다음부터 |
|---|---|---|---|---|
| S-1 | **SMPS 입력 단자(L·N)에 24 V LED를 물렸다가 "펑" 소리** | SMPS의 **AC 입력 쪽(L, N, FG/GN)** 과 **DC 출력 쪽(+V, −V)** 을 헷갈림. L–N 사이는 **AC 220 V** | 부품 파열·화상. L·N·GN 단자는 **감전 시 사망 위험**(AC 220 V 이상) | ① SMPS 단자 표기를 먼저 읽는다: `L` `N` `⏚(FG)` = AC 입력, `+V` `−V`(또는 `V+` `V−`, `COM`) = DC 출력 ② **24 V 부품은 +V/−V에만** ③ 결선 전 전원 플러그를 뽑는다 ④ 결선 후 **멀티미터 DCV로 +V–−V가 24 V인지 먼저 확인**하고 부품을 연결 ⑤ AC 단자는 덮개(터미널 커버)를 닫아 둔다 |
| S-2 | **단자대 작업 중 드라이버가 통전되어 스파크** | 전원이 켜진 상태에서 일반(비절연) 드라이버가 이웃 단자 2개에 동시에 닿음 → 단락 | 단자·드라이버 끝 손상, 센서 출력/전원 단락(센서 출력은 단락 보호가 있지만 반복은 금물), 손 화상 | ① **전원 OFF 후 결선**(매뉴얼 p.28 "결선·해체는 전원을 끈 상태에서만") ② **절연 드라이버**(VDE 1000 V 표시) 사용 ③ 한 손 작업, 이웃 단자와 거리 확보 ④ 스파크가 났다면: 전원 OFF → 단자 눌림·그을음 확인 → SMPS 출력 24 V 재확인 → 센서 Pwr LED·Device Manager 상태 확인 후 재가동 |

**사고 후 확인한 것 (S-1, S-2 이후 시험)**: 센서 출력 12·07에서 **23.0 V** 정상 측정, LED 3단 판별 정상(08 v5 9절) → 센서·SMPS DC 출력은 이상 없음. S-1의 LED는 교체 대상.

## 최종 프로젝트 구성 (2026-10-06)

| 증상 | 원인 | 조치 | 근거 |
|---|---|---|---|
| 판정기준값에 24.3을 넣으면 24,00이 됨 | 판정기준값 칸은 **정수만** 받음(소수점은 `,` 표기) | 경계값을 정수로 반올림하고 여유를 다시 계산 | 2026-10-06 화면 |
| 빈 지그인데 Matte로 판정, LED A만 켜짐 | 지그를 약 20° **비틀어** 놓아 지그 안쪽 벽 경계가 검사 영역에 들어감 → 점수 14–21 | 지그를 바닥 프로파일에 맞대어 똑바로 놓는다. 장기적으로 지그 고정 핀/스토퍼 | 08 v5 10절 |
| Matte 전용 출력이 필요한데 NOT이 없는 줄 알았음 | 디지털출력 탭 검출기 칸에 **켜기 / 반전 / 끄기**, 논리 칸에 **AND / OR** 가 있음 | `반전` = 그 검출기의 NOT. 고급 모드 없이 해결 | 08 v5 7절 |
| 셔터를 올리면 Matte/Basic 차이가 줄어듦 | Basic(광택)이 먼저 포화 | 0.70 ms 부근 유지, 자동 활상 금지 | shutter-sweep_20261006 |
| Configuration Studio 클릭이 안 먹힘(원격 조작) | 알림 창·다른 창이 맨 앞 | 알림 닫기, 창 최대화 | 2026-10-06 |
