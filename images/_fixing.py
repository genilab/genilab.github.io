from PIL import Image, ImageEnhance
import glob
import os

def main():
    # Get the directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Promo message
    print(f"✨ Running at #{base_dir}")

    # Define resize tasks
    resize_tasks = [
        {"pattern": "use-*.png", "size": (150, 150)},
        {"pattern": "*-icon.png", "size": (200, 200)},
        {"pattern": "*-headshot.png", "size": (None, 200)}, 
        {"pattern": "*-info.png", "size": (None, 700)}, 
    ]

    # Process each resize task
    for task in resize_tasks:
        pattern_path = os.path.join(base_dir, '**', task["pattern"])
        image_files = glob.glob(pattern_path, recursive=True)

        for img_path in image_files:
            try:
                with Image.open(img_path) as img:
                    orig_width, orig_height = img.size
                    target_width, target_height = task["size"]

                    # Calculate missing dimension if None
                    if target_width is None and target_height is not None:
                        aspect_ratio = orig_width / orig_height
                        target_width = int(target_height * aspect_ratio)
                    elif target_height is None and target_width is not None:
                        aspect_ratio = orig_height / orig_width
                        target_height = int(target_width * aspect_ratio)

                    resized_img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                    resized_img.save(img_path)
                    print(f"✅ Resized:  {os.path.basename(img_path)} → {task['size']}")
            except Exception as e:
                print(f"❌ Failed: {img_path} — {e}")

    # Create high-contrast black and white versions of headshots
    bw_pattern_path = os.path.join(base_dir, '**', '*-headshot.png')
    bw_files = glob.glob(bw_pattern_path, recursive=True)

    for img_path in bw_files:
        try:
            with Image.open(img_path) as img:
                bw_img = img.convert('L')  # Convert to grayscale

                # Enhance contrast
                enhancer = ImageEnhance.Contrast(bw_img)
                bw_img = enhancer.enhance(1.5)  # Increase contrast (adjust factor if needed)

                bw_img = bw_img.convert('RGB')  # Convert back to RGB to save as PNG

                base, ext = os.path.splitext(img_path)
                bw_path = base + '-bw' + ext
                bw_img.save(bw_path)
                print(f"✅ B&W Created: {os.path.basename(bw_path)}")
        except Exception as e:
            print(f"❌ BW Conversion Failed: {img_path} — {e}")

if __name__ == "__main__":
    main()