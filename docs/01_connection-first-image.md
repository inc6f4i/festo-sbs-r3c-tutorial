# Module 01 — 연결과 첫 이미지

> 현장 질문: **"센서와 PC가 말이 통하고, 초점 맞은 영상이 나오나?"**

## 🎯 목표
1. 센서에 전원·LAN을 연결하고 PC IP를 맞춰 Device Manager에서 센서를 **찾는다**.
2. Configuration Studio를 Online으로 열어 **라이브 영상**을 띄운다.
3. 초점 나사로 설치 거리에서 **초점을 맞추고** 그 상태를 수치로 남긴다.

## 🏭 왜 필요한가
현장에서 "센서가 안 잡힌다"는 문의의 대부분은 PC의 다른 네트워크 어댑터나 서브넷 불일치다. 순서대로 확인하는 습관이 없으면 멀쩡한 센서를 교체하게 된다.

## 📋 선행 조건 / 준비물
- [Module 00](00_device-map.md) — 설치 거리 결정
- [사양서 4절·5절](hardware/sensor-spec-and-cabling.md) 결선 완료 (최소: 핀 1 BN +24 V, 핀 2 BU 0 V, LAN)
- 스톱워치(휴대폰), 모눈종이, OK 시료 1개

---

## 1.1 전원 투입과 준비 시간

1. 쓰지 않는 DATA 소켓에 보호 캡이 있는지 확인한다(매뉴얼 p.28).
2. 24 V 전원을 켜고 스톱워치를 시작한다.
3. 센서 뒷면 **Pwr LED(녹색)** 가 켜지는지 본다(매뉴얼 p.29).
4. Device Manager 목록에서 센서가 나타날 때까지 시간을 잰다. 데이터시트상 준비 지연은 typ. 13 s(매뉴얼 p.395).

## 1.2 PC IP 확인

센서: **192.168.3.40 / 255.255.255.0** ([0] 입력값). PC는 같은 서브넷의 다른 주소여야 한다(매뉴얼 p.35). 현재 PC: **192.168.3.10** (스크린샷 dm_main 상태표시줄).

1. Windows `설정 › 네트워크 및 인터넷 › 이더넷 › (센서가 꽂힌 어댑터) › IP 할당 편집` — Windows 화면(Festo 자료 아님)
2. 수동, IPv4: `192.168.3.10`, 서브넷 `255.255.255.0`. .0, .255, 센서 주소(.40)는 쓰지 않는다(매뉴얼 p.35).

⚠️ [스크린샷 필요: `pc_ipv4.png`]

> [!WARNING]
> 이 PC에는 이더넷 어댑터가 둘 이상 있다(스크린샷 dm_main 상태표시줄 경고). Device Manager 상태표시줄의 `IP 주소 (PC)`가 **센서가 꽂힌 어댑터**의 주소인지 확인한다(매뉴얼 p.36).

## 1.3 Device Manager — 찾기·추가·세부 사항

### ⚙️ 메뉴 경로
`Vision Sensor Device Manager › 탐색 (Find)` / `› 활성화된 센서 추가 › IP 주소 › 추가 (Add)` / `› 활성화된 센서들 › 세부 사항` (매뉴얼 p.40, p.55–57)

![Device Manager](../images/annotated/dm_00_layout.png)

| 번호 | 할 일 |
|---|---|
| 6 | `탐색` 을 눌러 다시 검색 |
| 2 | 센서 행이 나타나면 첫 칸 LED 색 확인: 녹색 Run / 노랑 Config / 빨강 오류·시작 중 (Help 패널 문구) |
| 2 | 행 오른쪽 `세부 사항` → IP, Hardware(R3C), Sensor type(Color), Variant(Standard), Version(1.23.2.2) 확인 |
| 4 | 검색이 안 되면 IP `192.168.3.40` 입력 → `추가` |
| 8 | PC IP 확인 |

⚠️ [스크린샷 필요: `dm_details.png`, `dm_settings.png`]

