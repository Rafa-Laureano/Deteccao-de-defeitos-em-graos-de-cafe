from ultralytics import YOLO

# Load the YOLO11 model
model = YOLO("yolo_12n/yolo_12n/weights/best.pt")
# Export the model to TFLite format
model.export(format="tflite", data="beans_mosaic.v11-nova-versao.yolov11/data.yaml")

#model.export(format="onnx")