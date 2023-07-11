from ultralytics import YOLO
 
# 加载模型
model = YOLO("Z:\homework\DXQ\github\Yolov8-seg\yolov8n-seg.pt")
 
# 转换模型
model.export(format="onnx")