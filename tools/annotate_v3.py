"""스크린샷 번호 박스 도구 v3 — v2와 같은 JSON 형식을 쓰되,
- 선 굵기·번호 크기를 '잘라낸 뒤 크기' 기준으로 정하고
- 번호 원을 박스 **바깥 왼쪽**(자리가 없으면 위쪽)에 그려 글자를 가리지 않는다.
상자별로 "badge": "left" | "top" | "right" | "inside" 지정 가능.

사용법:  python tools/annotate_v3.py tools/annotations_v3.json
원본(images/raw)은 수정하지 않는다. 결과는 images/annotated 새 파일.
"""
import json
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

COLOR = "#e00000"


def font(size):
    for n in ("arialbd.ttf", "DejaVuSans-Bold.ttf"):
        try:
            return ImageFont.truetype(n, size)
        except OSError:
            pass
    return ImageFont.load_default()


def annotate(item, root):
    img = Image.open(root / item["src"]).convert("RGB")
    k = float(item.get("scale", 1.0))
    crop = [int(v * k) for v in item.get("crop", [0, 0, img.width, img.height])]
    img = img.crop(tuple(crop))
    ox, oy = crop[0], crop[1]
    big = img.width > 1600
    w, r, fs = (4, 15, 18) if big else (3, 11, 14)
    d = ImageDraw.Draw(img)
    f = font(fs)
    for b in item["boxes"]:
        x1, y1, x2, y2 = [v * k for v in b["xy"]]
        x1, x2, y1, y2 = x1 - ox, x2 - ox, y1 - oy, y2 - oy
        c = b.get("color", COLOR)
        d.rectangle([x1, y1, x2, y2], outline=c, width=w)
        pos = b.get("badge", "left")
        if pos == "left" and x1 - 2 * r - 4 < 0:
            pos = "right" if x2 + 2 * r + 4 < img.width else "inside"
        if pos == "left":
            cx, cy = x1 - r - 3, y1 + r
        elif pos == "right":
            cx, cy = x2 + r + 3, y1 + r
        elif pos == "top":
            cx, cy = x1 + r, y1 - r - 3
        else:
            cx, cy = x1 + r + 3, y1 + r + 3
        cx = min(max(cx, r + 1), img.width - r - 1)
        cy = min(max(cy, r + 1), img.height - r - 1)
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=c, outline="white", width=2)
        t = str(b["n"])
        l, tt, rr, bb = d.textbbox((0, 0), t, font=f)
        d.text((cx - (rr - l) / 2, cy - (bb - tt) / 2 - tt), t, fill="white", font=f)
    out = root / item["out"]
    out.parent.mkdir(parents=True, exist_ok=True)
    img.save(out)
    print("saved", out)


def main():
    spec = Path(sys.argv[1] if len(sys.argv) > 1 else "tools/annotations_v3.json")
    root = spec.resolve().parent.parent
    for it in json.loads(spec.read_text(encoding="utf-8")):
        annotate(it, root)


if __name__ == "__main__":
    main()