### 📝 단계별 조작
1. Device Manager를 연다.
2. `탐색 (Find)`을 누른다. 목록에 센서가 나타나는 데 걸린 시간을 적는다.
3. 센서 행의 `세부 사항`을 눌러 [0] 입력값과 같은지 표로 대조한다.
4. 목록에서 센서 행을 오른쪽 클릭 → 목록에서 제거(Remove from list) → 4번 영역에 IP를 넣고 `추가` → 다시 나타나는지 확인한다(Help: sffavorite).
5. `설정 (Settings)`을 눌러 네트워크 설정 창을 **열어 보기만** 하고 캡처 후 **취소**한다.

> [!CAUTION]
> 설정 창에서 IP를 바꾸면 PC와 연결이 끊긴다. 이 레슨에서는 바꾸지 않는다. DHCP를 켰는데 DHCP 서버가 없으면 센서 IP가 0.0.0.0이 된다(매뉴얼 p.38).

<details>
<summary>📖 Help 번역 — Active sensors (Help: sfsensor)</summary>

연결된 네트워크에서 쓸 수 있는 모든 센서가 선택 목록 Active sensors에 표시된다.
- 연결된 센서 설정하기 (Vision Sensor Configuration Studio 호출)
- 이미지와 결과 데이터 표시하기 (Vision Sensor Visualisation Studio 호출)

**표시되는 파라미터의 의미**

| 파라미터 | 의미 |
|---|---|
| IP address | 네트워크상의 센서 IP 주소 |
| Hardware | 하드웨어 (예: R3B, R2B, …) |
| Sensor type | 센서 종류 (Object, Color, Code Reader) |
| Variant | 센서 하위 변형 (Advanced …) |
| Version | 펌웨어 버전 |
| Mode | 동작 모드 (Run, Config 또는 Offline) |
| Sensor name | 센서 이름 |
| Manufacturer | 제조사 이름 |
| Mac-Address | 센서 MAC 주소 |
| Subnet mask | 센서 서브넷 마스크 |
| Gateway | 기본 게이트웨이 |
| DHCP | DHCP 활성 / 비활성 |
| Operating system | 운영체제 종류 |
| Operating System Version | 운영체제 버전 |
| Platform | 예: SBS |
| Hardware | 하드웨어 버전 |
| RAM | RAM 크기 |
| Flash | 플래시 크기 |

참고:
- 센서가 연결되어 있는데도 목록에 아무것도 없으면 "Find" 버튼으로 목록을 새로 고치거나 제품의 IP 주소를 직접 "Add"할 수 있다.
- 센서가 연결되어 있지 않으면 Sensors for simulation mode 목록에서 'Object' 센서 같은 여러 센서 응용의 시뮬레이션을 쓸 수 있다.
- "details" 버튼(Active Sensors 파라미터 목록 오른쪽 위 모서리)을 누르면 SBS의 모든 파라미터를 자세히 볼 수 있다.
</details>

<details>
<summary>📖 Help 번역 — Sensors for simulation mode (Help: sfsimulation)</summary>

시뮬레이션 모드에 들어가려면 원하는 센서 종류를 더블클릭해 선택하고 "Config" 버튼을 누른다(Vision Sensor Configuration Studio 호출).

| 파라미터 | 기능 |
|---|---|
| Type | 센서 종류 (예: Object, Color, Code Reader, …) |
| Hardware | 하드웨어 종류 (예: 해상도, 흑백 또는 컬러 버전) |
| Version | 펌웨어 버전 |
| Variant | 센서 하위 변형 (예: Advanced …) |

"Config" 기능을 쓸 수 없으면(버튼 비활성) 비밀번호를 입력하는 로그인(문/화살표 기호 버튼)이 필요하다. 비밀번호를 모르면 관리자에게 문의한다.
</details>

<details>
<summary>📖 Help 번역 — Find / Add active sensor (Help: sfaddfind)</summary>

센서가 연결되어 있는데도 Active sensors 목록에 센서가 없으면 다음 순서를 따른다.

**센서 찾기(Find):** PC에 직접 연결되었거나 네트워크에 있는 센서를 찾으려면 "Find" 버튼을 누른다.

**활성 센서 추가(Add):** 센서의 IP 주소를 알면 IP-address 칸에 입력하고 "Add" 버튼을 누른다.

