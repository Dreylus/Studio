"""Resize the temporary app icon for both platforms (requires Pillow)."""
from pathlib import Path

from PIL import Image, ImageOps

ROOT = Path(__file__).resolve().parents[1]
source = Image.open(ROOT / "branding/app-icon.png").convert("RGB")
square = ImageOps.pad(source, (max(source.size),) * 2, color="white")

ios_sizes = {
    "AppIcon60x60@2x.png": 120,
    "AppIcon60x60@3x.png": 180,
    "AppIcon76x76~ipad.png": 76,
    "AppIcon76x76@2x~ipad.png": 152,
    "AppIcon83.5x83.5@2x~ipad.png": 167,
}
for name, size in ios_sizes.items():
    square.resize((size, size), Image.Resampling.LANCZOS).save(ROOT / "ios/icons" / name)

for density, scale in {"mdpi": 1, "hdpi": 1.5, "xhdpi": 2, "xxhdpi": 3, "xxxhdpi": 4}.items():
    folder = ROOT / f"android/res/mipmap-{density}"
    size = round(48 * scale)
    square.resize((size, size), Image.Resampling.LANCZOS).save(folder / "ic_launcher.png")
    # Keep the complete supplied image inside the adaptive icon's safe zone.
    size, content_size = round(108 * scale), round(66 * scale)
    foreground = Image.new("RGBA", (size, size))
    icon = square.resize((content_size, content_size), Image.Resampling.LANCZOS)
    inset = (size - content_size) // 2
    foreground.paste(icon, (inset, inset))
    foreground.save(folder / "ic_fg.png")
