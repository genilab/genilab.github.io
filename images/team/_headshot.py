"""
Headshot Normalizer

Scans the current folder for files matching task["patterns"] 
It resizes them to a height of 200 pixels (maintaining aspect ratio), converts them 
to black & white, applies contrast enhancement, and overwrites the original file.

Disclaimer:
This script was 'vibe coded', a lightweight approach to quickly solving a specific need. 
The result has been revised and approved by a human.
"""

from PIL import Image, ImageEnhance
import glob
import os

BASE_DIR = "."

def convert_to_jpg(base_dir):
    print("🔁 Converting non-JPG images to JPG (max quality)...")

    image_files = glob.glob(os.path.join(base_dir, "*"))
    for path in image_files:
        if not os.path.isfile(path):
            continue

        _, ext = os.path.splitext(path)
        if ext.lower() == ".jpg":
            continue  # Already JPG, skip

        try:
            with Image.open(path) as img:
                base_name = os.path.splitext(os.path.basename(path))[0]
                jpg_path = os.path.join(base_dir, f"{base_name}.jpg")

                img = img.convert("RGB")  # Ensure compatibility
                img.save(jpg_path, format="JPEG", quality=100)
                print(f"🟢 Converted: {os.path.basename(path)} → {os.path.basename(jpg_path)}")

        except Exception as e:
            print(f"❌ Conversion failed for {path} — {e}")

def normalize_jpgs(base_dir, size, bw, contrast):
    print("🎨 Normalizing JPG images...")

    jpg_files = glob.glob(os.path.join(base_dir, "*.jpg"))

    if not jpg_files:
        print("❌ No JPG files found for processing.")
        return

    for img_path in jpg_files:
        try:
            with Image.open(img_path) as img:
                orig_width, orig_height = img.size
                target_width, target_height = size

                # Calculate missing dimension to preserve aspect ratio
                if target_width is None:
                    aspect_ratio = orig_width / orig_height
                    target_width = int(target_height * aspect_ratio)
                elif target_height is None:
                    aspect_ratio = orig_height / orig_width
                    target_height = int(target_width * aspect_ratio)

                if (orig_width, orig_height) == (target_width, target_height):
                    print(f"⏩ Skipped (already size): {os.path.basename(img_path)}")
                    continue

                resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                print(f"✅ Resized: {os.path.basename(img_path)} → {target_width}x{target_height}")

                if bw:
                    bw_img = resized_img.convert('L')
                    enhancer = ImageEnhance.Contrast(bw_img)
                    bw_img = enhancer.enhance(contrast)
                    bw_img = bw_img.convert('RGB')
                else:
                    bw_img = resized_img

                bw_img.save(img_path, format="JPEG", quality=100)
                print(f"🖤 Normalized & overwritten: {os.path.basename(img_path)}")

        except Exception as e:
            print(f"❌ Failed to process {img_path} — {e}")

def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), BASE_DIR))
    print(f"✨ Running at: {base_dir}")

    task = {
        "size": (None, 200),     # Resize to height 200px, preserve aspect ratio
        "bw": True,              # Grayscale?
        "contrast": 1.4          # Contrast enhancement
    }

    convert_to_jpg(base_dir)
    normalize_jpgs(base_dir, task["size"], task["bw"], task["contrast"])

if __name__ == "__main__":
    main()