이제 센서가 목록에 나타나 Config나 View 등으로 접근할 수 있다.
"Config" 기능을 쓸 수 없으면(버튼이 비활성/회색) 비밀번호를 입력하는 로그인이 필요하다. 비밀번호를 모르면 현장 시스템 관리자에게 문의한다.
</details>

<details>
<summary>📖 Help 번역 — Configuring a connected sensor (Help: sfconfig)</summary>

목록에서 센서(시뮬레이션)를 선택하고 "Config" 버튼을 누른다. 설정 프로그램 Vision Sensor Configuration Studio가 실행되고, 현재 센서에 저장된 잡들이 선택 목록에 표시된다. Vision Sensor Configuration Studio를 호출할 때 비밀번호 입력이 필요할 수 있다. 비밀번호 정의는 User administration / Passwords를 본다.
</details>

<details>
<summary>📖 Help 번역 — Display images and result data (Help: sfview)</summary>

목록에서 센서를 선택하고 "View" 버튼을 누른다. Vision Sensor Visualisation Studio 프로그램이 열리고, 활성 잡의 이미지와 측정 결과가 화면에 표시된다.

참고: Vision Sensor Visualisation Studio를 호출해도 선택한 센서의 동작에는 영향이 없다.
</details>

<details>
<summary>📖 Help 번역 — Sensor's network settings (Help: sfset)</summary>

선택한 센서의 네트워크 설정은 Set 버튼으로 바꿀 수 있다. 여기서 IP 주소, 서브넷 마스크, 기본 게이트웨이, DHCP, 센서 이름을 설정할 수 있다. PC의 IP 주소와 서브넷 마스크는 Vision Sensor Device Manager 상태표시줄 아래에 표시된다. 센서를 PC에 연결하려면 주소 구조가 올바라야 한다. 따라서 필요하면 여기서 센서 IP 주소 등을 알맞게 바꿀 수 있다. 네트워크 파라미터는 현장 관리자에게 문의해 정한다. 자세한 내용은 Network settings, Short reference 장과 Network connection 장을 본다. "DHCP = active"를 선택하면 센서가 시작할 때마다 IP 주소가 새로 할당되어 바뀔 수 있으므로 센서에 고유한 이름을 붙여야 한다. 이 기능에는 관리자 권한이 필요하다(user administration 참조).
</details>

## 1.4 Configuration Studio 열기 — Online / Offline

### ⚙️ 메뉴 경로
`Device Manager › 센서 선택 › 구성 (Config)` → `Vision Sensor Configuration Studio – Color` (매뉴얼 p.44, p.60)

![Configuration Studio 화면 지도](../images/annotated/cs_00_layout.png)

| 번호 | 영역 | 이 레슨에서 할 일 |
|---|---|---|
| 5 | Connection mode `Online` / `Offline` | Online 확인 |
| 4 | Trigger/Image update `Single` / `Continuous` | Continuous로 라이브 영상 |
| 10 | Job › `Image acquisition` › Trigger mode | `Free run` 확인 |
| 11 | 상태표시줄 | Mode, Name(MASTER), Active job 확인 |

### 📝 단계별 조작
1. 센서 행을 선택하고 `구성 (Config)`을 누른다.
2. 상태표시줄에서 `Mode: Config`, `Name: MASTER`, `Active job`을 확인한다(스크린샷 cs_00 ⑪).
3. **라이브 영상 만들기** (Help: sctrigger):
   - Setup `Job` › 탭 `Image acquisition` › Trigger mode = `Free run`
   - 왼쪽 Trigger/Image update = `Continuous`
4. `Single`을 눌러 영상이 멈추는지, `Continuous`로 다시 흐르는지 확인한다.
5. `Offline`으로 바꿔 본다 → 센서 없이 필름스트립 이미지로 동작하는 모드다. 다시 `Online`.

<details>
<summary>📖 Help 번역 — Connection mode (Help: scconnection)</summary>

센서 설정과 시험 운전에는 두 가지 동작 모드가 있으며, Connection mode 창에서 고른다.
- **Online mode:** 센서를 연결한 상태에서 설정
- **Offline mode:** 필름스트립에 저장된 이미지로 센서를 시뮬레이션

센서가 연결되어 있으면 두 모드를 모두 쓸 수 있고 서로 전환할 수 있다. 센서가 없으면 Offline 모드, 즉 센서 시뮬레이션으로만 작업할 수 있다.
</details>

