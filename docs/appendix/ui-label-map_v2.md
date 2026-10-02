# 🔤 화면 표기 대응표 (English ↔ 한국어) — v2

> v2 (2026-10-02 PC 제어 캡처): 9장 추가 — 드롭다운 선택지, 색 대비 검사 탭, 출력양식설정 나머지 탭, 보기 메뉴(한국어). 이전 판: [ui-label-map.md](ui-label-map.md)

레슨은 매뉴얼·Help와 맞추기 위해 **영문 표기**를 기준으로 쓴다(사용자 규칙 8). 이 PC는 Device Manager가 한국어이고, Configuration Studio도 `Options › Language`에서 한국어로 바꿀 수 있다(스크린샷 cs_menu_options-language). 한국어 화면에서 메뉴를 찾을 때 이 표를 쓴다.
모든 한국어 표기는 2026-10-02 캡처(`images/raw/cs_ko_*.png`, `dm_*.png`)에서 그대로 옮겼다. 번역이 어색한 곳(예: `자동 활상`)도 화면 그대로 적는다.

> 언어 바꾸기: Configuration Studio `Options › Language › 한국어/English` · Device Manager `옵션 › 언어 › English/한국어` (스크린샷 dm_menu_options-language). Help 탭 내용은 언어 설정과 관계없이 **영문**으로 나온다.

## 1. Configuration Studio — 메뉴 · 공통

| English | 한국어 | 출처 |
|---|---|---|
| File / View / Options / Help | 파일 / 보기 / 옵션 / 도움말 | cs_ko_main |
| Help › Help (F1) / (User manual) / Support info / About | 도움말 › 도움말 F1 / 사용자설명서 / 지원 정보 / 정보 | cs_ko_menu_help |
| Setup | 작업설정메뉴 | cs_ko_main |
| Job / Alignment / Detector / Output / Result / Start sensor | 작업 / 위치보정설정 / 검사기 / 출력양식설정 / 검사설정결과보기 / 검사시작 | cs_ko_main |
| Trigger/Image update: Trigger / Single / Continuous | 트리거신호/이미지갱신: 트리거방식 / 한번 / 연속 | cs_ko_main |
| Connection mode: Online / Offline | 연결모드: 온라인 / 오프라인 | cs_ko_main |
| Fit (zoom) | 해상도에 맞춤 | cs_ko_main |
| Help / Result / Statistics (tabs) | 도움말 / 결과 / 통계 | cs_ko_main |
| Home / Prev / Next / Print | 홈 / 이전 / 다음 / 프린트 | cs_ko_main |
| Enlarged image view (창) | 이미지 확대 보기 | cs_ko_enlarged-view |

## 2. File · View 메뉴 (영문 화면에서 캡처)

| File 메뉴 | 비고 |
|---|---|
| New job (Ctrl+N) | |
| Load job... | |
| Load job set (Backup)... | 센서의 기존 잡 전부 삭제 (Help: scjobset) |
| Save job | 저장된 적 없으면 비활성 |
| Save job as... | |
| Save job set (Backup) ... | 백업 |
| Protect job set ... | |
| Save current image... › Without overlays / With overlays | 실험 이미지 남기기 |
| Configure filmstrip... | **Online에서는 비활성**, Offline에서 사용 |
| Get recorder images... | 이미지 레코더 창(센서이미지) |
| Examples | 비활성(이 품번) |
| Quit | |

| View 메뉴 | 비고 |
|---|---|
| Result graphs | 결과 막대 |
| Overlay current detector only | |
| Overlay of failed detectors only | |
| Overlay settings... | |
| **Image focus meter** | 초점 보조 (Help 표기 "Focussing aid") |
| Enlarged image view | |
| Switch to previous job (Alt+Up) / Switch to next job (Alt+Down) | 잡 전환 단축키 |

## 3. Job (작업) 설정

