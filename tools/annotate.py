"""스크린샷에 번호 박스를 그려 '메뉴 위치'를 표시하는 도구.

사용법:
    python tools/annotate.py tools/annotations.json

annotations.json 형식:
[
  {
    "src": "images/raw/cs_job_image-acquisition.png",
    "out": "images/annotated/cs_layout.png",
    "boxes": [
      {"n": 1, "xy": [0, 33, 190, 50]},
      {"n": 2, "xy": [0, 52, 420, 88], "color": "#0070c0"}
    ]
  }
]

- xy = [왼쪽, 위, 오른쪽, 아래] (픽셀). 그림판 등에서 마우스 좌표를 보고 적으면 된다.
- 번호의 의미(범례)는 이미지가 아니라 마크다운 표에 적는다. (한글 폰트 문제 회피 + 검색 가능)
- 원본(images/raw)은 수정하지 않고 항상 새 파일(images/annotated)로 저장한다.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

DEFAULT_COLOR = "#e00000"


def load_font(size: int):
    for name in ("arialbd.ttf", "DejaVuSans-Bold.ttf", "Arial Bold.ttf"):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default()


def badge(draw, x, y, text, color, font, r=13):
    draw.ellipse([x - r, y - r, x + r, y + r], fill=color, outline="white", width=2)
    l, t, rgt, b = draw.textbbox((0, 0), text, font=font)
    draw.text((x - (rgt - l) / 2, y - (b - t) / 2 - t), text, fill="white", font=font)


def annotate(item, root: Path):
    img = Image.open(root / item["src"]).convert("RGB")
    draw = ImageDraw.Draw(img)
    font = load_font(15)
    for box in item["boxes"]:
        color = box.get("color", DEFAULT_COLOR)
        x1, y1, x2, y2 = box["xy"]
        draw.rectangle([x1, y1, x2, y2], outline=color, width=3)
        # 번호 배지는 박스 왼쪽 위 모서리에 둔다(화면 밖으로 나가지 않게 보정)
        bx = min(max(x1 + 2, 14), img.width - 14)
        by = min(max(y1 + 2, 14), img.height - 14)
        badge(draw, bx, by, str(box["n"]), color, font)
    out = root / item["out"]
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    print("saved", out)


def main():
    spec = Path(sys.argv[1] if len(sys.argv) > 1 else "tools/annotations.json")
    root = spec.resolve().parent.parent
    for item in json.loads(spec.read_text(encoding="utf-8")):
        annotate(item, root)


if __name__ == "__main__":
    main()
