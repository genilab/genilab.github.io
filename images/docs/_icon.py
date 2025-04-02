from PIL import Image
import glob
import os

def main():
    # Get the directory where this script is located
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Promo message
    print(f"🚀 Running at #{base_dir}")

    # Define resize tasks
    resize_tasks = [
        {"pattern": "use-*.png", "size": (150, 150)},
        {"pattern": "*-icon.png", "size": (200, 200)},
    ]

    # Process each task
    for task in resize_tasks:
        pattern_path = os.path.join(base_dir, task["pattern"])
        image_files = glob.glob(pattern_path)

        for img_path in image_files:
            try:
                with Image.open(img_path) as img:
                    resized_img = img.resize(task["size"], Image.Resampling.LANCZOS)
                    resized_img.save(img_path)
                    print(f"✅ Resized: {os.path.basename(img_path)} → {task['size']}")
            except Exception as e:
                print(f"❌ Failed: {os.path.basename(img_path)} — {e}")

if __name__ == "__main__":
    main()
        

