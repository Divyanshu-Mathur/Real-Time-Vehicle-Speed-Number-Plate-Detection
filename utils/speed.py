import numpy as np


def estimate_speed(track_id, centroid, vehicle_positions, meter_per_pixel, frame_id, fps):
    if track_id in vehicle_positions:
        prev_center,prev_frame = vehicle_positions[track_id]
        pixel_distance = np.linalg.norm(np.array(centroid) - np.array(prev_center))
        real_dist = pixel_distance * meter_per_pixel
        time_elasped = (frame_id-prev_frame)/fps
        mps = real_dist/max(time_elasped,1e-6)
        kmph = mps*3.6
    else:
        kmph=0.0
        
    vehicle_positions[track_id]=(centroid,frame_id)
    return kmph
