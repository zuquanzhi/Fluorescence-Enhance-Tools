import cv2
import os
from src.processors.utils import create_black_mask, process_mask, adjust_image, blend_images

class ImageProcessor:
    def __init__(self, alpha=1.6, beta=25):
        self.alpha = alpha
        self.beta = beta

    def process_image(self, image_path, output_path):
        """处理单张图片"""
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"无法读取图片: {image_path}")

        final_image = self.process_frame(image)
        cv2.imwrite(output_path, final_image)

    def process_directory(self, input_dir, output_dir):
        """处理整个目录的图片"""
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for filename in os.listdir(input_dir):
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tiff')):
                input_path = os.path.join(input_dir, filename)
                output_path = os.path.join(output_dir, filename)
                self.process_image(input_path, output_path)

    def process_frame(self, frame):
        """处理图像帧"""
        mask = create_black_mask(frame)
        mask_blur = process_mask(mask)
        non_black_mask = 1.0 - mask_blur
        
        adjusted_frame = adjust_image(frame, self.alpha, self.beta)
        return blend_images(adjusted_frame, frame, non_black_mask, mask_blur)