| English | 한국어 | 출처 |
|---|---|---|
| Configure job | 작업 설정 | cs_ko_main |
| Name / Description / Author / Created / Changed | 작업명 / 작업설명 / 제작자 / 생성일자 / 변경일자 | cs_ko_main |
| New / Load / Save / Delete / Delete all | 신규 / 열기 / 저장 / 지우기 / 모두 지우기 | cs_ko_main |
| Image acquisition / White balance / Pre-processing / Cycle time (tabs) | 일반 / 화이트 밸런스 / 이미지 전처리 / 사이클 타임 | cs_ko_main |
| Resolution (WVGA/VGA/QVGA/QQVGA + Zoom) | 해상도 (… , 줌 1/2/3) | cs_ko_02_job_resolution-dropdown |
| Shutter speed / Auto shutter | 셔터속도 / 자동 활상 | cs_ko_main |
| Dynamic: Linear / High | 다이나믹: 일반 / 하이필터 | cs_ko_02_job_dynamic-dropdown |
| Gain | 게인(Gain) | cs_ko_main |
| Trigger mode: Trigger / Free run | 트리거방식: 트리거모드 / 연속촬상모드 | cs_ko_main |
| Quadrants | 조명4분할설정 | cs_ko_main |
| Internal illumination / External illumination (On / Off) | 내부조명 / 외부조명 (켜기 / 끄기) | cs_ko_main |
| White balance: Active / Red / Green / Blue / Teach / Reset | 활성화 / 레드 / 그린 / 블루 / 티칭 / 초기화 | cs_ko_job_white-balance |
| Pre-processing: Arrangement (Rotation 180°) / Filter / Property (Off) | 배치 (180도 회전) / 필터 / 속성 (끄기) | cs_ko_job_preprocessing |
| Filter 목록 | Gauss / Erosion / Dilation / Mean / Median_Separate (영문 그대로) | cs_ko_job_preprocessing |
| Cycle time: Max. cycle time / Active | 사이클타임: 최대 실행 시간 / 활성화 | cs_ko_job_cycle-time |
| Max. processing time per image | 사이클 타임아웃 | cs_ko_job_cycle-time (순서 대조) |
| Min. processing time per image / Auto | 트리거 잠금시간 / 자동 | cs_ko_job_cycle-time (순서 대조) |
| LED power | 조명전원 | cs_ko_job_cycle-time |
| Repeat mode: Number of images (max.) / Shutter variation | 반복모드: 최대 사이클 횟수 / 셔터변화값 | cs_ko_job_cycle-time |

## 4. Alignment · Detector

| English | 한국어 | 출처 |
|---|---|---|
| Configure alignment | 영역찾기 | cs_ko_alignment |
| Method: None / Contour detection | 방법: 없음 / 윤곽선추출 검사 | cs_ko_alignment |
| Reset | 초기화 | cs_ko_alignment |
| Configure detectors and regions | 검사영역선택 | cs_ko_detector_new |
| Detector name / Detector type / Alignment | 검사기 이름 / 검사기 종류 / 위치보정설정 | cs_ko_detector_new |
| New / Copy / Reset / Delete / Delete all | 신규 / 복사 / 초기화 / 지우기 / 모두 지우기 | cs_ko_detector_new |
| New detector › Available detector types | 새로운 검사기 › 선택 가능한 검사기 종류 | cs_ko_detector_new |
| Color area | 컬러영역 (설명: 컬러영역계산) | cs_ko_detector_new |
| Contrast | 색 대비(콘트라스트)검사 (설명: 색대비를 이용한 물체 검…) | cs_ko_detector_new |

## 5. Output (출력양식설정)

| English | 한국어 | 출처 |
|---|---|---|
| Configure output | 출력 지정 | cs_ko_output_io-mapping |
| I/O mapping / Digital output / Interfaces / Timing / Telegram / Image transmission / Archiving | 입/출력 핀맵 설정 / 디지털출력 / 통신설정 / 출력 타이밍 설정 / 출력문자열 설정 / 이미지전송 / 저장(아카이빙) | cs_ko_output_io-mapping |
| Pin / color / Input / Output / Function / Unique function | 핀 번호/선 색상 / 입력 / 출력 / 기능 정의 / 기본 기능 | cs_ko_output_io-mapping |
| 03 WH / 10 VT / 12 RDBU (A) / 09 RD / 07 BK (B) / 08 GY (C) | 03 화이트 / 10 보라 / 12 빨강/파랑(A) / 09 빨강 / 07 검정(B) / 08 회색(C) | cs_ko_output_io-mapping |
| H/W Trigger | 하드웨어 트리거 | cs_ko_output_io-mapping |
| no function / undefined | 기능없음/미지정 | cs_ko_output_io-mapping |
| Ejector / Result | 배출/결과치 | cs_ko_output_io-mapping |
| Result | 검사결과 | cs_ko_output_io-mapping |
| Enable Trigger (unique) | 트리거사용설정 | cs_ko_output_io-mapping |
| External illumination (unique) | 외부조명 | cs_ko_output_io-mapping |

