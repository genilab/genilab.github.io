"""
LOGO Normalizer

Scans the current folder for PNG files and resizes each to a width of 100 pixels
(maintaining aspect ratio). Colors are preserved; no grayscale or contrast changes.
Only .png files are processed; .jpg/.jpeg (and others) are ignored.

Disclaimer:
This script was 'vibe coded', a lightweight approach to quickly solving a specific need.
The result has been revised and approved by a human.
"""

from PIL import Image
import glob
import os

BASE_DIR = "."

def normalize_pngs(base_dir, target_width=100, patterns=("*.png",)):
    print(f"🎯 Target width: {target_width}px")
    print("🔎 Scanning for PNG files...")

    # Collect files from patterns
    files = []
    for pattern in patterns:
        files.extend(glob.glob(os.path.join(base_dir, pattern)))

    # Filter to .png extension only (ignore jpg/jpeg/etc)
    png_files = [p for p in files if os.path.splitext(p)[1].lower() == ".png"]

    if not png_files:
        print("❌ No PNG files found for processing.")
        return

    for img_path in sorted(png_files):
        try:
            with Image.open(img_path) as img:
                orig_w, orig_h = img.size

                # Skip if already at target width
                if orig_w == target_width:
                    print(f"⏩ Skipped (already {target_width}px wide): {os.path.basename(img_path)}")
                    continue

                # Compute target height to preserve aspect ratio
                scale = target_width / float(orig_w)
                target_height = max(1, int(round(orig_h * scale)))

                # Convert palette images to RGBA/RGB for better resize quality (colors preserved)
                if img.mode == "P":
                    img = img.convert("RGBA")

                # Keep alpha if present
                if img.mode not in ("RGB", "RGBA"):
                    # Convert uncommon modes while preserving alpha if available
                    img = img.convert("RGBA" if "A" in img.getbands() else "RGB")

                resized = img.resize((target_width, target_height), Image.Resampling.LANCZOS)

                # Save back as PNG, overwriting original
                # optimize=True can reduce file size without changing colors
                resized.save(img_path, format="PNG", optimize=True)
                print(f"✅ Resized: {os.path.basename(img_path)} → {target_width}x{target_height}")

        except Exception as e:
            print(f"❌ Failed to process {img_path} — {e}")

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), BASE_DIR))
    print(f"✨ Running at: {base_dir}")

    task = {
        "patterns": ("*.png",),  # process only PNGs
        "target_width": 100      # resize width to 100px, preserve aspect ratio
    }

    normalize_pngs(base_dir, target_width=task["target_width"], patterns=task["patterns"])

if __name__ == "__main__":
    main()
