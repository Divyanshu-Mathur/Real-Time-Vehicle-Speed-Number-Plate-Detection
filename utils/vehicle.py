import cv2

def draw_box(frame,bbox,speed,speed_limit,track_id,plate_text):
    x1,y1,x2,y2 = map(int,bbox)
    color = (0,255,0) if speed<=speed_limit else (0,0,255)
    cv2.rectangle(frame,(x1,y1-10),(x2,y2),color,2)
    text = f"{int(speed)}km/h {plate_text}"
    cv2.putText(frame,text,(x1+5,y1-15),cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    