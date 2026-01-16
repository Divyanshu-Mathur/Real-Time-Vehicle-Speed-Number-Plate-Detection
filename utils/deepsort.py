from deep_sort_realtime.deepsort_tracker import DeepSort as DS


class DeepSort:
    def __init__(self, max_age=30, n_init=3, nms_max_overlap=1.0):
        self.tracker = DS(max_age=max_age,
                          n_init=n_init,
                          nms_max_overlap=nms_max_overlap,
                          embedder='mobilenet',
                          half=True,
                          embedder_gpu=True)

    def update_tracks(self, detections, frame=None):
        dets = []
        for det in detections:
            x1, y1, x2, y2, conf, cls = det
            dets.append(((float(x1), float(y1), float(x2), float(y2)), float(conf)))

        tracks = self.tracker.update_tracks(dets, frame=frame)
        return tracks