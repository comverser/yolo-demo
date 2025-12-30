set shell := ["bash", "-c"]

preset := "rescue_demo.mp4"
venv := "source venv/bin/activate &&"

default: preset

setup:
    [ ! -d "venv" ] && python3 -m venv venv || true
    {{venv}} pip install -q opencv-python ultralytics yt-dlp

download: setup
    {{venv}} yt-dlp -f "best[height<=720]" --download-sections "*09:11-12:11" -o "{{preset}}" "https://www.youtube.com/watch?v=IF_JL2LEcFo"

preset: setup
    [ ! -f "{{preset}}" ] && just download || true
    {{venv}} STREAM_URL="{{preset}}" python person_detector.py

stream url: setup
    {{venv}} STREAM_URL="{{url}}" python person_detector.py
