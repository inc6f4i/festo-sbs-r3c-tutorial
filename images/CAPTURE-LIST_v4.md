# 📸 스크린샷 촬영 목록 v4 — 남은 요청

> v4 (2026-10-02 18:37): 실물 사진 4장 반영. 원본 `images/raw/8404·8405·8407·8408.jpg`는 그대로 두고, 방향을 바로잡고 화면(모니터) 부분을 흐리게 한 사본을 새 이름으로 만들었다.
>
> | 원본 | 새 raw | 주석본 | 쓰인 곳 |
> |---|---|---|---|
> | 8404.jpg | photo_setup_overview.jpg (모니터 흐림) | photo_00_setup_overview.jpg | M00 v3 |
> | 8407.jpg | photo_setup_side.jpg | photo_00_setup_side.jpg | M00 v3 |
> | 8408.jpg | photo_setup_front.jpg (모니터 흐림), photo_sensor_back.jpg (뒷면 확대·180° 회전) | photo_00_setup_front.jpg, photo_01_sensor_back.jpg | M00 v3, 사양서 v2 |
> | 8405.jpg | photo_sensor_label.jpg (라벨 확대·180° 회전) | photo_01_sensor_label.jpg | 사양서 v2 |
>
> ⚠️ 원본 jpg 4장에는 오른쪽 모니터 화면이 찍혀 있다. 공개 저장소에 올리기 싫으면 원본은 `.gitignore`에 넣거나 빼고, 흐림 처리한 `photo_*.jpg`만 올린다.

---

(이하 v3 내용)

# 📸 스크린샷 촬영 목록 v3

3차(2026-10-02 17:49–17:59)는 **Claude가 PC를 직접 제어**해 `Win + Shift + S` 전체 화면 캡처로 찍었다. 설정값은 바꾸지 않았고 드롭다운은 펼쳐 보기만 한 뒤 `Esc`로 닫았다. 사용자 캡처 2장(174945, 174948)도 함께 반영했다.
원본 `스크린샷 2026-10-02 *.png`는 `C:\Users\user\Pictures\Screenshots`에 그대로 있다.

## ✅ 이번에 반영한 것 (17장 → 주석 16장)

| raw 새 이름 | 원본 시각 | 주석본 (`images/annotated/`) | 쓰인 곳 |
|---|---|---|---|
| cs_ko_det_contrast_color-distance | 174945 (사용자) | cs_ko_04_det_contrast_color-distance(+ _image) | M04 v3 |
| cs_ko_det_contrast_binarization_user | 174948 (사용자) | cs_ko_04_det_contrast_binarization_image | M04 v3 |
| cs_ko_det_contrast_binarization | 175309 | cs_ko_04_det_contrast_color-channel | M04 v3 |
| cs_ko_det_contrast_check | 175444 | (raw만 보관 — 아래 펼친 화면으로 대체) | |
| cs_ko_det_contrast_search-area-dropdown | 175456 | cs_ko_04_det_contrast_check-tab | M04 v3 (V-01, V-11) |
| cs_ko_job_resolution-dropdown | 175529 | cs_ko_02_job_resolution-dropdown | M02 v3 (V-02) |
| cs_ko_job_dynamic-dropdown | 175556 | cs_ko_02_job_dynamic-dropdown | M02 v3 (V-03) |
| cs_ko_menu_view | 175616 | cs_ko_07_menu_view | M01 v3 |
| cs_ko_view_focus-meter | 175636 | cs_ko_02_view_focus-meter | M01 v3 (V-16) |
| cs_ko_output_io10-dropdown | 175705 | cs_ko_06_output_io10-dropdown | M06 v3, M07 v3 (V-19) |
| cs_ko_output_digital-output | 175720 | cs_ko_05_output_digital-output | M05 v3 |
| cs_ko_output_interfaces | 175726 | cs_ko_06_output_interfaces | M06 v3 (V-07, V-09) |
| cs_ko_output_timing | 175732 | cs_ko_05_output_timing | M05 v3 |
| cs_ko_output_telegram | 175856 | cs_ko_07_output_telegram | M07 v3 |
| cs_ko_output_image-transmission | 175902 | cs_ko_07_output_image-transmission | M07 v3 |
| cs_ko_output_archiving | 175908 | (raw만 보관) | |
| cs_ko_output_archiving_result-filter | 175927 | cs_ko_07_output_archiving | M07 v3 (V-18) |

