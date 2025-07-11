"""
Image Headshot Processor
v0.1

Scans the current folder for files matching *-headshot.png or *-headshot.jpg.
It resizes them to a height of 200 pixels (maintaining aspect ratio), converts them 
to black & white, applies contrast enhancement, and overwrites the original file.

Disclaimer:
This script was 'vibe coded', a lightweight approach to quickly solving a specific need. 
The result has been revised and approved by a human.
"""

from PIL import Image, ImageEnhance
import glob
import os

BASE_DIR = "../images/people"
   
def main():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), BASE_DIR))
    print(f"✨ Running at: {base_dir}")

    task = {
        "patterns": ["*-headshot.png", "*-headshot.jpg"],
        "size": (None, 200),
        "bw": True,
        "contrast": 1.4
    }

    image_files = []
    for pattern in task["patterns"]:
        pattern_path = os.path.join(base_dir, pattern)  # no ** — current folder only
        image_files.extend(glob.glob(pattern_path))

    for img_path in image_files:
        try:
            with Image.open(img_path) as img:
                orig_width, orig_height = img.size
                target_width, target_height = task["size"]

                # Calculate missing dimension to preserve aspect ratio
                if target_width is None:
                    aspect_ratio = orig_width / orig_height
                    target_width = int(target_height * aspect_ratio)
                elif target_height is None:
                    aspect_ratio = orig_height / orig_width
                    target_height = int(target_width * aspect_ratio)

                # Skip if already at target size
                if (orig_width, orig_height) == (target_width, target_height):
                    print(f"⏩ Skipped (already size): {os.path.basename(img_path)}")
                    continue

                # Resize
                resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                print(f"✅ Resized: {os.path.basename(img_path)} → {target_width}x{target_height}")

                # B&W + Contrast
                if task.get("bw", False):
                    contrast_value = task.get("contrast", 1.0)
                    bw_img = resized_img.convert('L')
                    enhancer = ImageEnhance.Contrast(bw_img)
                    bw_img = enhancer.enhance(contrast_value)
                    bw_img = bw_img.convert('RGB')

                    bw_img.save(img_path)
                    print(f"🖤 Overwritten with B&W: {os.path.basename(img_path)} (contrast: {contrast_value})")

        except Exception as e:
            print(f"❌ Failed: {img_path} — {e}")

if __name__ == "__main__":
    main()
