import numpy as np


# def estimate_speed(track_id, centroid, vehicle_positions, meter_per_pixel, frame_id, fps):
#     if track_id in vehicle_positions:
#         prev_center,prev_frame = vehicle_positions[track_id]
#         pixel_distance = np.linalg.norm(np.array(centroid) - np.array(prev_center))
#         real_dist = pixel_distance * meter_per_pixel
#         time_elasped = (frame_id-prev_frame)/fps
#         mps = real_dist/max(time_elasped,1e-6)
#         kmph = mps*3.6
#     else:
#         kmph=0.0
        
#     vehicle_positions[track_id]=(centroid,frame_id)
#     return kmph

def estimate_speed(track_id, centroid, vehicle_positions,
                   meter_per_pixel, frame_id, fps, frame_gap=10):

    if track_id not in vehicle_positions:
        vehicle_positions[track_id] = {
            "centroid": centroid,
            "frame": frame_id,
            "speed": 0
        }
        return 0

    prev_data = vehicle_positions[track_id]
    prev_centroid = prev_data["centroid"]
    prev_frame = prev_data["frame"]

    frame_diff = frame_id - prev_frame

    if frame_diff >= frame_gap:
        pixel_dist = np.linalg.norm(
            np.array(centroid) - np.array(prev_centroid)
        )
        distance_m = pixel_dist * meter_per_pixel
        time_sec = frame_diff / fps

        speed_mps = distance_m / time_sec
        speed_kmph = speed_mps * 3.6

        vehicle_positions[track_id] = {
            "centroid": centroid,
            "frame": frame_id,
            "speed": speed_kmph
        }
    else:
        speed_kmph = prev_data["speed"]

    return speed_kmph

