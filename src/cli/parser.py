import argparse
import yaml
from pathlib import Path

def load_config(config_path='config/default_config.yaml'):
    """加载配置文件"""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)
    except Exception as e:
        raise ValueError(f"无法加载配置文件: {str(e)}")

def create_parser():
    """创建命令行参数解析器"""
    parser = argparse.ArgumentParser(description='荧光增强处理工具')
    parser.add_argument('--mode', choices=['video', 'image'], required=True,help='处理模式：video（视频）或 image（图片）')
    parser.add_argument('--input', required=True,help='输入文件或目录路径')
    parser.add_argument('--output', required=True,help='输出文件或目录路径')
    parser.add_argument('--config', default='config/default_config.yaml',help='配置文件路径')
    parser.add_argument('--alpha', type=float,help='对比度参数（覆盖配置文件）')
    parser.add_argument('--beta', type=float,help='亮度参数（覆盖配置文件）')
    parser.add_argument('--show', action='store_true',help='是否显示处理过程')
    return parser