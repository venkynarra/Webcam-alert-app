# Webcam Alert App

**Tech Stack:** Python, OpenCV, Threading, Email (SMTP)

## Description
A motion detection system using your webcam. When motion is detected in a frame, it saves the image, and once motion stops, it automatically sends the image via email. This project demonstrates OpenCV techniques, image preprocessing, threading, and basic automation.

## Features
- 🖥 Real-time webcam monitoring
-  Motion detection with frame differencing and contour tracking
-  Sends an email alert with an image of detected movement
-  Auto-cleans image folder on exit using `atexit` + threading

## How It Works
1. Starts webcam and reads live frames.
2. Converts frames to grayscale and applies Gaussian blur.
3. Detects movement using difference frames and contours.
4. When movement stops:
   - Picks the mid-frame from the detection window.
   - Sends it via email using the custom `emailing.py` module.
5. Deletes saved images after sending.

## How to Run
```bash
python main.py
