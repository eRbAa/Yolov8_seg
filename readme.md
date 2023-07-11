## Yolov8-seg实例分割模型

### 模型介绍

YOLOv8 是来自 Ultralytics 的最新的基于 YOLO 的对象检测模型系列，提供最先进的性能。

### 模型结构

特征提取部分采用了一种名为CSPDarknet的网络结构，它是一种基于Darknet的改进版本。CSPDarknet采用了Cross Stage Partial Network（CSP）结构，将网络分为两个部分，每个部分都包含多个残差块。这种结构可以有效地减少模型的参数量和计算量，同时提高特征提取的效率。

目标检测部分采用了一种名为YOLOv4-Head的检测头结构。该结构包含了多个卷积层和池化层，用于对特征图进行处理和压缩。然后，通过多个卷积层和全连接层，将特征图转换为目标检测结果。YOLOv8采用了一种基于Anchor-Free的检测方式，即直接预测目标的中心点和宽高比例，而不是预测Anchor框的位置和大小。这种方式可以减少Anchor框的数量，提高检测速度和精度。

### 预训练模型

 在根目录下提供了一个预训练模型以及对应的onnx模型

 fall_detect.pt  —— `#基于pytorch框架训练出的yolo预训练模型 `

 fall_detect.onnx —— `#由fall_detect.pt转换的onnx模型 `

### 测试

以下命令使用YOLOv8n-seg模型对视频运行实例分割。

`yolo task=detect mode=predict model=yolov8n-seg.pt source='pingpong.mp4' show=True`

|      名称      |         默认值         |                      描述                      |
| :------------: | :--------------------: | :---------------------------------------------: |
|     source     | ‘ultralytics/assets’ |               图片或视频的源目录               |
|      save      |         False         |                  是否保存结果                  |
|      show      |         False         |                  是否显示结果                  |
|    save_txt    |         False         |             将结果保存为 .txt 文件             |
|   save_conf   |         False         |            保存带有置信度分数的结果            |
|   save_crop   |         Fasle         |             保存裁剪后的图像和结果             |
|      conf      |          0.3          |                   置信度阈值                   |
|  hide_labels  |         False         |                    隐藏标签                    |
|   hide_conf   |         False         |                 隐藏置信度分数                 |
|   vid_stride   |         False         |                  视频帧率步幅                  |
| line_thickness |           3           |               边界框厚度（像素）               |
|   visualize   |         False         |                 可视化模型特征                 |
|    augment    |         False         |             将图像增强应用于预测源             |
|  agnostic_nms  |         False         |                类别不可知的 NMS                |
|  retina_masks  |         False         |              使用高分辨率分割蒙版              |
|    classes    |          null          | 只显示某几类结果，如class=0, 或者 class=[0,2,3] |

### 源码仓库及问题反馈

https://github.com/eRbAa/Yolov8_seg

### 参考

https://blog.csdn.net/stq054188/article/details/128925932
