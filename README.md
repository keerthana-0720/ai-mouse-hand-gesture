# AI Mouse

A real-time hand gesture controlled mouse using a webcam.

## Overview

This project uses a webcam to detect hand landmarks and uses the position of the index finger to control the computer mouse cursor.

## How It Works

1. OpenCV captures live video from the webcam.
2. MediaPipe Hands detects hand landmarks.
3. The index finger landmark (landmark 8) is tracked.
4. Its webcam position is mapped to screen coordinates.
5. PyAutoGUI moves the mouse cursor according to the index finger position.

## Technologies Used

- Python
- OpenCV
- MediaPipe
- PyAutoGUI

## Project Structure

```text
AI Mouse/
├── mouse.py
├── webcam_test.py
├── requirements.txt
├── README.md
└── .gitignore
```

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Test the webcam

```bash
python webcam_test.py
```

Press `Esc` to exit.

### Run the AI Mouse

```bash
python mouse.py
```

Move your index finger in front of the webcam to control the mouse cursor.

Press `Esc` to exit.

## Current Functionality

The current implementation provides cursor movement using the index finger. Mouse clicking and scrolling are not implemented.
