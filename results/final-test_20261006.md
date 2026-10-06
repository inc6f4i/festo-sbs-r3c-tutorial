# 최종 시험 — LED 2개 3단 판별 (2026-10-06 10:2x–10:46, 현장)

- 구성: Job1 수정(백업 `backups/jobset_20261006_before-seat-gloss.job`), 검사기 1 = 10–24(Matte), 검사기 2 = 24–100(Basic), 검사기 3 삭제
- 출력: 12 RDBU(A) = `!D2` → LED A, 07 BK(B) = `!D1` → LED B, 작업검사결과 = `D1|D2`
- 운전: 검사시작(Run), 사이클 타임 44 ms, 셔터 0.70 ms
- 결선(PNP): 출력선 → 24 V LED(+), LED(−) → 0 V

| 상태 | 기대 | 사용자 확인 결과 | 판정 |
|---|---|---|---|
| 지그 + Basic | 07(검정)만 24 V | 검정선 24 V | ✅ |
| 지그 + Matte | 12(빨강/파랑)만 24 V | 빨파선 24 V | ✅ |
| 빈 지그 | 12·07 둘 다 24 V | 빨파·검정선 둘 다 24 V | ✅ |

- 멀티미터: ON **23.0 V** (사진 `images/raw/photo_final_meter-23V.jpg`), OFF 측 0 표시(`photo_final_meter-off.jpg`)
- 처음 시도에서 지그가 약 20° 비틀려 놓여 빈 지그가 Matte로 오판(점수 14–21) → 똑바로 놓은 뒤 정상
- 결선 중 안전 사고 2건(SMPS AC 단자에 LED 연결, 통전 중 드라이버 단락) → [문제 해결 v2 — 안전](../docs/appendix/troubleshooting_v2.md)

남은 것: 각 상태 10회 반복 + 연속 시연 영상(CP6).
