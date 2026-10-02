"""스크린샷 번호 박스 도구 v2 — annotate.py에 '좌표 배율(scale)'과 '잘라내기(crop)'를 더했다.

사용법:
    python tools/annotate_v2.py tools/annotations_v2.json

항목 형식:
{
  "src": "images/raw/cs_ko_main.png",
  "out": "images/annotated/cs_ko_00_layout.png",
  "scale": 1.828571,            # 선택: boxes/crop 좌표에 곱할 배율 (축소본에서 좌표를 잰 경우)
  "crop": [0, 0, 1300, 1392],   # 선택: 주석을 그린 뒤 이 영역만 저장 (scale 적용 후 원본 좌표)
  "boxes": [{"n": 1, "xy": [4, 12, 95, 23]}]
}
- 원본(images/raw)은 수정하지 않는다. 결과는 항상 새 파일(images/annotated)로 저장한다.
- 번호의 의미(범례)는 마크다운 표에 적는다.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

DEFAULT_COLOR = "#e00000"


def load_font(size):
    for name in ("arialbd.ttf", "DejaVuSans-Bold.ttf", "Arial Bold.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def badge(draw, x, y, text, color, font, r):
    draw.ellipse([x - r, y - r, x + r, y + r], fill=color, outline="white", width=2)
    l, t, rr, b = draw.textbbox((0, 0), text, font=font)
    draw.text((x - (rr - l) / 2, y - (b - t) / 2 - t), text, fill="white", font=font)


def annotate(item, root):
    img = Image.open(root / item["src"]).convert("RGB")
    k = float(item.get("scale", 1.0))
    big = img.width > 1600
    width, r, fsize = (5, 20, 24) if big else (3, 13, 15)
    draw = ImageDraw.Draw(img)
    font = load_font(fsize)
    for box in item["boxes"]:
        color = box.get("color", DEFAULT_COLOR)
        x1, y1, x2, y2 = [v * k for v in box["xy"]]
        draw.rectangle([x1, y1, x2, y2], outline=color, width=width)
        bx = min(max(x1 + 2, r + 1), img.width - r - 1)
        by = min(max(y1 + 2, r + 1), img.height - r - 1)
        badge(draw, bx, by, str(box["n"]), color, font, r)
    if "crop" in item:
        img = img.crop(tuple(int(v * k) for v in item["crop"]))
    out = root / item["out"]
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    print("saved", out)


def main():
    spec = Path(sys.argv[1] if len(sys.argv) > 1 else "tools/annotations_v2.json")
    root = spec.resolve().parent.parent
    for item in json.loads(spec.read_text(encoding="utf-8")):
        annotate(item, root)


if __name__ == "__main__":
    main()
