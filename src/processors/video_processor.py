import cv2
from src.processors.utils import create_black_mask, process_mask, adjust_image, blend_images

class VideoProcessor:
    def __init__(self, alpha=1.6, beta=25):
        self.alpha = alpha
        self.beta = beta

    def create_writer(self, output_path, cap):
        """创建视频写入器"""
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        return cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    def process_video(self, input_path, output_path):
        """处理视频"""
        cap = cv2.VideoCapture(input_path)
        if not cap.isOpened():
            raise ValueError("无法打开视频文件")

        out = self.create_writer(output_path, cap)

        try:
            while True:
                ret, frame = cap.read() # 读取视频帧
                if not ret:
                    break

                final_frame = self.process_frame(frame)
                out.write(final_frame)

                cv2.imshow('Processed Frame', final_frame)  # 图像显示开关
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break

        finally:
            cap.release()
            out.release()
            cv2.destroyAllWindows()

    def process_frame(self, frame):
        """处理单帧"""
        mask = create_black_mask(frame)
        mask_blur = process_mask(mask)
        non_black_mask = 1.0 - mask_blur
        
        adjusted_frame = adjust_image(frame, self.alpha, self.beta)
        return blend_images(adjusted_frame, frame, non_black_mask, mask_blur)