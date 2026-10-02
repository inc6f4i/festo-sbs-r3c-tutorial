# 🔒 부록 — 상위 모델(Advanced / AF) 전용 기능

이 장비(SBSI-F-R3C-F12-W, Color **Standard**)에서는 쓸 수 없는 기능이다. 레슨으로 만들지 않고, "이런 문제는 상위 모델이 필요하다"를 알기 위한 목록으로만 둔다.
Color Advanced의 형식명은 **SBSI-F-AF-R3C-F12-W (8058734)** 이다. (매뉴얼 p.403)

| 기능 | Color Standard | Color Advanced | 출처 | Standard에서의 대안 |
|---|---|---|---|---|
| 잡 수 | 8 | 255 | (매뉴얼 p.19) | 잡을 품종별로 아껴 쓰기 |
| 정렬: Pattern matching, Edge | ❌ | ✅ | (매뉴얼 p.19) | Contour detection |
| 캘리브레이션(Scaling, Calibration plate, Point pair list) | ❌ | ✅ | (매뉴얼 p.19) | mm/px 수동 환산 |
| 검출기: Pattern matching, Contour | ❌ | ✅ | (매뉴얼 p.19) | 정렬 결과 + Contrast |
| 검출기: Gray, Brightness | ❌ | ✅ | (매뉴얼 p.19) | Contrast, Color area(밝기 범위) |
| 검출기: Caliper | ❌ | ✅ | (매뉴얼 p.19) | 경계 띠 Contrast로 Go/No-Go |
| 검출기: BLOB | ❌ | ✅ | (매뉴얼 p.19) | Color area 면적 |
| 검출기: Color value, Color list | ❌ | ✅ | (매뉴얼 p.19) | Color area 여러 개 |
| 검출기: Barcode, Datacode, OCR | ❌ | ❌ (Color 계열 전체) | (매뉴얼 p.19) | Code Reader 계열 |
| 입·출력 전환 핀 | 2개(07, 08) | 4개(05–08) | (매뉴얼 p.20, p.31) | — |
| 엔코더 입력 | ❌ | ✅ | (매뉴얼 p.20) | — |
| RS422 / RS232 | ❌ | ✅ | (매뉴얼 p.20, p.32) | Ethernet TCP/IP |
| I/O 확장 모듈 | ❌ | ✅ | (매뉴얼 p.20) | — |
| 자유 형상 ROI | Contour만 ⚠️ | ✅ | (매뉴얼 p.20) | — |

## 장비는 지원하지만 이 튜토리얼 규칙으로 제외한 기능

| 기능 | 이유 | 출처 |
|---|---|---|
| PROFINET (GSD, 모듈 1–5 텔레그램) | 사용자 규칙 9: PLC 통신 미구현 | (매뉴얼 p.20, p.331–363) |
| EtherNet/IP (Assembly, EDS) | 사용자 규칙 9: PLC 통신 미구현 | (매뉴얼 p.20, p.364–386) |

> [!TIP]
> 오프라인 학습: Device Manager의 `시뮬레이션 모드의 센서` 목록에 **Color / R3C / Advanced / 1.23.2.2** 항목이 있다(스크린샷 dm_main). 장비 없이 Advanced 검출기 화면을 구경할 수는 있지만, **이 장비에 내려받을 수는 없다.** 포트폴리오에는 "Standard 장비로 구현"과 "시뮬레이션 구경"을 섞어 쓰지 않는다.
