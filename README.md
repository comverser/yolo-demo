# YOLO Person Detection Demo

Real-time person detection using YOLOv11s with OpenCV.

## Setup

```bash
just setup
```

## Usage

**Run with preset demo video (rescue drone footage):**
```bash
just preset
```

**Run with custom video/stream URL:**
```bash
just stream "https://example.com/video.mp4"
```

**Run with webcam:**
```bash
just stream 0
```

Press `q` to quit.

## Demo Video

Rescue drone footage: https://www.youtube.com/watch?v=IF_JL2LEcFo

## Requirements

- Python 3
- OpenCV
- Ultralytics YOLO
- yt-dlp (for downloading demo video)
