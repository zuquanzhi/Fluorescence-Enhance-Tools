from src.cli.parser import create_parser, load_config
from src.processors.video_processor import VideoProcessor
from src.processors.image_processor import ImageProcessor
import logging
import sys
from pathlib import Path

def setup_logging():
    """配置日志系统"""
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    logging.basicConfig(
        level=logging.INFO,
        format=log_format,
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('fluorescent_charge.log')
        ]
    )
    return logging.getLogger(__name__)

def main():
    logger = setup_logging()
    parser = create_parser()
    args = parser.parse_args()
    
    try:
        config = load_config(args.config)
        mode_config = config[args.mode]

        # 验证路径
        input_path = Path(args.input)
        output_path = Path(args.output)
        
        if not input_path.exists():
            raise FileNotFoundError(f"输入路径不存在: {input_path}")

        # 命令行参数覆盖配置文件
        alpha = args.alpha if args.alpha is not None else mode_config['alpha']
        beta = args.beta if args.beta is not None else mode_config['beta']

        if args.mode == 'video':
            processor = VideoProcessor(alpha=alpha, beta=beta)
            logger.info(f"开始处理视频: {input_path}")
            processor.process_video(str(input_path), str(output_path))
            logger.info(f"视频处理完成，已保存至: {output_path}")
        else:
            processor = ImageProcessor(alpha=alpha, beta=beta)
            logger.info(f"开始处理图片目录: {input_path}")
            processor.process_directory(str(input_path), str(output_path))
            logger.info(f"图片处理完成，已保存至: {output_path}")

    except Exception as e:
        logger.error(f"处理过程中出现错误: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()