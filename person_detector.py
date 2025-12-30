import cv2
import time
import os
from ultralytics import YOLO

DEFAULT_URL = "https://github.com/intel-iot-devkit/sample-videos/raw/master/people-detection.mp4"

def get_source():
    url = os.environ.get("STREAM_URL", DEFAULT_URL)
    return int(url) if url.isdigit() else url

def main():
    model = YOLO("yolo11s.pt")
    cap = cv2.VideoCapture(get_source())
    prev_time = time.time()

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        for box in model(frame, classes=[0], verbose=False)[0].boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            conf = float(box.conf[0])
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, f"{conf:.0%}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

        fps = 1 / (time.time() - prev_time)
        prev_time = time.time()
        cv2.putText(frame, f"FPS: {fps:.0f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.imshow("Person Detection", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
