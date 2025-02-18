import cv2
import numpy as np
from typing import Tuple, Union

def create_black_mask(frame: np.ndarray, lower_threshold: int = 0, upper_threshold: int = 50) -> np.ndarray:
    """创建黑色区域掩码"""
    lower_black = np.array([lower_threshold] * 3, dtype=np.uint8)
    upper_black = np.array([upper_threshold] * 3, dtype=np.uint8)
    return cv2.inRange(frame, lower_black, upper_black)

def process_mask(mask: np.ndarray, 
                kernel_size: Tuple[int, int] = (21, 21)) -> np.ndarray:
    """处理掩码使边缘平滑"""
    mask_blur = cv2.GaussianBlur(mask, kernel_size, 0)
    return mask_blur.astype(np.float32) / 255.0

def adjust_image(image: np.ndarray, 
                alpha: float = 1.6, 
                beta: float = 25) -> np.ndarray:
    """调整图像的对比度和亮度"""
    return cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

def blend_images(adjusted_image: np.ndarray, 
                original_image: np.ndarray,
                non_black_mask: np.ndarray, 
                black_mask: np.ndarray) -> np.ndarray:

    """融合调整后的图像和原始图像"""
    return (adjusted_image * non_black_mask[..., np.newaxis] + 
            original_image * black_mask[..., np.newaxis]).astype(np.uint8)