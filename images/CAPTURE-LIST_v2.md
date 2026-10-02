# 📸 스크린샷 촬영 목록 v2 — 남은 요청

2차로 받은 45장 중 26장을 이름 붙여 레슨에 넣었다(`images/raw/` 새 이름 파일, `images/annotated/`). 원본 `스크린샷 2026-10-02 *.png`는 그대로 둔다.

> 찍는 요령
> - **창 단위 캡처**(`Alt + PrintScreen` 또는 `Win + Shift + S` → 창 모드). 전체 화면(2560×1392)은 글자가 작아져 주석이 어렵다.
> - 캡처 직후 오른쪽 아래 **캡처 도구 알림이 화면에 남지 않게** 잠깐 기다렸다 다음 캡처.
> - 드롭다운은 **펼친 상태**로 찍는다.
> - 한국어/영문 어느 쪽이든 괜찮다. 같은 화면을 두 언어로 찍을 필요는 없다.
> - 파일 이름은 아래 이름으로 저장하면 바로 연결된다(다른 이름이어도 내가 정리한다).

## ✅ 이번에 반영한 것

| 새 이름 | 원본 시각 | 쓰인 곳 |
|---|---|---|
| calc_home, calc_device-type-list, calc_working-distance | 172342, 172739, 172620 | M00 v2 |
| pc_ipv4, pc_ipv4_advanced | 172810, 172825 | M01 v2 |
| dm_details, dm_settings, dm_menu_file / options-language / help | 172843, 172945, 173001, 173014, 173016 | M01 v2, M07 v2 |
| cs_menu_file, cs_menu_file_save-image, cs_menu_view, cs_menu_options-language | 173123–173133 | M01 v2, M02 v2, M07 v2 |
| cs_ko_main (+ 지도, 일반 탭) | 173140 | M01 v2, M02 v2 |
| cs_ko_job_white-balance, cs_ko_job_preprocessing | 173325, 173328 | M02 v2 |
| cs_ko_alignment | 173236 | M03 v2 |
| cs_ko_detector_new, cs_error_no-detector | 173240, 173309 | M04 v2, M05 v2 |
| cs_ko_result, cs_ko_statistics, cs_ko_job_cycle-time | 173255, 173251, 173332 | M05 v2 |
| cs_ko_output_io-mapping | 173245 | M06 v2 |
| cs_ko_job_load-dialog, cs_recorder_window | 173151, 173206 | M07 v2 |

쓰지 않은 것: 173031·173041·173055·173109(Device Manager 전체 화면 — dm_main으로 충분), 173147·173200(작업2 어두운 화면), 173220·173259·173301·173303·173319·173329·173336·173339(Help 패널 스크롤 — 번역은 이미 있음), 173232(HTML Help 창), 173227(확대 보기 — cs_ko_enlarged-view로 이름만 보관), 173142(도움말 메뉴 — 대응표에 반영).

## ⏳ 남은 요청 (우선순위 순)

### A. 장비 확인과 같이 찍을 것 (V-항목)

| # | 파일명 | 찍을 화면 | 확인 항목 |
|---|---|---|---|
| A1 | `cs_det_contrast_3rd.png` | `검사기 › 신규`로 **색 대비 검사를 3개** 만든 뒤 검사기 목록 | V-01 검출기 최대 수 |
| A2 | `cs_job_resolution-dropdown.png` | `일반 › 해상도` 드롭다운 펼침 | V-02 |
| A3 | `cs_job_dynamic-dropdown.png` | `일반 › 다이나믹` 드롭다운 펼침 | V-03, V-24 |
| A4 | `cs_output_interfaces.png` | `출력양식설정 › 통신설정` 탭 | V-07 PNP/NPN, V-09 RS422 |
| A5 | `cs_output_io10-dropdown.png` | `입/출력 핀맵 설정`에서 **10 보라**의 `기능 정의` 드롭다운 펼침 | V-19 잡 전환 |
| A6 | `cs_output_archiving.png` | `출력양식설정 › 저장(아카이빙)` 탭 전체 | V-18 |
| A7 | `cs_view_focus-meter.png` | `보기 › Image focus meter` 켠 상태의 이미지 창 | V-16 |
| A8 | `cs_running_ok.png`, `cs_running_ng.png` | 빈 잡을 지운 뒤 `검사시작` 실행 중, OK 시료 / NG 시료 (상태표시줄 디지털출력·통계 보이게) | V-05, M05 |

### B. 레슨 화면 (메뉴 위치)

| # | 파일명 | 찍을 화면 | 레슨 |
|---|---|---|---|
| B1 | `cs_alignment_contour_*.png` (5장) | `위치보정설정 › 윤곽선추출 검사` 선택 후 아래 탭 5개 각각 | M03 |
| B2 | `cs_det_contrast_*.png` (2장) | 색 대비 검사 검출기 선택 후 설정 탭들 | M04-1 |
| B3 | `cs_det_colorarea_*.png` (3–4장) | 컬러영역 검출기 선택 후 설정 탭들 + **컬러 히스토그램** 창 | M04-2 |
| B4 | `cs_output_digital-output.png` | `출력양식설정 › 디지털출력` 탭 | M05 |
| B5 | `cs_output_timing.png` | `출력 타이밍 설정` 탭 | M05 |
| B6 | `cs_output_telegram.png` | `출력문자열 설정` 탭 | M07 |
| B7 | `cs_output_image-transmission.png` | `이미지전송` 탭 | M07 |
| B8 | `cs_toolbar.png` | 툴바 아이콘에 마우스를 올려 툴팁이 보이게 (아이콘마다 1장, 또는 툴바 전체 1장 + 이름 메모) | M01 |

### C. 다른 프로그램

| # | 파일명 | 찍을 화면 | 레슨 |
|---|---|---|---|
| C1 | `vs_main.png` | Device Manager `보기`로 연 Visualisation Studio 첫 화면 | M07 |
| C2 | `vs_tabs_result.png`, `vs_tabs_statistics.png`, `vs_tabs_job.png`, `vs_tabs_upload.png` | Visualisation Studio 아래 탭 4개 | M07 |
| C3 | `vs_archiving-config.png` | Visualisation Studio `파일 › 아카이빙 설정(Configure archiving)` 창 | M07 |
| C4 | `dm_useradmin.png` | Device Manager `파일 › 사용자 관리` 창 (값 바꾸지 말고 취소) | M07 |
| C5 | `dm_update.png` | `파일 › 펌웨어 업데이트...` 창 (**열기만, 실행 금지**) | M07 |
| C6 | `dm_autostart.png` | `파일 › 자동 실행 파일...` 창 | M07 |
| C7 | `web_viewer.png` | `통신설정`에서 SBSxWebViewer 켜고 검사시작 → 브라우저 `http://192.168.3.40` | M07 |
| C8 | `calc_fov.png` | SBS Calculator `Field of view` 화면 | M00 |
| C9 | `desktop_icons.png` | 바탕화면/시작 메뉴의 SBS 아이콘 | V-21 |

### D. 실물 사진 (휴대폰)

| # | 파일명 | 내용 | 레슨 |
|---|---|---|---|
| D1 | `photo_sensor_back.jpg` | 센서 뒷면(LED, 초점 나사, 커넥터 3개) | 사양서, M01 |
| D2 | `photo_cable_label.jpg` | 12핀 케이블 라벨(품번) | V-06 |
| D3 | `photo_setup.jpg` | 설치 거리·브래킷·시료가 보이는 전체 사진 | M00 |
| D4 | `photo_samples.jpg` | OK/NG 시료 전부 한 장에 | M04, M08 |