<details>
<summary>📖 Help 번역 — Trigger settings (Help: sctrigger)</summary>

잡 설정의 "General" 탭에서 원하는 트리거 모드를 고른다. (※ 이 버전 화면에서는 `Image acquisition` 탭의 `Trigger mode`)

| 파라미터 | 기능 |
|---|---|
| Triggered | 외부 트리거 또는 Vision Sensor Configuration Studio 화면의 트리거 버튼으로 동작 |
| Free run | 자동으로 도는 자체 트리거로 동작. 센서가 가능한 최대 빈도로 이미지를 공급 |

Trigger/Collect image 영역의 옵션 버튼으로 센서가 이미지를 어떤 형태로 공급할지 고른다.

| 파라미터 | 기능 |
|---|---|
| Single image | 이미지 한 장 기록. 다음 경우 한 번 촬영한다: 1. Trigger mode = triggered: 첫 외부 트리거 신호 또는 Vision Sensor Configuration Studio 화면의 트리거 버튼 / 2. Trigger mode = free run: Vision Sensor Configuration Studio 화면의 "Single image" 버튼을 처음 누를 때 (예: 설정 모드에서 중요) |
| Continuous | 이미지를 연속 공급. 다음 경우 계속 촬영한다: 1. Trigger mode = triggered: 외부 트리거마다 또는 트리거 버튼을 누를 때마다 / 2. Trigger mode = free run: 최대 빈도의 내부 자체 트리거로 계속 |

Job 설정에서 노출 시간, 증폭(게인), 조명, 해상도 파라미터를 바꾸면 센서에 새 이미지가 자동으로 요청된다.

트리거 없이도 계속 갱신되는 라이브 이미지를 얻으려면 다음을 (필요하면 임시로) 설정한다.
- "Job/General"에서 free run으로 설정
- "Trigger / Collect image"에서 continuous로 설정
</details>

## 1.5 초점 맞추기

### ⚙️ 메뉴 경로
센서 뒷면 초점 나사(매뉴얼 p.30): **시계 방향 = 먼 거리, 반시계 방향 = 가까운 거리**
보조 표시: `View` 메뉴 › Focussing aid (Help: scview) — ⚠️ 이 버전의 정확한 메뉴 이름은 [스크린샷 필요: `cs_menu_view.png`]

<details>
<summary>📖 Help 번역 — Displays in image window (Help: scview)</summary>

**이미지 영역과 확대:** 표시 창 아래의 버튼이나 드롭다운 메뉴로 원하는 이미지 영역을 고를 수 있다.

**결과의 그래픽 표시:** View 메뉴에서 다음 그래픽을 켜거나 끌 수 있다.
- Bar graph result: 검사 결과를 막대그래프로 표시
- Drawings: 검출기와 정렬 검출기의 검색·파라미터·위치 프레임 표시
- Focussing aid: 이미지 선명도 표시 (Job 설정도 참조)
- Enlarged display: 별도의 확대 표시 창을 넣는다. 프레임 모서리의 조절 손잡이로 원하는 배율에 맞출 수 있다.

Vision Sensor Visualisation Studio 모듈은 이 기능 중 일부만 제공한다.
</details>

<details>
<summary>📖 Help 번역 — Controlling image reproduction (Help: scfilmstripnavigation)</summary>

표시 창 아래의 버튼과 슬라이드 바로 저장된 이미지의 선택과 재생을 제어할 수 있다. 이미지 카운터는 현재 이미지 번호와 활성 필름스트립의 이미지 수를 보여 준다.

| 버튼 | 기능 |
|---|---|
| (◀) | 이전 이미지로 |
| (▶) | 저장된 이미지 재생 시작 / 정지 |
| (▶│) | 다음 이미지로 |
| (▶▶│) | 마지막 이미지로. 통계가 초기화되고 모든 이미지가 평가된다. |
</details>

