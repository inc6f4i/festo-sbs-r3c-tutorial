# 🔍 장비 앞에서 확인할 목록 v2 (⚠️ 실기 확인 필요)

자료만으로 확정할 수 없거나 자료끼리 다른 항목이다. 확인하면 **결과·날짜·스크린샷 파일명**을 적고, 관련 문서는 새 버전 파일로 고친다.
v2: 레슨 작성 중 새로 나온 V-15 ~ V-22 추가.

> [!TIP]
> 설정을 바꾸기 전에 **File › Save job set (Backup) ...** (Help: scjobset)으로 현재 상태를 `backups/`에 먼저 저장한다. 확인이 끝나면 **File › Load job set (Backup) ...** 으로 되돌린다.
> 불러오면 센서에 있던 잡이 **모두 지워진다**(Help: scjobset). 메뉴 이름이 화면과 다르면 화면 표기를 따르고 기록한다.

| ID | 확인할 것 | 왜 (상충 ID) | 방법 | 판정 기준 | 관련 레슨 | 결과 |
|---|---|---|---|---|---|---|
| V-01 | 잡당 검출기 최대 수 | B-02 (2 ↔ 32) | Detector › `New`로 Contrast를 3개 이상 추가 | 3개 이상 추가되면 매뉴얼(32) | 04, 08 | |
| V-02 | 해상도 QQVGA 표시 여부 | B-09 | Resolution 드롭다운 캡처 | 목록 그대로 기록 | 02 | |
| V-03 | Dynamic 선택지 이름 | B-09 | Dynamic 드롭다운 캡처 | "High" / "HDR" | 02 | |
| V-04 | 검출기 목록 | A-03 | Detector › `New` 창 캡처 | Contrast, Color area만 | 04 | |
| V-05 | 상태표시줄 DOUT 05·06의 의미 | C-01 | Start sensor 후 OK/NG 반복 + 핀 5·6 전압 | 변화·전압 없음 → 표시만 | 05 | |
| V-06 | 케이블 선 색 = 핀 번호 | 결선 안전 | 라벨 확인 + 멀티미터 도통 12선 | 사양서 4.1 표와 일치 | 01, 06 | |
| V-07 | 현재 PNP/NPN 설정 | 결선 안전 | Output › Interfaces › Internal I/O | 결선과 같아야 함 | 06 | |
| V-08 | 최대 잡 수 8 | 매뉴얼 p.19 | `New` 9번 | 9번째에서 막힘 | 07 | |
| V-09 | RS422 항목 유무 | B-03 | Output › Interfaces 캡처 | 없음/비활성 = 미지원 | 06 | |
| V-10 | SBS Calculator 기기 목록 | A-02 | Field of view › Device type 드롭다운 | 736×480 항목 유무 | 00 | |
| V-11 | Contrast·Color area의 Free shape | B-18 | Search region 드롭다운, Edit search region 활성 여부 | 선택 가능 여부 | 04 | |
| V-12 | 전원 투입 후 준비 시간 | 매뉴얼 p.395 (13 s) | 스톱워치 3회 | 평균값 | 01 | |
| V-13 | 외형 치수 | B-06 | 캘리퍼스 W·L·H | 어느 기준인지 | — | |
| V-14 | 표시등·버튼·외부 조명 보유 | M02·05·06 준비 | 비품 확인 | 없으면 DOUT + 멀티미터 | 02, 05, 06 | |
| V-15 | 파라미터 범위·기본값·단위 (Contour: Threshold, Angle/Scale range, Min. contrast / Contrast: Threshold / Color area: 채널 범위, Threshold %, Object size 단위) | 자료에 수치 없음 | 각 탭 기본값 캡처, 스핀박스 최소/최대까지 돌려 보기 | 표로 기록 | 03, 04 | |
| V-16 | 초점 보조 표시 | Help: scview "Focussing aid" | `View` 메뉴 캡처, 켰을 때 표시 형식(숫자/막대) | 메뉴명·표시 기록 | 01 | |
| V-17 | 상태표시줄 `I:` 값의 의미(컬러 영상) | Help: sc "pixel intensity" | 흰/빨/검 종이에서 I 값 비교 | 회색값인지 채널값인지 | 02 | |
| V-18 | SMB/FTP 아카이빙의 Pass/Fail 필터 | Help: scjobtransmit "selectable with / without filtering" | Archiving 탭 전체 캡처 | "Fail만" 설정 가능 여부 | 07 | |
| V-19 | 핀 10 VT의 `Job 1 or 2` 선택 가능 | 설정파일 IN2 Standard | I/O mapping › 10 VT Function 드롭다운 | 목록 기록 | 07 | |
| V-20 | 정렬 결과 표시와 정렬 실패 시 검출기 결과 | Help: scresult (Contour 위치값) | Result 탭에서 정렬 항목 확인, 시료를 검색 영역 밖에 두고 검출기·잡 결과 기록 | 정렬 실패 → 잡 NG인지 | 03, 08 | |
| V-21 | 바탕화면/시작 메뉴 아이콘 이름 | 매뉴얼 p.44 "SBS vision sensor" | 바탕화면·시작 메뉴 확인 | 이름 기록 | 00 | |
| V-22 | PNP 출력 ON 전압(부하 유/무) | 자료에 전압 강하 값 없음 | 멀티미터 | 실측값을 06 합격 기준으로 | 06 | |

## 확인 기록 예시

```text
V-01 | 2026-10-__ | Contrast 3개 추가 성공(4개째도 성공) → 매뉴얼 32 채택 | images/raw/verify_v01.png
```
