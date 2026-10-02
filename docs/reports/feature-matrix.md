# 📊 기능 매트릭스 — SBSI-F-R3C-F12-W (8058732, Color **Standard**)

> [!IMPORTANT]
> 이 표는 커리큘럼 설계의 기준이다. **✅ 지원** 항목만 레슨으로 만들고, **❌ 미지원** 항목은
> [`docs/appendix/advanced-only.md`](../appendix/advanced-only.md)(상위 모델 전용 부록)에서만 언급한다.
> **⚠️** 항목은 자료끼리 내용이 다르거나 자료로 확인할 수 없는 것이다. 장비 앞에서 확인한다 → [`verify-on-device.md`](../appendix/verify-on-device.md)

## 0. 품번 확정

| 항목 | 값 | 출처 |
|---|---|---|
| 품번 / 형식 | 8058732 / SBSI-F-R3C-F12-W | (데이터시트), (매뉴얼 p.403) |
| 변형(Variant) | **Standard** (형식명에 `AF`가 없음) | (매뉴얼 p.403 "Standard" 표), (매뉴얼 p.409 Type key: AF = Extended) |
| 장비가 보고한 값 | Hardware R3C / Sensor type Color / Variant Standard / FW 1.23.2.2 | [0] 입력값(Device Manager 세부 사항) |
| 설치 SW가 쓰는 기능 그룹 | group 2 = Contrast, ColorArea, ContourAlignment | (설치 SW 설정파일: `SBSConfig/1.23.2.2/Data/Color/DetectorCapabilityTable.xml`) |

