set shell := ["bash", "-c"]

demo_url := "https://github.com/intel-iot-devkit/sample-videos/raw/master/people-detection.mp4"
venv := "source venv/bin/activate &&"

default: demo

setup:
    [ ! -d "venv" ] && python3 -m venv venv || true
    {{venv}} pip install -q opencv-python ultralytics

demo: setup
    {{venv}} STREAM_URL="{{demo_url}}" python person_detector.py

webcam: setup
    {{venv}} STREAM_URL="0" python person_detector.py

stream url: setup
    {{venv}} STREAM_URL="{{url}}" python person_detector.py
