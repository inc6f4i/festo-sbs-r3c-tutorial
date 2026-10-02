# 🔍 장비 앞에서 확인할 목록 (⚠️ 실기 확인 필요)

자료만으로 확정할 수 없거나 자료끼리 다른 항목이다. 확인하면 **결과·날짜·스크린샷 파일명**을 적고, 관련 문서는 새 버전 파일로 고친다.

> [!TIP]
> 설정을 바꾸기 전에 **File › Save job set (Backup) ...** (Help: scjobset)으로 현재 상태를 `backups/`에 먼저 저장한다. 확인이 끝나면 **File › Load job set (Backup) ...** 으로 되돌린다.
> 불러오면 센서에 있던 잡이 **모두 지워진다**(Help: scjobset). 메뉴 이름이 화면과 다르면 화면 표기를 따르고 기록한다.

| ID | 확인할 것 | 왜 (상충 ID) | 방법 | 판정 기준 | 결과 |
|---|---|---|---|---|---|
| V-01 | 잡당 검출기 최대 수 | B-02 (2 ↔ 32) | Detector › `New`로 Contrast를 3개 이상 추가. 3번째가 막히는지 본다 | 3개 이상 추가되면 매뉴얼(32)이 맞음 | |
| V-02 | 해상도 QQVGA 표시 여부 | B-09 | Job › Image acquisition › Resolution 드롭다운 펼쳐서 캡처 | 목록 그대로 기록 | |
| V-03 | Dynamic 선택지 이름 | B-09 | Job › Image acquisition › Dynamic 드롭다운 | "High"인지 "HDR"인지 | |
| V-04 | 검출기 목록 | A-03 | Detector › `New` 창 캡처 | Contrast, Color area만 보이면 확정 | |
| V-05 | 상태표시줄 DOUT 05·06의 의미 | C-01 | Start sensor 후 OK/NG를 번갈아 넣으며 DOUT 05·06 색 변화 관찰 + 핀 5·6 선 전압 측정 | 변화·전압 없음 → "표시만 있음" | |
| V-06 | 케이블 선 색 = 핀 번호 | 결선 안전 | 케이블 라벨 확인, 멀티미터 도통 시험으로 12선 전부 매핑 | [사양서 4.1](../hardware/sensor-spec-and-cabling.md#41-24-v-dc--io--m12-12핀-a-coded) 표와 일치 | |
| V-07 | 현재 PNP/NPN 설정 | 결선 안전 | Output › Interfaces › Internal I/O | 결선 방식과 같아야 함 | |
| V-08 | 최대 잡 수 8 | 매뉴얼 p.19 | Job 목록에서 `New`를 9번 | 9번째에서 막히면 확정 | |
| V-09 | RS422 항목 유무 | B-03 | Output › Interfaces 탭 캡처 | RS422가 없거나 비활성이면 미지원 확정 | |
| V-10 | SBS Calculator 기기 목록 | A-02 | SBS Calculator › Field of view › Device type 드롭다운 | 736×480 / R3C 항목 유무 | |
| V-11 | "Free shape of ROI: Contour only" 의미 | 매뉴얼 p.20 | Contrast·Color area ROI에서 도형/마스크 메뉴(우클릭 포함) 확인 | 사각형 외 형상이 가능한지 | |
| V-12 | 전원 투입 후 준비 시간 | 매뉴얼 p.395 (13 s) | 전원 ON부터 Device Manager LED가 녹색이 될 때까지 스톱워치 3회 | 평균값 기록 | |
| V-13 | 외형 치수 | B-06 | 캘리퍼스로 W·L·H(커넥터 포함/제외) 측정 | 두 자료 중 어느 기준인지 | |
| V-14 | 실습용 표시등·버튼·외부 조명 보유 여부 | Module 02·05 준비 | 실습실 비품 확인 | 없으면 DOUT 표시 + 멀티미터로 대체 | |

## 확인 기록 예시

```text
V-01 | 2026-10-__ | Contrast 3개 추가 성공(4개째도 성공) → 매뉴얼 32 채택 | images/raw/verify_v01.png
```
