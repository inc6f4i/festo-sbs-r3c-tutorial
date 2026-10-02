# 📊 기능 매트릭스 v2 + 최종 커버리지 검증 — SBSI-F-R3C-F12-W (8058732, Color **Standard**)

v2: 레슨 작성 완료 후 "다루는 레슨"을 실제 링크로 바꾸고, Module 06 변경(PC 연동 → 출력 24 V)과 최종 커버리지를 반영했다. 1차 판은 [feature-matrix.md](feature-matrix.md).

## 0. 품번 확정

| 항목 | 값 | 출처 |
|---|---|---|
| 품번 / 형식 | 8058732 / SBSI-F-R3C-F12-W | (데이터시트), (매뉴얼 p.403) |
| 변형 | **Standard** (형식명에 `AF` 없음) | (매뉴얼 p.403, p.409) |
| 장비 보고값 | R3C / Color / Standard / FW 1.23.2.2 | [0] 입력값 |
| 설치 SW 기능 그룹 | group 2 = Contrast, ColorArea, ContourAlignment | (설정파일 `Color/DetectorCapabilityTable.xml`) |

**출처 약어**: (매뉴얼 p.xx) = `SBS_user_manual_en_V_1_23_2.pdf` · (데이터시트) = `8058732.pdf` · (설치설명서) = `SBS_MountingInstruction_en_V_1_23_2.pdf` · (Help: 파일) = `SBS_ContextHelp_en_V1_22_14.chm` · (설정파일) = `SBSConfig/1.23.2.2/Data/*.xml` · (스크린샷) = `images/raw/`
링크: Festo 다운로드·문서 안내 <https://www.festo.com/sp> (8058732 검색)

[M00]: ../00_device-map.md
[M01]: ../01_connection-first-image.md
[M02]: ../02_image-quality.md
[M03]: ../03_alignment-contour.md
[M04]: ../04_inspection-detectors.md
[M05]: ../05_judgement-and-output.md
[M06]: ../06_output-24v.md
[M07]: ../07_operation-maintenance.md
[M08]: ../08_capstone.md
[ADV]: ../appendix/advanced-only.md

## 1. 기능 매트릭스