> [!WARNING]
> 데이터시트 첫 줄은 "expanded function"이라고 쓰지만, 매뉴얼 표와 장비 보고값은 모두 **Standard**다.
> 이 튜토리얼은 **Standard** 기준으로 쓴다. → [상충 보고서 B-01](conflict-report.md#b-01)

**출처 약어**

| 표기 | 문서 |
|---|---|
| (매뉴얼 p.xx) | *SBS Vision Sensor Manual* `SBS_user_manual_en_V_1_23_2.pdf` (8097682 2018-07c). 쪽 번호는 인쇄 쪽 = PDF 쪽 |
| (데이터시트) | `8058732.pdf` colour sensor SBSI-F-R3C-F12-W (2022-03-10) |
| (설치설명서) | `SBS_MountingInstruction_en_V_1_23_2.pdf` (8090327 2018-07c) |
| (Help: 파일명) | Configuration Studio 내장 Help 원본 `SBS_ContextHelp_en_V1_22_14.chm`의 토픽 파일 |
| (설정파일) | 설치 SW `SBSConfig/1.23.2.2/Data/…xml` |
| (스크린샷 파일명) | `images/raw/` 사용자 캡처 |

---

## 1. 하드웨어 · 영상 취득

| 기능 | 품번 지원 | 근거 | 다루는 레슨 | 실습 유형 |
|---|---|---|---|---|
| 해상도 WVGA 736×480 / VGA 640×480 / QVGA 320×240 | ✅ | (Help: scjobgeneral), (데이터시트) | 02 | 같은 시료를 해상도별로 촬영 → 검출 결과·사이클 타임 비교 |
| 해상도 QQVGA 160×120 | ⚠️ | Help에는 없고 (설정파일 Configuration_R3C.xml)에는 있음 | 02 | 드롭다운 확인만 |
| 프레임 속도 40 fps | ✅ | (매뉴얼 p.19), (데이터시트) | 05 | 프리런 사이클 측정 |
| 셔터(Shutter speed) 0.017–100 ms, Auto shutter | ✅ | (Help: scjobgeneral), (설정파일) | 02 | 셔터 단계별 밝기·검출 점수 기록 |
| 게인(Gain) 0.75–4 | ✅ | (설정파일), (Help: scjobgeneral) | 02 | 셔터 고정, 게인만 변경 → 노이즈 관찰 |
| Dynamic (Linear / High) | ✅ ⚠️ 표기 | (Help: scjobgeneral) "High", (설정파일) "HDR" | 02 | 반사 시료에서 Linear vs High 비교 |
| 내장 조명 On/Off (백색 LED 8개) | ✅ | (Help: scjobgeneral), (매뉴얼 p.395) | 02 | 조명 On/Off 콘트라스트 비교 |
| 조명 쿼드런트(Quadrants) 개별 Off | ✅ | (매뉴얼 p.20 "Illumination quadrant controlled"), (Help: scjobgeneral) | 02 | 반사 줄이기 실험 |
| 외부 조명 출력(Off/On/Permanent, 핀 09 RD) | ✅ | (Help: scjobgeneral), (설정파일) | 02, 05 | 핀 09 출력 동작을 상태표시줄 DOUT/테스터로 확인 |
| 초점 나사(시계 방향 = 먼 거리) | ✅ | (매뉴얼 p.30) | 01 | 거리별 초점 맞추기 |
| 화이트 밸런스(Active, R/G/B, Teach, Reset) | ✅ | (Help: scjobwhitebalance), (스크린샷 cs_job_white-balance) | 02 | 흰 기준판으로 Teach 전후 색값 비교 |
| 전처리(필터 최대 5개 + 배치 1개: Gauss, Erosion, Dilation, Median, Mean, Range, Std dev, Sobel, Multiplication, Inversion / Rotation 180°, Mirror, Flip) | ✅ | (Help: scjobpreprocessing), (매뉴얼 p.71), (스크린샷: Pre-processing 탭 존재) | 02 | 필터 하나씩 적용 → 검출 점수 변화 |
| 캘리브레이션(Scaling / Calibration plate / Point pair) | ❌ | (매뉴얼 p.19 Standard 칸 공란), (스크린샷: Calibration 탭 없음) | 부록 | — |
| Cycle time 탭(Max. cycle time, 이미지당 최소/최대 처리 시간, LED-Power, Repeat mode, Shutter variation) | ✅ | (매뉴얼 p.95–97), (매뉴얼 p.20 "Timeout") | 05 | 타임아웃 일부러 걸어 NG 확인 |
| 가변 해상도 / 이미지 레코더 | ✅ | (매뉴얼 p.20) | 02, 07 | — |

## 2. 위치 추적(Alignment)

| 기능 | 품번 지원 | 근거 | 다루는 레슨 | 실습 유형 |
|---|---|---|---|---|
| Contour detection(윤곽 기반 위치 추적, X·Y·회전) | ✅ | (매뉴얼 p.19 "Contour only"), (스크린샷 cs_alignment: None / Contour detection) | 03 | 시료를 ±X mm 이동·±θ 회전 → 추종 여부 기록 |
| Pattern matching 정렬, Edge 정렬 | ❌ | (매뉴얼 p.19), (설정파일 group 2) | 부록 | — |
| 잡(Job)당 정렬 검출기 최대 1개 | ✅(제약) | (매뉴얼 p.97) | 03 | — |

## 3. 검출기(Detector)

| 검사 질문 | 검출기 | 품번 지원 | 근거 | 다루는 레슨 | 실습 유형 |
|---|---|---|---|---|---|
| 있나/없나 | **Contrast** | ✅ | (매뉴얼 p.19, p.143) | 04-1 | 캡 유/무 시료 OK·NG 각 10회 |
| 색이 맞나 / 얼마나 덮였나 | **Color area** | ✅ | (매뉴얼 p.19, p.217) | 04-2 | 색 다른 시료 판별, 면적 임계값 |
| 크기가 맞나(근사) | Color area 면적 + Contrast 경계 띠 (대체 기법) | ✅(대체) | 위 두 검출기 조합 | 04-3 | 크기 다른 시료로 Go/No-Go |
| 잡당 검출기 수 | 최대 32 | ⚠️ | (매뉴얼 p.19) 32 ↔ (데이터시트) 2 | 04 | 같은 잡에 검출기 3개 이상 추가해 확인 |
| 맞는 부품인가 | Pattern matching, Contour | ❌ | (매뉴얼 p.19) | 부록 | — |
| 밝기·명암 | Brightness, Gray | ❌ | (매뉴얼 p.19) | 부록 | — |
| 치수 | Caliper | ❌ | (매뉴얼 p.19) | 부록 | — |
| 결함·개수 | BLOB | ❌ | (매뉴얼 p.19) | 부록 | — |
| 색 값·색 목록 | Color value, Color list | ❌ | (매뉴얼 p.19) | 부록 | — |
| 코드·문자 | Barcode, Datacode, OCR | ❌(Color 계열 전체 미지원) | (매뉴얼 p.19) | 부록 | — |
| 검사 영역 자유 형상 | "Contour only" | ⚠️ 의미 | (매뉴얼 p.20) | 03 | 화면에서 마스크 가능 범위 확인 |
| 색 모델 RGB / HSV / LAB | ✅(Color area 내부) | (매뉴얼 p.273–275) | 04-2 | 같은 시료를 색 모델별로 판별 |

## 4. 판정 · 출력

| 기능 | 품번 지원 | 근거 | 다루는 레슨 | 실습 유형 |
|---|---|---|---|---|
| I/O mapping — 핀 03 WH, 10 VT(입력), 12 RDBU, 09 RD(출력), 07 BK·08 GY(입·출력 전환) | ✅ | (스크린샷 cs_output_io-mapping), (매뉴얼 p.31) | 05 | 핀별 기능 지정 → 상태표시줄 DOUT로 확인 |
| 핀 05 PK, 06 YE (입·출력 전환) | ❌ (이 Standard 형식에는 표시 안 됨) | (매뉴얼 p.31 각주 *5), (스크린샷) | 부록 | — |
| Ready(핀 04) / Valid(핀 11) 고정 출력 | ✅ | (매뉴얼 p.31), (Help: scoutputiosettings) | 05 | 트리거 타이밍 측정 |
| H/W 트리거(핀 03), Enable Trigger | ✅ | (Help: scoutputiosettings) | 05 | 트리거 → 출력 지연 측정 |
| SW 트리거(Trigger 버튼) | ✅ | (매뉴얼 p.52) | 01, 05 | — |
| Digital output 논리(Standard 모드 / Formula 모드) | ✅ | (매뉴얼 p.229–231) | 05 | 검출기 2개 AND/OR 조합 |
| PNP / NPN 전환 | ✅ | (매뉴얼 p.232), (데이터시트) | 05 | 결선 방식 확인 |
| Timing(트리거 지연, 결과 지연, 결과 유지 시간) | ✅ | (매뉴얼 p.236) | 05 | 지연값 변경 → 출력 시점 변화 |
| 엔코더 입력 | ❌ | (매뉴얼 p.20) | 부록 | — |
| Teach temp/perm 입력 | ✅ | (Help: scoutputiosettings), (설정파일 IN1/IN2 capability Standard) | 05 | 입력으로 재학습 |
| Job 전환(디지털 입력: Job 1 or 2 / 2진 / 펄스) | ✅ | (매뉴얼 p.323–324) | 07 | 입력 하나로 Job 1↔2 전환 |

## 5. 통신 · 외부 연동

> [!NOTE]
> 사용자 최상위 규칙(9)에 따라 **PLC 통신(PROFINET, EtherNet/IP)은 구현하지 않는다.**
> 장비는 지원하지만 레슨으로 만들지 않고 부록에서만 언급한다. → [상충 보고서 A-07](conflict-report.md#a-07)

| 기능 | 품번 지원 | 근거 | 다루는 레슨 | 실습 유형 |
|---|---|---|---|---|
| Ethernet TCP/IP 텔레그램(포트 2005 데이터 / 2006 명령, ASCII·Binary) | ✅ | (매뉴얼 p.20, p.232, p.247) | 06 (PC 연동, 선택) | Python 소켓으로 결과 수신 |
| PROFINET | ✅(장비) / 규칙상 제외 | (매뉴얼 p.20) | 부록 | — |
| EtherNet/IP | ✅(장비) / 규칙상 제외 | (매뉴얼 p.20) | 부록 | — |
| RS422 / RS232 | ❌ | (매뉴얼 p.20, p.32 각주 *A, p.395) — 데이터시트와 상충 | 부록 | — |
| I/O 확장 모듈 | ❌ | (매뉴얼 p.20) | 부록 | — |

## 6. 운영 · 유지보수

| 기능 | 품번 지원 | 근거 | 다루는 레슨 | 실습 유형 |
|---|---|---|---|---|
| 잡 최대 8개 | ✅ ⚠️ | (매뉴얼 p.19), (데이터시트) | 07 | 9번째 잡 생성 시 동작 확인 |
| 잡 템플릿 저장 | ✅ | (매뉴얼 p.48) | 07 | — |
| 잡/잡셋 저장·불러오기, 잡셋 보호 | ✅ | (매뉴얼 p.262–263) | 07 | 백업 → 초기화 → 복원 |
| 백업 / 센서 교체 절차 | ✅ | (매뉴얼 p.322) | 07 | — |
| Image transmission: Image recorder(최대 10장, Any/Pass/Fail), RAM disk(FTP로 `image.bmp`) | ✅ | (매뉴얼 p.247–248) | 07 | NG만 기록 |
| Archiving: FTP / SMB (Pass/Fail 폴더 분리, Limit/Unlimited/Cyclic) | ✅ | (매뉴얼 p.250–251) | 07 | NG 이미지만 PC 공유폴더에 저장 |
| 필름스트립 / 오프라인 시뮬레이션 | ✅ | (매뉴얼 p.268–269, p.276) | 02, 04 | 같은 이미지 묶음으로 반복 검증 |
| SBSxWebViewer(웹 브라우저 모니터링) | ✅ | (매뉴얼 p.20, p.233–234) | 07 | 브라우저로 결과 확인 |

## 7. 소프트웨어 4종

| 소프트웨어 | 역할 | 품번 사용 가능 | 근거 | 다루는 레슨 |
|---|---|---|---|---|
| SBS Calculator (v3.0.10) | 작업 거리 / 시야(FOV) / Data Matrix 계산 | ⚠️ 기기 목록에 R3C(736×480)가 없음 | (SBS Calculator 리소스 `theme/settings.json`: SBS 2560×1936 / 1440×1080 / 800×600만 노출) | 00 (계산식 + 실측으로 대체) |
| Vision Sensor Device Manager | 센서 검색·추가, IP/DHCP, 즐겨찾기, 비밀번호, 펌웨어 업데이트, Auto Start Up, 시뮬레이션 센서 | ✅ | (매뉴얼 p.39–40, p.54–66), (스크린샷 dm_main) | 01, 07 |
| Vision Sensor Configuration Studio — Color | 잡·정렬·검출기·출력·결과·센서 시작 설정 | ✅ | (매뉴얼 p.41, p.67–), (스크린샷) | 01–08 |
| Vision Sensor Visualisation Studio | 이미지·결과 모니터링, Freeze, Zoom, PC 아카이빙, 이미지 레코더, Result/Statistics, Job select, Job upload | ✅ | (매뉴얼 p.20 "Viewer, Job-Upload", p.277–286) | 07 |

---

## 8. 커버리지 검증(1차)

| 확인 | 결과 |
|---|---|
| ✅ 지원 기능 중 레슨이 없는 항목 | 없음 (모든 ✅ 항목에 레슨 번호 배정) |
| 규칙상 제외(PLC) | PROFINET, EtherNet/IP → 부록 |
| ⚠️ 실기 확인 항목 | 14건 (V-01 ~ V-14) → [`verify-on-device.md`](../appendix/verify-on-device.md) |

> 최종 커버리지 검증표(레슨 작성 완료 후 실제 링크 포함)는 마지막 단계에서 이 파일을 갱신하는 대신 `feature-matrix_v2.md`로 새로 만든다.
