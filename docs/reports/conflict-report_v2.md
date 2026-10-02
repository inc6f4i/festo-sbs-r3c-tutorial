# 🧾 상충 보고서 (Conflict Report) — v2

- 대상 장비: SBSI-F-R3C-F12-W (8058732), FW 1.23.2.2, IP 192.168.3.40
- 작성일: 2026-10-02 (v2: 사용자 결정 반영 — A-07, A-09 종결 / B-16, B-17 추가)
- 원칙: 사용자 규칙 **9(최상위)** > 1~8. 자료끼리 다르면 **장비 실측**을 최종 판정으로 하고, 그 전까지는 ⚠️로 남긴다.

> [!NOTE]
> 상충은 세 종류로 나눈다.
> **A** = 사용자 요청(규칙)과 장비·자료의 상충 · **B** = 자료끼리의 상충 · **C** = 화면(스크린샷)에서 본 것과 자료의 차이
> 각 항목의 "조치"가 튜토리얼에 실제로 반영된 내용이다. **결정 필요** 표시는 사용자 확인을 기다리는 항목이다.

## 요약

| ID | 종류 | 한 줄 요약 | 조치 | 상태 |
|---|---|---|---|---|
| [A-01](#a-01) | 규칙1 ↔ 첨부 | 첨부 폴더에 매뉴얼이 없음 | 설치 폴더의 공식 매뉴얼을 근거로 씀 | 반영 |
| [A-02](#a-02) | 규칙3 ↔ SW | SBS Calculator에 R3C 기기가 없음 | 계산식 + 줄자 실측으로 대체 | 반영 |
| [A-03](#a-03) | 규칙4 ↔ 품번 | 검출기 11종 중 2종만 지원 | Module 04 재구성, 나머지는 부록 | 반영 |
| [A-04](#a-04) | 규칙4·7 ↔ 품번 | 치수 측정(Caliper, 캘리브레이션) 불가 | 면적·경계 띠 기반 크기 Go/No-Go로 대체 | 반영 |
| [A-05](#a-05) | 규칙4 ↔ 품번 | RS232/422 미지원 | 레슨 제외 | 반영 |
| [A-06](#a-06) | 규칙4 ↔ 품번 | 핀 05·06, 엔코더 미지원 | 부록 | 반영 |
| [A-07](#a-07) | 규칙9 ↔ 규칙4·7 | PLC 통신 금지 | Module 06 = "검출 시에만 출력 24 V ON" | **종결** (사용자 결정) |
| [A-08](#a-08) | 규칙8 ↔ UI | Device Manager UI가 한국어 | 한국어 표기 + (영문 매뉴얼명) 병기 | 반영 |
| [A-09](#a-09) | 규칙9 ↔ 저작권 | Help 전문 번역의 공개 배포 | 연구·학습용, 출처 링크 명시 | **종결** (사용자 결정) |
| [A-10](#a-10) | 규칙9 ↔ 자료 | 메뉴 위치 스크린샷이 8장뿐 | 레슨에 ⚠️ [스크린샷 필요: 파일명] 표시, 촬영 목록 | 진행 중 |
| [A-11](#a-11) | 규칙8 ↔ 작업 방식 | "파일마다 코드 블록 출력" | 파일을 리포지토리에 직접 생성 | 반영 |
| [A-12](#a-12) | 규칙1 ↔ 출처 표기 | 출처 표기 2종으로는 부족 | 출처 약어 6종으로 확장 | 반영 |
| [B-01](#b-01) | 데이터시트 ↔ 매뉴얼 | "expanded function" ↔ Standard | Standard로 확정 | 반영 |
| [B-02](#b-02) | 데이터시트 ↔ 매뉴얼 | 검출기 최대 2개 ↔ 32개 | ⚠️ 실기 확인 | 확인 대기 |
| [B-03](#b-03) | 데이터시트 ↔ 매뉴얼 | 시리얼 지원 여부 | 미지원으로 판단, ⚠️ | 확인 대기 |
| [B-04](#b-04) | 데이터시트 ↔ 매뉴얼 ↔ Help | 디지털 I/O 개수와 전환 가능 핀 | 핀 07·08만 전환 가능으로 정리 | 반영 |
| [B-05](#b-05) | 데이터시트 ↔ 매뉴얼 | 출력 전류 50 mA ↔ 핀 12는 100 mA | 핀별로 구분 표기 | 반영 |
| [B-06](#b-06) | 데이터시트 ↔ 매뉴얼 | 외형 치수, 보호등급, 진동 규격 | 둘 다 표기, ⚠️ | 확인 대기 |
| [B-07](#b-07) | 데이터시트 표기 오류 | "Focal depth 12 mm" | 초점거리 12 mm로 해석 | 반영 |
| [B-08](#b-08) | 데이터시트 ↔ 매뉴얼 | 일반 사이클 타임 값 | Standard 검출기만 사용 | 반영 |
| [B-09](#b-09) | Help ↔ 설정파일 | 해상도 QQVGA, Dynamic "High/HDR" | ⚠️ 실기 확인 | 확인 대기 |
| [B-10](#b-10) | Help ↔ 매뉴얼 표 | 정렬 방식 "3종" ↔ "Contour only" | Contour만 다룸 | 반영 |
| [B-11](#b-11) | Help 그림 ↔ 실제 UI | Calibration 탭 | 이 품번에는 없음 | 반영 |
| [B-12](#b-12) | 매뉴얼 ↔ 설치 폴더 | Ethernet 유틸리티 경로 없음 | Python 수신기 자체 제공 | 반영 |
| [B-13](#b-13) | 자료 버전 | 매뉴얼 2종, Help 버전 차이 | V1.23.2 매뉴얼 + V1.22.14 Help 사용 | 반영 |
| [B-14](#b-14) | 데이터시트 | 단종 품번 | 백업 절차 강조 | 반영 |
| [B-15](#b-15) | Help ↔ 실제 UI | Job 목록 버튼 이름(Open/Protect) | 화면 표기(Load) 사용 | 반영 |
| [B-16](#b-16) | Help ↔ 실제 UI | 트리거 모드 위치 "General" 탭 | Image acquisition 탭으로 안내 | 반영 |
| [B-17](#b-17) | Help 표 오류 | 검출기 선택 표의 설명 열이 어긋남 | 매뉴얼 p.125 기준으로 정정 번역 | 반영 |
| [B-18](#b-18) | Help ↔ 매뉴얼 p.20 | Contrast·Color area "Free shape" ↔ Standard "Contour only" | ⚠️ V-11 | 확인 대기 |
| [C-01](#c-01) | 스크린샷 ↔ I/O 매핑 | 상태표시줄 DOUT에 05·06 표시 | ⚠️ 실기 확인 | 확인 대기 |
| [C-02](#c-02) | 스크린샷 ↔ Help | 내장 조명 Off + 셔터 50 ms | Module 02 실험 소재로 사용 | 반영 |
| [C-03](#c-03) | 스크린샷 | Device Manager Help 예시표가 다른 센서 | 혼동 주의 표기 | 반영 |

---

## A. 사용자 규칙 ↔ 장비·자료

### A-01
**규칙 1(출처는 첨부 자료에서만)** ↔ 첨부 폴더 `E:\code\vision-festo`에는 데이터시트(2쪽)와 스크린샷 8장만 있고, 매뉴얼은 없었다.
- **조치**: 같은 PC의 SBS 설치 폴더 `C:\Program Files (x86)\Festo\`에 있는 Festo 공식 문서를 사용자 승인을 받아 읽고 근거로 삼았다.
  - `Documentation/SBS_user_manual_en_V_1_23_2.pdf` — 펌웨어 1.23.2.2와 버전이 같아 **주 근거**로 씀
  - `Documentation/SBS_MountingInstruction_en_V_1_23_2.pdf`
  - `Help/en/1.22.14.1/SBS_ContextHelp_en_V1_22_14.chm` — Configuration Studio Help 탭의 원본(실행 중인 프로그램이 이 파일을 열고 있음)
  - `SBSConfig/1.23.2.2/Data/Configuration_R3C.xml`, `Data/Color/DetectorCapabilityTable.xml`
- 권장: 위 PDF·CHM을 첨부 폴더로 복사해 두면 "첨부 자료" 조건을 그대로 만족한다(저장소에는 올리지 않는다 → A-09).

### A-02
**규칙 3·4(SBS Calculator로 FOV 계산)** ↔ 설치된 SBS Calculator **v3.0.10**의 기기 목록은 `SBS 2560 x 1936`, `SBS 1440 x 1080`, `SBS 800 x 600`뿐이다(SBS Calculator 리소스 `theme/settings.json`). 2.x 세대용 목록이라 **R3C(736×480)를 고를 수 없다.**
- 같은 앱 코드 안에 736×480 센서용 상수(센서 폭 4.416 mm, 12 mm 렌즈 오프셋 −15.1 mm 등)는 남아 있지만 화면에는 나오지 않는다(SBS Calculator 리소스 `libraries/sensocalc/global/configuration.js`).
- **조치**: Module 00에서 ① Calculator 화면에서 기기 목록을 직접 확인하고(⚠️ V-10), ② 같은 계산식을 손으로 풀고, ③ 줄자·자로 실제 FOV를 재서 비교하는 실험으로 바꾼다. 매뉴얼의 FOV 그래프(매뉴얼 p.398 Fig. 362)를 교차 검증에 쓴다.

### A-03
**규칙 4(Module 04: 검출기 11종)** ↔ 이 품번(Color Standard)의 검출기는 **Contrast, Color area 2종**뿐이다(매뉴얼 p.19), (설정파일 group 2).
- **조치**: Module 04를 다음처럼 재구성한다.

| 원래 계획 | 바뀐 구성 |
|---|---|
| 04-1 있나/없나: 콘트라스트·밝기·그레이 | 04-1 있나/없나: **Contrast** |
| 04-2 맞는 부품인가: 패턴·윤곽 매칭 | (부록) — 위치는 Module 03 정렬로만 다룸 |
| 04-3 치수: 엣지·버니어 캘리퍼 | 04-3 크기가 맞나(근사): Color area 면적 + Contrast 경계 띠 → A-04 |
| 04-4 결함/개수: BLOB | (부록) |
| 04-5 색: 색상 값·면적·리스트 | 04-2 색이 맞나: **Color area** (RGB/HSV/LAB 색 모델 포함) |

### A-04
**규칙 4·7(치수, 픽셀→mm 환산)** ↔ Caliper 검출기와 Calibration(월드 좌표) 기능이 모두 Advanced 전용이다(매뉴얼 p.19). 화면에도 Calibration 탭이 없다(스크린샷 cs_job_image-acquisition).
- **조치**: 치수 **측정값 출력**은 하지 않는다. 대신
  1. 픽셀→mm 환산은 자를 찍은 이미지에서 **손으로** 구한다(mm/px 기록).
  2. 크기 판정은 Color area의 **면적(픽셀 수)** 임계값, 또는 공차 경계에 놓은 좁은 Contrast ROI(경계 띠)로 **Go/No-Go**만 한다.
- 최종 프로젝트의 "치수" 결함은 "크기 Go/No-Go"로 바꾼다. 포트폴리오에는 "Standard 형식의 한계를 검출기 조합으로 우회"로 기록한다.

### A-05
**규칙 4(Module 06: RS232/422)** ↔ Color-Standard에는 DATA 소켓 기능이 없다(매뉴얼 p.32 각주 *A "Not with Object-, Color-Standard version"), (매뉴얼 p.395 "Interfaces SBS-XX-Standard: Ethernet (LAN)"). → B-03
- **조치**: 레슨에서 뺀다.

### A-06
핀 05 PK·06 YE(입·출력 전환)와 엔코더 입력은 "Not available with all Standard types"(매뉴얼 p.31 각주 *5)이고, 실제 I/O mapping 화면에도 없다(스크린샷 cs_output_io-mapping). 설정파일에서도 IN3·IN4는 `capability="Advanced/Professional"`이다.
- **조치**: 부록에서만 언급.

### A-07
**규칙 9 "PLC 통신은 구현하지 않는다"** ↔ 규칙 4 Module 06(PROFINET/EtherNet/IP, 래더/ST), 규칙 7("I/O 또는 PLC 출력").
- 규칙 9가 우선하므로 PLC 관련 실습(장치 설명 파일, 데이터 매핑, 래더)은 **모두 뺐다.**
- **사용자 결정(2026-10-02)**: "검출 시에만 접점에 24 V 신호 ON 정도로 마무리."
- **조치**:
  - Module 06 = [`06_output-24v.md`](../06_output-24v.md): I/O mapping, Internal I/O(PNP), 검출기 → 출력 핀, 멀티미터로 24 V / 0 V 검증.
  - Module 05는 판정 논리·트리거·타이밍까지만, 실제 전압은 06에서.
  - 최종 프로젝트 출력 = 핀 07(OK) / 핀 12(NG) 24 V.
  - Ethernet TCP/IP 텔레그램, PROFINET, EtherNet/IP는 레슨에서 쓰지 않는다. Telegram 탭 Help 번역은 아카이빙 CSV 내용 정의 때문에 Module 07에만 싣는다.
- 참고: SBS 출력은 기계식 접점이 아니라 PNP/NPN 트랜지스터 출력이다(매뉴얼 p.395). 무전압 접점이 필요하면 릴레이를 둔다(06에 명시).

### A-08
**규칙 8("메뉴명은 실제 UI 표기(영문)")** ↔ Vision Sensor Device Manager가 이 PC에서 **한국어**로 표시된다(스크린샷 dm_main: `탐색`, `구성`, `보기`, `설정`, `추가`, `즐겨찾기`, `세부 사항`).
- **조치**: 화면에 보이는 그대로 쓰고, 매뉴얼 영문명을 괄호로 붙인다. 예: `탐색 (Find)`, `구성 (Config)`, `보기 (View)`, `설정 (Settings)` (매뉴얼 p.40–41). Configuration Studio는 영문 UI이므로 영문 그대로 쓴다.

### A-09
**규칙 9(Help 영문 반드시 번역, 단계마다 포함)** ↔ 매뉴얼 저작권 고지(매뉴얼 p.2).
- **사용자 결정(2026-10-02)**: "연구·학습용이라 저작권 OK, 링크만 명시."
- **조치**: 모든 Help 번역을 각 레슨의 `📖 Help 번역` 블록에 전문으로 넣고, 레슨 끝에 출처 링크를 둔다.
  - Festo 다운로드·문서 안내: <https://www.festo.com/sp> (부품번호 8058732로 검색)
  - 로컬 원본: `C:\Program Files (x86)\Festo\SBS Vision Sensor\Documentation\`, `…\Help\en\1.22.14.1\`
- 원본 PDF·CHM 파일 자체는 저장소에 넣지 않는다(`.gitignore`).

### A-10
**규칙 9(메뉴 위치를 스크린샷으로 표기)** ↔ 현재 스크린샷은 8장(Device Manager 1, Configuration Studio 7)이다. Visualisation Studio, SBS Calculator, 검출기 설정 화면, Output의 나머지 탭 등이 없다.
- **조치**: 받은 8장은 번호 박스 주석을 달았다(`images/annotated/`). 나머지는 [`images/CAPTURE-LIST.md`](../../images/CAPTURE-LIST.md)에 파일명과 찍을 화면을 정리했다. 각 모듈을 쓸 때 해당 캡처가 없으면 그 자리에 ⚠️ [스크린샷 필요] 표시를 남긴다.

### A-11
**규칙 8("각 파일을 코드 블록 하나로 출력")** ↔ 이 세션은 사용자 PC 폴더에 파일을 직접 쓸 수 있다.
- **조치**: 파일을 리포지토리 구조 그대로 직접 만들고, 대화창에는 요약만 낸다(긴 문서를 코드 블록으로 붙이면 복사 과정에서 표·이미지 경로가 깨지기 쉽다). 코드 블록 출력이 꼭 필요하면 요청 시 제공한다.

### A-12
**규칙 1(출처는 "(매뉴얼 p.xx) 또는 (데이터시트)")** ↔ 실제 근거가 Help·설정파일·스크린샷에도 있다.
- **조치**: 출처 약어를 6종으로 늘렸다 → [기능 매트릭스 v2 0절](feature-matrix_v2.md#0-품번-확정).

---

## B. 자료 ↔ 자료

### B-01
| 자료 | 내용 |
|---|---|
| (데이터시트) 첫 문단 | "…for various tasks such as checking for presence and quality inspection, **expanded function**." |
| (매뉴얼 p.403) | 8058732 = SBSI-F-R3C-F12-W, **Standard** 표에 있음. AF 형식(8058734)이 Advanced |
| (매뉴얼 p.409) | Type key: `AF` = Extended (at functional range) |
| [0] 장비 보고값 | 변수(Variant) = Standard |
| (데이터시트) 기능 항목 | "Function of detectors: Position tracking via contour, Contrast, Colour surface" — Standard 구성과 일치 |

- **판정**: **Standard**. 데이터시트 첫 문단의 "expanded function"은 오기로 본다.

### B-02
검출기 최대 수: (데이터시트) "Max. number of test criteria/detectors: **2**" ↔ (매뉴얼 p.19) Color Standard "Number of detectors: **32**", (매뉴얼 p.48) "max. 32 or 255 detectors".
- 데이터시트의 "2"는 검출기 **종류** 수(Contrast, Color area)일 가능성이 있다. 확정은 장비에서 한다 → ⚠️ V-01.
- 그 전까지 레슨과 최종 프로젝트는 **잡당 검출기 2개 이하**로도 성립하게 설계한다(안전한 쪽).

### B-03
시리얼: (데이터시트) "Serial interface, type: RS 232 / RS 422" ↔ (매뉴얼 p.20) Standard 칸 공란, (매뉴얼 p.32) "Not with Object-, Color-Standard version", (매뉴얼 p.395).
- 설정파일 `Configuration_R3C.xml`에는 Serial 항목이 있지만 이는 R3C 공통 파일이다.
- **판정**: 미지원. ⚠️ V-09에서 Output › Interfaces 탭에 RS422가 보이는지 확인.

### B-04
디지털 I/O:
| 자료 | 내용 |
|---|---|
| (데이터시트) | 디지털 입력 2, 출력 2, 입·출력 선택 가능 2 |
| (매뉴얼 p.20) | "4 digital outputs, 2 inputs", "Free definable digital In-/Outputs: **2**(Standard) / 4(Advanced)" |
| (Help: scoutputiosettings) | "Pin 05 - 08, can be used as input or output" (전 기종 공통 설명) |
| (매뉴얼 p.31) | 핀 05·06은 "*5 Not available with all Standard types" |
| (스크린샷 cs_output_io-mapping) | 03 WH, 10 VT(입력) / 12 RDBU, 09 RD(출력) / 07 BK, 08 GY(전환) — 6개만 표시 |

- **판정**: 입력 2(03, 10) + 출력 2(12, 09) + 전환 2(07, 08) + 고정 출력 Ready(04)·Valid(11). 매뉴얼의 "출력 4"는 Ready·Valid를 포함한 수로 보인다. 데이터시트와 화면이 일치한다.

### B-05
출력 전류: (데이터시트) "Max. output current 50 mA" ↔ (매뉴얼 p.395), (설치설명서) "50 mA, Ejector (Pin 12 / RDBU) **100 mA**".
- **조치**: 핀 12만 100 mA, 나머지 50 mA로 표기. 램프·릴레이 결선 시 부하 전류를 먼저 확인하도록 경고한다.

### B-06
| 항목 | (데이터시트) | (매뉴얼 p.395–396) |
|---|---|---|
| 외형 | 45 × 45 × 76.7 mm (W×L×H) | 65 × 45 × 45 mm (without plug) |
| 보호등급 | IP67 | IP65/67 |
| 진동 | EN 60068-2-6 | EN 60947-5-2 (Vibration / shock) |
- 측정 기준(커넥터 포함 여부 등)이 다른 것으로 보인다. 설치 브래킷 설계가 필요하면 실측한다 → ⚠️ V-13.

### B-07
(데이터시트) "Focal depth: 12 mm" ↔ (매뉴얼 p.403) Focal length 12, Depth of focus "Normal". 형식명 `F12` = 12 mm 광학계(매뉴얼 p.409).
- **판정**: 초점**거리**(focal length) 12 mm로 해석.

### B-08
일반 사이클 타임: (데이터시트) Pattern 30 / Caliper 12 / BLOB 50 ms ↔ (매뉴얼 p.396) Pattern 20 / Caliper 8 / BLOB 30 ms.
- 이 품번에서 쓰는 값(Contrast 2 ms, Color area 30 ms, 위치 추적(Contour) 30 ms)은 두 자료가 같다. 레슨에서는 실측값을 기록해 비교한다.

### B-09
| 항목 | (Help: scjobgeneral) | (설정파일 Configuration_R3C.xml) |
|---|---|---|
| R3C 해상도 | WVGA, VGA, QVGA | WVGA, VGA, QVGA, **QQVGA** |
| Dynamic | "Linear", "**High**" | "Linear", "**HDR**" |
- 실제 드롭다운으로 확정 → ⚠️ V-02, V-03.

### B-10
(Help: scalignment), (매뉴얼 p.97) "Three different detection methods (alignment detectors) are available" ↔ (매뉴얼 p.19) Standard "Alignment: Contour only", (스크린샷 cs_alignment) Method = None / Contour detection.
- **판정**: 이 품번은 Contour detection만. Help 번역에는 "※ 이 품번은 Contour detection만 표시됨" 주석을 단다.

### B-11
(Help: scjobwhitebalance)의 그림 탭 목록에는 `Calibration`이 있지만, 실제 화면은 Image acquisition / White balance / Pre-processing / Cycle time 4개뿐이다(스크린샷 cs_job_white-balance). 캘리브레이션은 Advanced 전용(매뉴얼 p.19). → A-04

### B-12
(매뉴얼 p.247) "Please see also installed help: …\Program files\Festo\SBS vision sensor\Utilities\Ethernet" ↔ 실제 설치 폴더에는 `Tools\EtherNetIP`, `Tools\Profinet`만 있고 `Utilities\Ethernet`은 없다.
- **조치**: Module 06(선택)에서 Python 수신 스크립트를 직접 제공한다.

### B-13
- 설치 폴더에 영문 사용자 매뉴얼이 두 개 있다: `SBS_user_manual_en_V_1_23_2.pdf`(2018, 563쪽)와 `23438122_SBS_user_manual_en.pdf`(2021, 400쪽, 2.x 세대용). 펌웨어 1.23.2.2와 맞는 **V1.23.2**를 쓴다.
- Help는 `V1_22_14`(chm)로 펌웨어보다 버전이 조금 낮다. 화면 표시 내용과 일치하는지는 스크린샷의 Help 문구로 대조했다(Tab Image acquisition, Setup Alignment, Tab I/O mapping, Tab White balance 일치).

### B-14
(데이터시트) "Product to be discontinued … Available until 2024." → 교체품 확보가 어려울 수 있다.
- **조치**: Module 07에서 잡셋·백업 절차(매뉴얼 p.322)를 필수 실습으로 둔다. 펌웨어 업데이트는 **절차 학습만** 하고, 실제 실행은 강사 승인 후에만 한다.

### B-15
(Help: scjobedit) Job 목록 아래 버튼 = `New`, `Open`, `Save`, `Delete`, `Delete all`, `Protect` ↔ 실제 화면 = `New`, `Load`, `Save`, `Delete`, `Delete all` (스크린샷 cs_job_image-acquisition). `Protect` 버튼은 화면에 없다.
- **조치**: 화면 표기(`Load`)를 쓴다. 잡셋 보호는 File 메뉴의 "Protect job set ..."(Help: scprotectjobset)로 확인한다 → Module 07에서 메뉴 캡처(cs_menu_file.png) 후 확정.

### B-16
(Help: sctrigger) "Select the required trigger mode in the job settings in the **General** tab" ↔ 실제 화면에는 General 탭이 없고 Trigger mode가 `Job › Image acquisition`에 있다(스크린샷 cs_job_image-acquisition).
- **조치**: 레슨에서는 `Image acquisition` 탭으로 안내하고 번역문에 ※ 주석을 단다.

### B-17
(Help: scdetectormethod)의 검출기 표는 Color area 이후 설명 열이 한 칸씩 어긋나 있다(예: "Color area — Barcode reading 1D Codes"). 매뉴얼 p.125도 같은 오류.
- **조치**: 각 검출기 장(Color area p.217 등)의 설명으로 맞춰 번역하고 ※ 주석을 단다.

### B-18
(Help: scdetectorcontrast, scdetectorcolorarea) Search region = Rectangle, Circle, **Free shape** ↔ (매뉴얼 p.20) Color Standard "Free shape of ROI: **Contour only**".
- **조치**: Standard에서는 Contrast·Color area의 Free shape가 막혀 있을 가능성. ⚠️ V-11. 막혀 있으면 사각형/원 여러 개로 대체한다(04 함정 표).

---

## C. 화면(스크린샷) ↔ 자료

### C-01
상태표시줄 DOUT 영역에 `12 09 05 06 07 08`이 표시된다(스크린샷 cs_alignment_status-bar). 그러나 I/O mapping에는 05·06이 없다(A-06).
- 표시만 남은 것인지, 출력이 실제로 있는지 모른다 → ⚠️ V-05.

### C-02
화면 설정: Internal illumination **Off**, Shutter speed **50.008 ms**(스크린샷 cs_job_image-acquisition).
(Help: scjobgeneral) "Maximum duration of internal illumination pulse is **8 ms**. Shutter timers longer than 8 ms just make sense, if internal and external illuminations are used."
- 지금 영상은 실내 조명에만 기대고 있고 색도 파랗게 치우쳐 있다. 오류라기보다 **Module 02의 출발점**으로 쓴다(내장 조명 On + 셔터 8 ms 이하 + 화이트 밸런스 Teach 실험).

### C-03
Device Manager 오른쪽 Help 영역의 Property 표(IP 192.168.100.125, R3B, Object, FW 1.18.19.2)는 **Help 예시 그림**이다. 이 장비 값이 아니다(이 장비: 192.168.3.40, R3C, Color, 1.23.2.2).


---
출처 링크: Festo 다운로드·문서 안내 <https://www.festo.com/sp> (8058732 검색) · 데이터시트 `8058732.pdf` · 매뉴얼 `SBS_user_manual_en_V_1_23_2.pdf` · Help `SBS_ContextHelp_en_V1_22_14.chm`
