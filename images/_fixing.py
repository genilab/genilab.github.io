from PIL import Image, ImageEnhance
import glob
import os

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    print(f"✨ Running at #{base_dir}")

    resize_tasks = [
        {"pattern": "use-*.png", "size": (150, 150)},
        {"pattern": "*-icon.png", "size": (200, 200)},
        {"pattern": "*-headshot.png", "size": (None, 200), "bw": True, "contrast": 1.4},
        {"pattern": "*-info.png", "size": (None, 700)},
    ]

    for task in resize_tasks:
        pattern_path = os.path.join(base_dir, '**', task["pattern"])
        image_files = glob.glob(pattern_path, recursive=True)

        for img_path in image_files:
            try:
                with Image.open(img_path) as img:
                    orig_width, orig_height = img.size
                    target_width, target_height = task["size"]

                    if target_width is None:
                        aspect_ratio = orig_width / orig_height
                        target_width = int(target_height * aspect_ratio)
                    elif target_height is None:
                        aspect_ratio = orig_height / orig_width
                        target_height = int(target_width * aspect_ratio)

                    # Skip resizing if already at target size
                    if (orig_width, orig_height) == (target_width, target_height):
                        print(f"⏩ Skipped (already size): {os.path.basename(img_path)}")
                        resized_img = img.copy()
                    else:
                        resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                        resized_img.save(img_path)
                        print(f"✅ Resized:  {os.path.basename(img_path)} → {target_width}x{target_height}")

                    # Optional B&W processing
                    if task.get("bw", False):
                        contrast_value = task.get("contrast", 1.0)
                        bw_img = resized_img.convert('L')
                        enhancer = ImageEnhance.Contrast(bw_img)
                        bw_img = enhancer.enhance(contrast_value)
                        bw_img = bw_img.convert('RGB')

                        base, ext = os.path.splitext(img_path)
                        bw_path = base + '-bw' + ext
                        bw_img.save(bw_path)
                        print(f"🖤 B&W Created: {os.path.basename(bw_path)} (contrast: {contrast_value})")

            except Exception as e:
                print(f"❌ Failed: {img_path} — {e}")

if __name__ == "__main__":
    main()