## 6. Result · Statistics · 상태표시줄

| English | 한국어 | 출처 |
|---|---|---|
| Results/statistics | 결과-통계 | cs_ko_result |
| Detector / Score / Time / Detector type | 검사기 / 점수 / 실행시간 / `m_DetectorType` (번역 안 된 내부 이름이 그대로 보임) | cs_ko_result |
| Count / Pass / Fail / Reset | 카운트 / 정상 / 불량 / 초기화 | cs_ko_statistics |
| Minimum / Maximum / Average execution time (n/a) | 최소 실행 시간 / 최대 실행 시간 / 평균실행시간 (해당없음) | cs_ko_statistics |
| Mode: Config / Name / Active job | 모드: 설정모드 / 이름 / 활성 작업 | cs_ko_main |
| Cycle time (n/a) / Flash | 사이클타임 m_(n/a) / 사용/미사용 플래쉬 | cs_ko_main |
| DOUT | 디지털출력 | cs_ko_main |
| Images from recorder: Date / Recorded time / Images / Back / Next / Save / Save all / Close | 센서이미지: 날짜 / 저장 시간 / 이미지 n 의 m / 이전 / 다음 / 저장 / 모두 저장 / 닫기 | cs_recorder_window |

## 7. Device Manager

| English (매뉴얼) | 한국어 화면 | 출처 |
|---|---|---|
| File / Options / Help | 파일 / 옵션 / 도움말 | dm_menu_file |
| File › User administration | 파일 › 사용자 관리 | dm_menu_file |
| File › Update (firmware) | 파일 › 펌웨어 업데이트... | dm_menu_file |
| (Rescue / sensor reset — ⚠️ 매뉴얼 대응 확인 필요) | 파일 › 센서 소프트웨어 리셋 | dm_menu_file |
| File › Auto Start Up file | 파일 › 자동 실행 파일... | dm_menu_file |
| File › Quit | 파일 › 중지 (Ctrl+F4) | dm_menu_file |
| Options › Language | 옵션 › 언어 | dm_menu_options-language |
| Help › Help / Contact & support / About | 도움말 › 도움말 F1 / 연락 및 지원 정보 / 정보 Shift+F1 | dm_menu_help |
| Active sensors | 활성화된 센서들 (열: 모드 / IP 주소 / 센서 이름 / 하드웨어 / 종류 / 변수 / 펌웨어 버전 / Mac 주소 / 서브넷 마스크 / 게이트웨이 / DHCP / 속성) | dm_run_full |
| Mode Run / Config | 실행 / 구성 | dm_run_full, dm_details |
| Details › Sensor properties | 세부 사항 › 센서 속성 (복사 / 확인) | dm_details |
| Variant | 변수 | dm_details |
| Function restriction | 기능 제한 | dm_details |
| Settings (IP setup): IPAddress / Mask / Gateway / DHCP / Name / Set / Cancel | IP주소 / 마스크 / 게이트웨이 / DHCP / 이름 / 설정 / 취소 | dm_settings |
| Sensors for simulation mode | 시뮬레이션 모드의 센서 (종류 / 하드웨어 / 변수 / 버전) | dm_main |
| Add sensors via IP address › Add | 활성화된 센서 추가 › IP 주소 › 추가 | dm_main |
| Favorites | 즐겨찾기 | dm_main |
| Find / Config / View / Settings | 탐색 / 구성 / 보기 / 설정 | dm_main |

## 8. v2 추가 — Detector (색 대비 검사) 탭

