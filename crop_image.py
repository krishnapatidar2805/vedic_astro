import os
from PIL import Image

def crop_watermark(image_path, crop_bottom_percent=0.065):
    if not os.path.exists(image_path):
        print(f"File not found: {image_path}")
        return
    
    with Image.open(image_path) as img:
        width, height = img.size
        # Crop out the bottom percentage where FaceApp watermark is located
        crop_height = int(height * (1.0 - crop_bottom_percent))
        cropped = img.crop((0, 0, width, crop_height))
        
        # Save back to same path
        cropped.save(image_path, quality=95)
        print(f"Cropped {image_path}: Original {width}x{height} -> New {width}x{crop_height}")

if __name__ == '__main__':
    paths = [
        os.path.join(os.path.dirname(__file__), 'static', 'img', 'astrologer.jpeg'),
        os.path.join(os.path.dirname(__file__), 'media', 'astrologer', 'gajendra_sharma.jpeg'),
    ]
    for p in paths:
        crop_watermark(p)
