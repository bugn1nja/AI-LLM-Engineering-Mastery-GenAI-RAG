from tkinter import Image

from PIL import image, ImageDraw, ImageFont
import os

def add_text_watermark_to_folder(
    inout_dir, output_dir, watermark_text, font_size, position
) :
    # Create output_dir if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    for filename in os.listdir(inout_dir):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(inout_dir, filename)
            original = Image.open(image_path)
            