### 📝 단계별 조작
1. Module 00에서 정한 거리(예: 150 mm)에 모눈종이를 놓는다.
2. Job › Image acquisition에서 **Internal illumination = On**, Shutter speed를 영상이 하얗게 날아가지 않는 값으로 낮춘다(밝기 조절은 Module 02에서 자세히).
3. View 메뉴의 Focussing aid를 켠다.
4. 초점 나사를 한쪽 끝까지 돌린 뒤 반대로 천천히 돌리며, 모눈선이 가장 가늘게 보이는(Focussing aid 값이 최대인) 위치에서 멈춘다.
5. 화면을 캡처하고 Module 00의 FOV 실측을 한다.

## 🧪 실험 — 거리별 초점과 준비 시간

| # | 변수 | 값 | 측정 | 결과 |
|---|---|---|---|---|
| 1 | 전원 ON → 목록 표시 시간 | 3회 | s | |
| 2 | 작업 거리 | 100 mm | Focussing aid 최대값 ⚠️(표시 형식 확인) / 모눈 선명 여부 | |
| 3 | 작업 거리 | 150 mm | 〃 | |
| 4 | 작업 거리 | 200 mm | 〃 | |
| 5 | 150 mm에서 맞춘 초점으로 100 mm 시료 보기 | — | 흐려짐 정도(모눈선 구분 가능?) | |

## 🔍 검증
- `탐색` 후 센서 표시: 5회 중 5회 성공
- 세부 사항이 [0]과 일치: Hardware R3C / Color / Standard / 1.23.2.2 / 192.168.3.40
- 준비 시간 평균 기록(매뉴얼 typ. 13 s와 비교)
- 설치 거리에서 1 mm 모눈선이 화면 전체에서 구분됨

## 💥 고장 주입

| 해 볼 것 | 관찰할 증상 |
|---|---|
| PC IP를 192.168.**4**.10으로 바꾸고 `탐색` | 목록에 안 나타남 → `추가`로 IP를 넣어도 실패하는지 확인 → 원복 |
| LAN 케이블 분리 상태에서 Configuration Studio 사용 | 연결 끊김 메시지 / Offline만 가능한지 확인 → 메시지 캡처 |
| 초점 나사를 끝까지 돌림 | 영상이 흐려짐. Focussing aid 값 변화 기록 |
| Trigger mode = `Trigger`인데 Continuous | 영상이 안 바뀜 → 화면 `Trigger` 버튼을 눌러야 갱신되는 것 확인 |

## ⚠️ 함정과 해결

| 증상 | 원인 | 조치 |
|---|---|---|
| 목록이 비어 있음 | PC가 다른 어댑터/서브넷 | 상태표시줄 PC IP 확인, `추가`로 직접 입력 (Help: sfaddfind) |
| `구성` 버튼이 회색 | 비밀번호 보호 상태 | 열쇠 아이콘으로 로그인 (Help: sfsimulation) |
| LED 빨강이 오래감 | 시작 중 또는 오류 | 13 s 이상 기다린 뒤 전원 재투입 |
| 라이브 영상이 안 움직임 | Trigger mode = Trigger 또는 Single | Free run + Continuous (Help: sctrigger) |
| DHCP 켠 뒤 연결 불가 | DHCP 서버 없음 → 0.0.0.0 | 매뉴얼 p.38, 직결 후 재설정 |

## ✅ 체크리스트
- [ ] Pwr LED 녹색, 준비 시간 측정
- [ ] PC IP 192.168.3.10/24 (센서 쪽 어댑터)
- [ ] Device Manager에서 센서 찾기·추가·세부 사항 확인
- [ ] Configuration Studio Online, Free run + Continuous 라이브 영상
- [ ] 설치 거리에서 초점 고정, Module 00 FOV 실측 완료

## 📁 포트폴리오 기록
- 스크린샷: `dm_details.png`, 초점 맞춘 모눈 이미지
- 수치: 준비 시간 평균, 거리별 초점 결과
- 한 줄 요약 예: "다중 어댑터 PC에서 서브넷을 분리해 Festo SBS 비전 센서 연결 절차를 표준화(검색 성공 5/5, 준비 시간 평균 ○ s)"

---
출처 링크: Festo 다운로드·문서 안내 <https://www.festo.com/sp> (8058732 검색) · 로컬 Help 원본 `C:\Program Files (x86)\Festo\SBS Vision Sensor\Help\en\1.22.14.1\SBS_ContextHelp_en_V1_22_14.chm`
