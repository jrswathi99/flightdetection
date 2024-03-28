from ultralytics import YOLO

webcam_i = 0
model = YOLO('best_yolo8.pt')

results = model(source = webcam_i, show= True, conf=0.3 , save=True)