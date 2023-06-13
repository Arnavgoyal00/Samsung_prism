from ultralytics import YOLO
from PIL import Image
import cv2
# Load a model
# model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("runs/detect/train2/weights/best.pt")  # load a pretrained model (recommended for training)

im2 = cv2.imread("data/images/Train/IMG_0071.PNG")
results = model.predict(source=im2, save=True, save_txt=True)

