# 📚 용어집

화면 표기(영문)는 그대로 두고 뜻을 적는다. 출처가 있는 정의는 괄호로 표시.

| 용어 (화면 표기) | 뜻 | 처음 나오는 곳 |
|---|---|---|
| Job (잡) | 검사 하나에 필요한 모든 설정·파라미터 묶음 (Help: scjob). 이 품번 최대 8개 | M02 |
| Job set (잡셋) | 센서에 저장된 여러 잡의 묶음. XML 파일로 저장 (Help: scjobset) | M07 |
| Alignment (정렬) | 부품 위치·각도를 찾아 검출기 ROI를 따라가게 하는 추적 좌표계 (Help: scalignment) | M03 |
| Contour detection | 엣지로 윤곽을 학습해 최대 360° 회전까지 찾는 정렬 방식 | M03 |
| Detector (검출기) | 검사 단계 하나. 이 품번: Contrast, Color area | M04 |
| Contrast | 검색 영역 픽셀의 밝기 폭과 개수로 명암 값을 계산. 위치는 무관 (Help: scdetectorcontrast) | M04-1 |
| Color area | 정한 색 범위가 영역에서 차지하는 면적 % (Help: scdetectorcolorarea) | M04-2 |
| Search region / 검색 영역 (노랑) | 검출기가 찾는 범위 | M03 |
| Parameter zone / 파라미터 영역 (빨강/초록) | 학습한 특징 / 찾은 특징 | M03 |
| Threshold | 합격 범위(최소/최대) | M04 |
| Score | 검출기 점수(0–100 %) (Help: scresult) | M04 |
| 마진 (margin) | 측정값과 가장 가까운 합격 경계 사이 거리(%p). 이 튜토리얼 기준 ≥ 15 %p | M04 |
| Color model (RGB / HSV / LAB) | 색 표현 방식. HSV는 사람 눈에 가깝고, LAB는 장비 독립적 (Help: sccolormodel*) | M04-2 |
| Linear RGB | 셔터 2배 → RGB 값 2배인 선형 값 (Help: sccolormodelrgb) | M04-2 |
| White balance | 흰 기준면으로 R/G/B 보정 (Help: scjobwhitebalance) | M02 |
| Shutter speed | 노출 시간 0.017–100 ms. 내장 LED 펄스는 최대 8 ms | M02 |
| Gain | 신호 증폭 0.75–4. 노이즈도 증폭 | M02 |
| Dynamic (Linear / High) | 응답 곡선. High = 밝은 부분 포화 감소 | M02 |
| Quadrants | 내장 LED 사분면 개별 끄기 | M02 |
| Pre-processing | 검출 전 필터(최대 5개 + 배치 1개) | M02 |
| Filmstrip (.flm) | 최대 30장 이미지 묶음. Offline 시뮬레이션용 | M02 |
| Online / Offline | 센서 연결 / 필름스트립 시뮬레이션 | M01 |
| Free run / Trigger | 자체 연속 촬영 / 트리거 때만 촬영 | M01 |
| Single / Continuous | 이미지 1장 / 연속 갱신 | M01 |
| Result (Setup) | 잡을 **PC에서** 실행해 결과 표시(사이클 타임 없음) | M05 |
| Start sensor | 잡을 센서 플래시에 저장하고 Run 모드로 실행 | M05 |
| Overall job result | 물리 출력 없는 잡 전체 결과. 통계·레코더·아카이빙 기준 | M05 |
| Standard mode / Formula mode | 출력 논리를 체크박스로 / 수식으로 | M05 |
| Trigger delay / Result delay | 트리거→촬영 지연 / 트리거→출력 지연 (최대 3000 ms) | M05 |
| Reset signal | 출력 리셋 방식: Change on result / Change on trigger / Result duration | M05 |
| Max. cycle time | 넘으면 잡 결과 NG(타임아웃) | M05 |
| LED-Power | 셔터와 최소 잡 시간으로 계산되는 LED 출력. 최소 잡 시간 ≥ 셔터 × 10이면 100 % | M05 |
| Ready / Valid | 핀 04: 다음 트리거 준비 / 핀 11: 출력 결과 유효 | M05 |
| PNP / NPN | 출력이 +24 V로 / 0 V로 스위칭 | M06 |
| Ejector | 핀 12 전용 출력(최대 100 mA) | M06 |
| Unique function | 특정 핀에서만 가능한 기능 | M06 |
| Image recorder | 센서 RAM 링 버퍼 최대 10장 (Any/Pass/Fail) | M07 |
| RAM disk | 마지막 이미지 `/tmp/results/image.bmp`, FTP user/user | M07 |
| Archiving (FTP / SMB) | 센서가 PC 서버로 이미지·CSV를 직접 저장 | M07 |
| SBSxWebViewer | 센서 내장 웹서버 모니터링, 연결 1개 | M07 |
| Favorites | Device Manager 센서 즐겨찾기(XML) | M07 |
| Auto Start Up | SBS 소프트웨어 자동 시작 배치 파일 | M07 |
| Standard / Advanced (AF) | 기능 등급. 이 장비는 Standard (매뉴얼 p.403, p.409) | M00 |
| FOV | 시야(가로×세로 mm) | M00 |
| mm/px | 픽셀 하나가 덮는 실제 길이 | M00 |
