import cv2
import numpy as np
from object_detection import ObjectDetection
import math

# Initialize Object Detection
od = ObjectDetection()

cap = cv2.VideoCapture(0)

# Initialize trackers
tracking_objects = {}
track_id = 0

def assign_new_id():
    global track_id
    track_id += 1
    return track_id

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Detect objects on frame
    (class_ids, scores, boxes) = od.detect(frame)
    center_points_cur_frame = []

    for box in boxes:
        (x, y, w, h) = box
        cx = int((x + x + w) / 2)
        cy = int((y + y + h) / 2)
        center_points_cur_frame.append((cx, cy))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Track objects
    tracking_objects_copy = tracking_objects.copy()
    for cur_pt in center_points_cur_frame:
        assigned = False
        for object_id, tracked_pt in tracking_objects_copy.items():
            if math.hypot(tracked_pt[0] - cur_pt[0], tracked_pt[1] - cur_pt[1]) < 20:
                tracking_objects[object_id] = cur_pt
                assigned = True
                break
        if not assigned:
            new_id = assign_new_id()
            tracking_objects[new_id] = cur_pt

    # Visualize tracking
    for object_id, pt in tracking_objects.items():
        cv2.circle(frame, pt, 5, (0, 0, 255), -1)
        cv2.putText(frame, str(object_id), (pt[0], pt[1] - 7), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:  # ESC key to break
        break

cap.release()
cv2.destroyAllWindows()

# Print total unique cars detected
print(f"Total unique cars detected: {track_id}")