| 분류 | 기능 | 품번 지원 | 근거 | 다루는 레슨 | 실습 유형 |
|---|---|---|---|---|---|
| 영상 | 해상도 WVGA / VGA / QVGA | ✅ | (Help: scjobgeneral) | [M02] | 해상도 결정, 검출기 삭제 고장 주입 |
| 영상 | 해상도 QQVGA | ⚠️ V-02 | Help ↔ 설정파일 | [M02] | 드롭다운 확인 |
| 영상 | 40 fps | ✅ | (데이터시트) | [M05] | Statistics 처리 시간 |
| 영상 | Shutter 0.017–100 ms, Auto shutter | ✅ | (Help: scjobgeneral), (설정파일) | [M02] | 셔터 단계별 ΔI |
| 영상 | Gain 0.75–4 | ✅ | (설정파일) | [M02] | 노이즈 σ |
| 영상 | Dynamic Linear / High | ✅ ⚠️ V-03 | (Help: scjobgeneral) | [M02] | 광택 부품 비교 |
| 영상 | 내장 조명 On/Off, Quadrants | ✅ | (Help: scjobgeneral), (매뉴얼 p.20) | [M02] | 반사 감소 |
| 영상 | 외부 조명 출력(핀 09, Off/On/Permanent) | ✅ | (Help: scjobgeneral), (설정파일) | [M02] | DOUT 09·전압 |
| 영상 | 초점 나사, Focussing aid | ✅ ⚠️ V-16 | (매뉴얼 p.30), (Help: scview) | [M01] | 거리별 초점 |
| 영상 | White balance (Active, Teach, Reset) | ✅ | (Help: scjobwhitebalance) | [M02] | Teach 전후 값 |
| 영상 | Pre-processing (필터 5 + 배치 1) | ✅ | (Help: scjobpreprocessing) | [M02] | 필터별 노이즈·결함 소실 |
| 영상 | Calibration | ❌ | (매뉴얼 p.19) | [ADV] | — |
| 잡 | Cycle time 탭 (Max cycle, Min/Max processing, LED-Power, Repeat, Shutter variation) | ✅ | (Help: scjobtimeout) | [M05] | 타임아웃 고장 주입 |
| 잡 | 잡 최대 8, 템플릿 | ✅ ⚠️ V-08 | (매뉴얼 p.19, p.48) | [M07] | 잡 2개 전환 |
| 정렬 | Contour detection (Color channel / Parameters / Optimization / Speed / Result offset) | ✅ | (매뉴얼 p.19), (스크린샷) | [M03] | ±mm, ±° 추종 범위 |
| 정렬 | Pattern matching, Edge | ❌ | (매뉴얼 p.19) | [ADV] | — |
| 검출기 | Contrast | ✅ | (매뉴얼 p.19) | [M04] 04-1 | OK/NG 10/10, 마진 |
| 검출기 | Color area (RGB/HSV/LAB, histogram, Thresholds, Object size) | ✅ | (매뉴얼 p.19) | [M04] 04-2, 04-3 | 색 모델 비교, 크기 Go/No-Go |
| 검출기 | 잡당 검출기 수 32 | ⚠️ V-01 | 매뉴얼 32 ↔ 데이터시트 2 | [M04], [M08] 설계 B | — |
| 검출기 | Free shape ROI / Mask | ⚠️ V-11 | Help ↔ 매뉴얼 p.20 | [M04] | — |
| 검출기 | Pattern, Contour, Gray, Brightness, Caliper, BLOB, Color value/list, 코드류 | ❌ | (매뉴얼 p.19) | [ADV] | — |
| 판정 | Result(PC) / Start sensor / Statistics | ✅ | (Help: scresult, scstart, svstatistics) | [M05] | 처리 시간 |
| 판정 | Digital output 논리 (Overall job result, Invert, Standard / Formula) | ✅ | (Help: scoutputlogic*) | [M05] | 출력 계획 표 |
| 판정 | 트리거: 화면 Trigger, H/W 핀 03, Enable Trigger | ✅ | (Help: sctrigger, scoutputiosettings) | [M05] | 버튼 20회 = Count 20 |
| 판정 | Timing (Trigger delay, Result delay, Reset signal, Duration) | ✅ | (Help: scoutputtiming) | [M05] | Result duration 펄스 |
| 출력 | I/O mapping (03, 10 / 12, 09 / 07, 08 전환) | ✅ | (스크린샷), (매뉴얼 p.31) | [M06] | 핀 07 = Result |
| 출력 | Internal I/O PNP/NPN | ✅ ⚠️ V-07 | (Help: scoutputsettings) | [M06] | NPN 고장 주입 |
| 출력 | **검출 시 24 V ON** | ✅ | (매뉴얼 p.31, p.395) | [M06] | 멀티미터 OK 24 V / NG 0 V |
| 출력 | Ready(04) / Valid(11) | ✅ | (Help: scoutputtiming) | [M05], [M06] | 표시등(선택) |
| 출력 | 핀 05·06, 엔코더, I/O 확장 | ❌ | (매뉴얼 p.20, p.31) | [ADV] | — |
| 입력 | Job 1 or 2 / 2진 / 펄스 잡 전환 | ✅ ⚠️ V-19 | (Help: scoutputiosettings), (설정파일 IN2) | [M07] | 핀 10 스위치 |
| 입력 | Teach temp / perm, Repeat mode enable | ✅ | (Help: scoutputiosettings) | [M06] 번역·설명 | 설명 |
| 통신 | Ethernet TCP/IP 텔레그램 | ✅(장비) / 규칙 9로 미사용 | (매뉴얼 p.247) | [M07] Telegram 번역(CSV 내용 정의용) | — |
| 통신 | PROFINET, EtherNet/IP | ✅(장비) / 규칙 9로 제외 | (매뉴얼 p.20) | [ADV] | — |
| 통신 | RS422 / RS232 | ❌ ⚠️ V-09 | (매뉴얼 p.20, p.32) | [ADV] | — |
| 운영 | 잡/잡셋 저장·불러오기·보호 | ✅ | (Help: scjobset, scprotectjobset) | [M07] | 백업→삭제→복원 |
| 운영 | Image recorder, RAM disk | ✅ | (Help: scjobtransmit, scimagerec) | [M07] | Fail만 기록 |
| 운영 | Archiving FTP / SMB | ✅ ⚠️ V-18 | (Help: scjobarchive) | [M07] | FAIL 폴더 |
| 운영 | 필름스트립 / 오프라인 시뮬레이션 | ✅ | (Help: scfilmstripedit, scfilmstrip) | [M02], [M04] | OK/NG 필름 |
| 운영 | SBSxWebViewer | ✅ | (Help: svwebviewbase) | [M07] | 연결 1개 제한 |
| SW | SBS Calculator (Working distance / Field of view) | ⚠️ V-10 (R3C 목록 없음) | (SBS Calculator 리소스) | [M00] | 계산 vs 실측 |
| SW | Device Manager: 찾기·추가·세부 사항·네트워크 설정·시뮬레이션 | ✅ | (Help: sf*) | [M01] | 검색 5/5 |
| SW | Device Manager: 즐겨찾기·비밀번호·펌웨어 업데이트·Auto Start Up | ✅ | (Help: sffavorite, sfuseradmin, sfupdate, sfautostart) | [M07] | 절차·캡처(펌웨어 실행 안 함) |
| SW | Configuration Studio 전체 | ✅ | (Help: sc*) | [M01]–[M08] | — |
| SW | Visualisation Studio (Freeze, Zoom, Archiving, Result, Statistics, Job select, Job upload) | ✅ | (Help: sv*) | [M07] | NG만 아카이빙 |
| 하드웨어 | 사양·핀 배치·실습 결선 | ✅ | (매뉴얼 p.29–34, p.395–396) | [사양서](../hardware/sensor-spec-and-cabling.md), [M01], [M06] | 도통 시험 |

