# Real-Time Hand Gesture Recognition

A real-time hand gesture recognition system built using Python, OpenCV, and MediaPipe. The system detects hand landmarks through a webcam and identifies predefined hand gestures using geometric calculations and rule-based classification.

## Features

- Real-time hand detection using MediaPipe.
- Detection of 21 hand landmarks.
- 3D finger angle calculation.
- Finger and thumb state detection.
- Recognition of predefined hand gestures.
- Gesture stabilization using recent frame history.
- Real-time webcam visualization.
- Support for detecting up to two hands.

## Supported Gestures

| Gesture | Recognition |
|---|---|
| ✊ | FIST |
| 🖐️ | OPEN_PALM |
| ☝️ | POINTING |
| ✌️ | VICTORY |
| 🤙 | CALL_ME |
| 👍 | THUMBS_UP |
| 👎 | THUMBS_DOWN |

## Technologies Used

- Python
- OpenCV
- MediaPipe
- NumPy

## Project Structure

```text
hand-gesture-recognition/
│
├── notebooks/
│   └── gesture_recognition.ipynb
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   ├── hand_detector.py
│   └── gesture_recognizer.py
│
├── README.md
├── requirements.txt
└── .gitignore
```

## How It Works

The system follows these steps:

1. Captures video frames from the webcam using OpenCV.
2. Detects hand landmarks using MediaPipe.
3. Extracts 21 hand landmark coordinates.
4. Calculates 3D finger joint angles.
5. Determines whether individual fingers are open or closed.
6. Identifies gestures using predefined rules.
7. Stabilizes predictions using recent frame history.
8. Displays the recognized gesture on the webcam feed.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/itz-me-sree/Hand-Gesture-Recognition.git
```

### 2. Navigate to the project directory

```bash
cd hand-gesture-recognition
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the environment

Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

From the project root directory, execute:

```bash
python -m src.main
```

The webcam will open and display the detected hand landmarks along with the recognized gesture.

Press **Q** to exit the application.

## Limitations

- Gesture recognition is based on predefined geometric rules.
- Detection accuracy may vary with hand orientation and camera positioning.
- Lighting conditions and hand visibility can affect detection.
- The system recognizes only a limited set of predefined gestures.
- Gesture classification is not based on a trained machine learning model.

## Future Improvements

- Improve gesture recognition robustness.
- Add finger counting functionality.
- Support additional hand gestures.
- Explore machine learning-based gesture classification.

## Author

Sreerag S
