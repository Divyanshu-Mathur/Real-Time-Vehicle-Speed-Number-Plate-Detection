import cv2
import numpy as np
import torch
import easyocr
from ultralytics import YOLO
from utils.deepsort import DeepSort
from utils.speed import estimate_speed
from utils.vehicle import draw_box
from utils.ocr import read_plate


# loading the models
model = YOLO("yolo11n.pt")
conf = 0.4
plate_model = YOLO("D:\Data Science\Computer Vision\Project 5 - Car Speed\models\plate_model.pt")
plate_model_conf = 0.4 

# init tracker
tracker = DeepSort(max_age=50, n_init=3)

# video
video_path = r"D:\Data Science\Computer Vision\Project 5 - Car Speed\Video\test_1.mp4"
cap = cv2.VideoCapture(video_path)
fps    = int(cap.get(cv2.CAP_PROP_FPS))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
out = cv2.VideoWriter(r'D:\Data Science\Computer Vision\Project 5 - Car Speed\Output\test_1_out.mp4',
                      cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))


# ppm estimation
point1 = (638, 547)
point2 = (642, 407)
real_distance_m = 10
meter_per_pixel = real_distance_m / np.linalg.norm(np.array(point2) - np.array(point1))


speed_limit = 50
vehicle_positions = {} 

frame_id = 0

while True:
    ret,frame = cap.read()
    if not ret:
        break
    
    frame_id+=1
    
    # model detection
    results = model(frame,conf=0.4)[0]
    detections = []
    for det in results.boxes:
        x1, y1, x2, y2, conf, cls = det.data[0].cpu().numpy()
        if int(cls) in [2, 3, 5, 7]:
            w = x2 - x1
            h = y2 - y1
            cx = x1 + w  / 2
            cy = y1 + h / 2
            # detections.append([x1, y1, x2, y2, conf, int(cls)])
            detections.append([x1, y1, w, h, conf,int(cls)])


    # deepsort tracking
    tracks = tracker.update_tracks(detections,frame)
    for track in tracks:
        if not track.is_confirmed():
            continue
        
        track_id = track.track_id
        bbox = track.to_ltrb()
        x1, y1, x2,y2 = bbox

        vehicle_img = frame[int(y1):int(y2), int(x1):int(x2)]
        if vehicle_img.size == 0:
            continue
        results_plate = plate_model(vehicle_img,conf=0.15)[0]
        
        plate_text = ""
        for det in results_plate.boxes:
            px1, py1, px2, py2, conf, cls = det.data[0].cpu().numpy()
            plate_crop = vehicle_img[int(py1):int(py2), int(px1):int(px2)]
            if plate_crop.size == 0:
                continue
            plate_text = read_plate(plate_crop)
        
        # speed detection
        centroid = (int(x1 + (x2-x1)/2), int(y2))
        speed_kmph = estimate_speed(track_id, centroid, vehicle_positions, meter_per_pixel, frame_id, fps)
        draw_box(frame, (x1, y1, x2, y2), speed_kmph, speed_limit, track_id, plate_text)
        
    out.write(frame)
    # cv2.imshow("Vehicle Detection",frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break
    
cap.release()
out.release()
cv2.destroyAllWindows()

        
    
        




