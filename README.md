# 视频图像荧光增强处理工具

这是一个用于处理视频和图像的荧光增强工具，可以提升暗光环境下的图像质量。

## 功能特点

- 支持视频和图片处理
- 可调节对比度和亮度参数
- 支持批量处理图片
- 支持视频帧提取
- 提供进度显示和日志记录

## 安装依赖

```bash
pip install opencv-python
pip install pyyaml
```

## 使用方法

### 1. 视频/图像处理

```bash
python main.py --mode [video|image] --input <输入路径> --output <输出路径> [选项]
```

参数说明：
- `--mode`: 处理模式，可选 `video`（视频）或 `image`（图片）
- `--input`: 输入文件或目录路径
- `--output`: 输出文件或目录路径
- `--config`: 配置文件路径（可选，默认：config/default_config.yaml）
- `--alpha`: 对比度参数（可选，覆盖配置文件）
- `--beta`: 亮度参数（可选，覆盖配置文件）
- `--show`: 显示处理过程（可选）

示例：
```bash
# 处理视频
python main.py --mode video --input input.mp4 --output output.mp4

# 处理图片目录
python main.py --mode image --input ./input_images --output ./output_images
```

### 2. 视频帧提取

如果需要将视频拆分为连续帧图像，可以使用视频帧提取工具：

```bash
python video_to_images.py --video <视频文件路径> --output <输出目录>
```

参数说明：
- `--video`, `-v`: 输入视频文件路径
- `--output`, `-o`: 输出目录路径（默认：frames）

示例：
```bash
python video_to_images.py --video input.mp4 --output ./video_frames
```

## 配置文件

在 `config/default_config.yaml` 中可以设置默认的处理参数：

```yaml
video:
  alpha: 1.6  # 对比度参数
  beta: 25    # 亮度参数

image:
  alpha: 1.4  # 对比度参数
  beta: 20    # 亮度参数
```

## 注意事项

1. 确保输入文件或目录存在
2. 处理大型视频文件时，请确保有足够的磁盘空间
3. 建议先使用小样本测试参数效果
4. 处理过程中可以按 'q' 键退出

## 日志

程序运行日志将保存在 `fluorescent_charge.log` 文件中，包含处理过程的详细信息。

## 系统要求
```
- Python 3.6+
- OpenCV
- PyYAML
```

## 许可证

MIT License