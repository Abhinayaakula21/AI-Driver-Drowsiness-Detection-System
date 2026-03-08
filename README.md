# AI-Driver-Drowsiness-Detection-System
This project implements an AI-based Driver Drowsiness Detection System using computer vision.
The system monitors the driver's face using a webcam in real time.
It uses MediaPipe Face Mesh to detect facial landmarks.
The system focuses on eye landmarks to analyze eye movements.
The Eye Aspect Ratio (EAR) is calculated to determine whether the eyes are open or closed.
If the eyes remain closed for several frames, the system identifies driver fatigue.
When drowsiness is detected, the system triggers an alarm sound to alert the driver.
The project uses Python, OpenCV, MediaPipe, and Winsound libraries.
Facial landmark points are displayed on the video frame for visualization.
The system continuously processes frames for real-time monitoring.
This project demonstrates how AI and computer vision can improve road safety.
The program stops when the user presses the 'q' key.
The system can be further improved by adding head pose detection and mobile alerts.
This project is useful for driver monitoring systems used in modern vehicles.