쓰지 않은 것: 175233(바탕화면·탐색기·Claude 창이 함께 찍힘).

> [!NOTE]
> 3차 캡처는 오른쪽 아래에 **Claude 창**이 겹쳐 있어 Help 패널 아래쪽이 가려졌다. 그래서 주석본은 설정 창(화면 아래쪽) 위주로 잘라 냈다. Help 번역은 이미 레슨에 있다.

## ⏳ 남은 요청

### A. 설정을 바꿔야 해서 Claude가 찍지 않은 것 (사용자 확인 필요)

| # | 파일명 | 찍을 화면 | 이유 |
|---|---|---|---|
| A1 | `cs_det_colorarea_*.png` (3–4장) | `검사기 › 신규 › 컬러영역`으로 검출기를 **새로 만든 뒤** 탭들 + `칼라분포도` 창 | 검출기 추가 = 잡 변경. 실습용 새 잡에서 만들고 지우면 됨 |
| A2 | `cs_alignment_contour_*.png` (5장) | `위치보정설정 › 방법 = 윤곽선추출 검사` 선택 후 탭 5개 | 방법 변경 = 잡 변경 (찍은 뒤 `없음`으로 되돌림) |
| A3 | `cs_running_ok.png`, `cs_running_ng.png` | `검사시작` 실행 중 OK / NG 시료 (상태표시줄 DOUT·통계) | 빈 작업2·작업3이 있어 검사시작이 막힘(C-05) → 지우거나 검출기 추가 필요 |
| A4 | `cs_job_resolution_zoom-compare.png` | **새 잡**에서 QVGA 줌 1 ↔ 줌 2 (V-25) | 해상도 변경 시 검출기 전부 삭제 |
| A5 | `cs_det_contrast_3rd+.png` | 검출기를 계속 추가해 상한 확인 (V-01 상한) | 잡 변경 |

### B. 다른 프로그램 (그대로 남음)

| # | 파일명 | 찍을 화면 | 레슨 |
|---|---|---|---|
| B1 | `vs_main.png`, `vs_tabs_*.png`, `vs_archiving-config.png` | Visualisation Studio (Device Manager `보기`) | M07 |
| B2 | `dm_useradmin.png` | Device Manager `파일 › 사용자 관리` (값 바꾸지 말고 취소) | M07 |
| B3 | `dm_update.png` | `파일 › 펌웨어 업데이트...` (**열기만, 실행 금지**) | M07 |
| B4 | `dm_autostart.png` | `파일 › 자동 실행 파일...` | M07 |
| B5 | `web_viewer.png` | SBSWebViewer 켜고 검사시작 → 브라우저 `http://192.168.3.40` | M07 |
| B6 | `calc_fov.png` | SBS Calculator `Field of view` 화면 | M00 |
| B7 | `desktop_icons.png` | 바탕화면/시작 메뉴의 SBS 아이콘 (V-21) | M01 |
| B8 | `cs_toolbar.png` | 툴바 아이콘 툴팁 | M01 |
| B9 | `cs_en_job_dynamic.png` | 영문 UI에서 `Dynamic` 드롭다운 (V-24 최종 대조) | M02 |

### C. 실물 사진 (휴대폰)

| # | 파일명 | 내용 | 상태 |
|---|---|---|---|
| C1 | `photo_sensor_back.jpg` | 센서 뒷면 | ✅ 반영 |
| C2 | `photo_cable_label.jpg` | 12핀 케이블의 **품번 라벨**(보통 커넥터 근처 또는 케이블 끝의 흰 띠) — V-06 | ⏳ |
| C3 | `photo_setup.jpg` | 설치 구성 | ✅ 반영 (앞·옆·전체 3장) |
| C4 | `photo_samples.jpg` | OK/NG 시료를 **위에서 한 장에** (지금은 같은 좌석 시료 2개만 보임 — 결함 NG 시료가 있으면 함께) | ⏳ |
| C5 | `photo_distance.jpg` | 렌즈 앞면 ~ 시료 윗면에 자를 댄 사진 — V-27 | ⏳ 신규 |