## 2. 최종 커버리지 검증

| 확인 | 결과 |
|---|---|
| ✅ 지원 기능 중 레슨이 없는 항목 | **없음** — 위 표의 모든 ✅ 항목에 레슨 링크 있음 |
| 실습(실물 시료 실험)이 없는 레슨 | 없음 — M00은 Module 01 이후 FOV 실측, M07은 백업 복원·NG 저장 실험 |
| 설명만 하고 실행하지 않는 기능 | 펌웨어 업데이트(단종 품번·장비 소유 문제로 절차만), Teach/Repeat mode 입력(설명만), 비밀번호(설정 후 해제) |
| 규칙 9로 제외 | PROFINET, EtherNet/IP, Ethernet 텔레그램 실습 |
| Help 번역 | 이 품번 해당 토픽 전부 번역 → [Help 색인 v2](../help-ko/README_v2.md) |
| 스크린샷 | 8장 주석 완료, 나머지는 레슨 안 ⚠️ [스크린샷 필요] + [촬영 목록](../../images/CAPTURE-LIST.md) |

### 보완이 남은 항목 (장비 확인 후)

| 항목 | 이유 | 확인 후 할 일 |
|---|---|---|
| V-01 검출기 수 | 2개면 최종 프로젝트 설계 B | M08 설계 확정 |
| V-11 Free shape | 막혀 있으면 마스크 레슨 불가 | M04 함정 표 갱신 |
| V-15 파라미터 범위 | 자료에 수치 없음 | M03·M04 파라미터 표에 범위 기입 |
| V-18 SMB 필터 | Fail만 저장 가능한지 | M07 방법 2 확정 |
| V-19 핀 10 잡 전환 | 화면 목록 미확인 | M07 7.2 확정 |
| V-20 정렬 실패 시 결과 | 논리식 설계에 영향 | M08 3절 확정 |

⚠️ 전체 목록: [장비 앞에서 확인할 목록 v2](../appendix/verify-on-device_v2.md) (V-01 ~ V-22)
