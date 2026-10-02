# 📖 Help 번역 색인 v2 (Vision Sensor Configuration Studio – Color)

사용자 규칙 9: Configuration Studio **Help 탭의 영문은 반드시 번역**하고, 각 Setup 단계 레슨에 해당 번역을 넣는다.
v2: 모든 번역 완료. 번역문은 각 레슨의 **`📖 Help 번역`** 접기 블록에 있다.

- 원본: `SBS_ContextHelp_en_V1_22_14.chm` (설치 폴더 `Help/en/1.22.14.1/`, Configuration Studio 1.23.2.2가 실제로 여는 파일)
- 번역 원칙: 문장 단위 번역. 이 품번(Color Standard)에 해당하지 않는 문장에는 `※ 이 품번 해당 없음`. 메뉴·버튼명은 영문 그대로. 그림 캡션은 생략.
- 용도: 연구·학습용(사용자 결정, [상충 A-09](../reports/conflict-report_v2.md#a-09)). 출처: Festo 다운로드·문서 안내 <https://www.festo.com/sp> (8058732 검색)

| Setup 단계 / 화면 | Help 토픽 (원문 제목) | 원본 파일 | 번역 위치 |
|---|---|---|---|
| 개요 | SBS Operating- and configuration software - Overview | overview.htm | [M00](../00_device-map.md) |
| 개요 | Vision Sensor Device Manager / Configuration Studio / Visualisation Studio | sf.htm, sc.htm, sv.htm | [M00](../00_device-map.md) |
| 개요 | Context help | help.htm | [M00](../00_device-map.md) |
| Device Manager | Active sensors / Sensors for simulation mode / Find / Add / Configuring / Display images / Network settings | sfsensor, sfsimulation, sfaddfind, sfconfig, sfview, sfset | [M01](../01_connection-first-image.md) |
| Configuration Studio | Connection mode / Trigger settings / Displays in image window / Controlling image reproduction | scconnection, sctrigger, scview, scfilmstripnavigation | [M01](../01_connection-first-image.md) |
| Setup **Job** | Setup Jobs / Creation of jobs / Tab Image acquisition / Tab White balance / Tab Pre-processing | scjob, scjobedit, scjobgeneral, scjobwhitebalance, scjobpreprocessing | [M02](../02_image-quality.md) |
| 도구 | Creating filmstrips / Simulation of jobs (offline mode) | scfilmstripedit, scfilmstrip | [M02](../02_image-quality.md) |
| 공통 | Search and parameter zones | scroi | [M03](../03_alignment-contour.md) |
| Setup **Alignment** | Setup Alignment / Selection and configuration / Contour detection / Tab Color channel / Parameters / Optimization, contour / Speed / Result offset | scalignment, scalignmentedit, scalignmentcontour, sccolorselectiongrey, scalignmentcontourparameters, scalignmentcontouroptimization, scalignmentcontourspeed, screspose | [M03](../03_alignment-contour.md) |
| Setup **Detector** | Setup Detectors / Creating and adjusting / Selecting a suitable detector / Function: Mask | scdetector, scdetectoredit, scdetectormethod, sceditroi | [M04](../04_inspection-detectors.md) |
| Setup **Detector** | Detector Contrast / Contrast application | scdetectorcontrast, scdetectorcontrastappl | [M04-1](../04_inspection-detectors.md#04-1-있나없나--contrast) |
| Setup **Detector** | Detector Color area / Tab Color channel / Color area / Color histogram / Thresholds | scdetectorcolorareabase, sccolorselection, scdetectorcolorarea, scdetectorcolorhistogram, scdetectorcolorareabasictab | [M04-2](../04_inspection-detectors.md#04-2-색이-맞나--color-area) |
| 공통 | Color models RGB / HSV / LAB | sccolormodels, sccolormodelrgb, sccolormodelhsv, sccolormodellab | [M04-2](../04_inspection-detectors.md#04-2-색이-맞나--color-area) |
| Setup **Result** / **Start sensor** | Setup Result / Setup Start sensor | scresult, scstart | [M05](../05_judgement-and-output.md) |
| Setup **Output** | Setup Output / Tab Output signals / Standard mode / Formula mode / Tab Timing | scoutput, scoutputlogic, scoutputlogicstandard, scoutputlogicadvanced, scoutputtiming | [M05](../05_judgement-and-output.md) |
| Setup **Job** | Tab Cycle time | scjobtimeout | [M05](../05_judgement-and-output.md) |
| Setup **Output** | Tab I/O mapping / Tab Interfaces | scoutputiosettings, scoutputsettings | [M06](../06_output-24v.md) |
| File | Load and save jobs / Protect job set | scjobset, scprotectjobset | [M07](../07_operation-maintenance.md) |
| Setup **Output** | Tab Image transmission / Tab Archiving / Tab Telegram (CSV 내용) | scjobtransmit, scjobarchive, scoutputtelegram | [M07](../07_operation-maintenance.md) |
| 도구 | Image recorder | scimagerec | [M07](../07_operation-maintenance.md) |
| Visualisation Studio | All functions / Image display / Freeze / Zoom / Archiving / Tab Result / Statistics / Job select / Job upload | svgettingstarted, svimage, svfreeze, svzoom, svarchiving, svresults, svstatistics, svjob, svupload | [M07](../07_operation-maintenance.md) |
| Output › Interfaces | SBS – SBSxWebViewer | svwebviewbase | [M07](../07_operation-maintenance.md) |
| Device Manager | Favorites / User administration / Update / Auto Start Up | sffavorite, sfuseradmin, sfupdate, sfautostart | [M07](../07_operation-maintenance.md) |

**번역 제외(이 품번 미지원)**: Calibration 전체, Pattern matching·Edge 정렬, Pattern/Contour/Gray/Brightness/BLOB/Caliper/Barcode/Datacode/OCR/Color value/Color list 검출기, PROFINET·EtherNet/IP·RS422 텔레그램 부록(anh_*).