| English (Help) | 한국어 | 출처 |
|---|---|---|
| Color channel (tab) | 칼라채널 | cs_ko_04_det_contrast_color-channel |
| Contrast (tab) | 검사실행 | cs_ko_04_det_contrast_check-tab |
| Color model: RGB / HSV / LAB | 칼라모델 | cs_ko_04_det_contrast_color-channel |
| Selection color filter: Color channel (default) / Color distance / Binarization | 컬러필터선택: 컬러채널(기본값) / 칼라거리값 / 이치화 | 같은 화면 |
| max. distance / invert image | 최대거리 / 반전이미지 | cs_ko_04_det_contrast_color-distance |
| Color histogram | 칼라분포도 | cs_ko_04_det_contrast_color-channel |
| Threshold | 판정기준값 | cs_ko_04_det_contrast_check-tab |
| Search region: Rectangle / Circle | 탐색영역: 사각 / `m_Circle` (번역 안 된 내부 이름) | 같은 화면 |

## 9. v2 추가 — Output 나머지 탭

| English | 한국어 | 출처 |
|---|---|---|
| Digital output: Standard / Advanced mode | 디지털출력: 일반 모드 / 고급 모드 | cs_ko_05_output_digital-output |
| Output / Invert / NOT / Logic / Logic expression | 출력 / 반전 / NOT / 논리 / 논리식 | 같은 화면 |
| Overall job result | 작업검사결과 | 같은 화면 |
| On / Off | 켜기 / 끄기 | 같은 화면 |
| Internal I/O: PNP / NPN | 내부 입/출력 | cs_ko_06_output_interfaces |
| Ethernet / EtherNet/IP / PROFINET | 이더넷 / 이더넷/IP / 프로피넷 | 같은 화면 |
| Settings 1–3 / Logical output / Active | 세팅1–3 / 논리 출력 / 사용 | 같은 화면 |
| Image and overlay | 이미지와 검사기표시 | 같은 화면 |
| Trigger delay | 트리거 › 시간지연 | cs_ko_05_output_timing |
| Ejector delay / Send signals | 배출/결과치 시간지연 / 신호보내기 (`결과 받을때 내 보내기`) | 같은 화면 |
| Telegram: Start / Trailer / Separator / End of telegram | 출력문자열: 시작 / 트레일러 / 구분자 / 출력문자열 마지막표시 | cs_ko_07_output_telegram |
| Save to file / Result data | 파일로 저장하기 / 결과데이타설정 | 같은 화면 |
| Image recorder / RAM disk | 저장장소 › 이미지레코더 / 램 디스크 | cs_ko_07_output_image-transmission |
| Archiving: Off / FTP / SMB | 활성타입: 끄기 / FTP / SMB | cs_ko_07_output_archiving |
| Sharing name / Workgroup | 공유폴더 / 도메인(Workgroup) | 같은 화면 |
| Result files / Image files: None / All / Pass / Fail | 수치결과 / 이미지파일: 없음 / 모두 / 정상 / 불량 | 같은 화면 |
| Storage mode: Limit / Unlimited / Cyclic | 저장공간용량: 제한크기 / 무제한 / 순환방식 | 같은 화면 |
| Max. number of files | 최대파일수 | 같은 화면 |
| Directory name (pass / fail) / Filename / Add expression | 폴더이름(정상) / 폴더이름(불량) / 파일이름(지정이름-) / 표현식삽입 | 같은 화면 |
| Pin 10 functions: Job (1 or 2) / Job 1…N / Teach temp. / Teach perm. / Job switch Bit1–5 / Ignore duplicate results | 작업(1 or 2) / 작업 1…N / 임시 티칭 / 영구 티칭 / 작업변경신호(Bit1–5) / 중복된 결과 무시 | cs_ko_06_output_io10-dropdown |

## 10. v2 추가 — View 메뉴 (한국어)

| English | 한국어 |
|---|---|
| Result graphs | 결과 그래프 보기 |
| Overlay current detector only | 현재 검사기만 보이기 |
| Overlay of failed detectors only | (번역 없음, 영문 그대로) |
| Overlay settings... | 표시항목설정 |
| Image focus meter | **검출영역 중심표시 보이기** (메뉴 순서 대조, 상충 C-08) |
| Enlarged image view | 이미지 확대 보기 |
| Switch to previous / next job (Alt+Up / Alt+Down) | 이전 작업으로 이동 / 다음 작업으로 이동 (Alt+위 / Alt+아래) |

> "Ignore duplicate results", "Send signals" 영문은 화면 뜻으로 붙인 이름이다 ⚠️ 영문 UI 화면에서 정확한 표기 확인 필요.
