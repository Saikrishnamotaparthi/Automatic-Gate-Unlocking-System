# Automatic Gate Unlocking System with Car Number Plate Recognition

This project uses Python and OpenCV to detect car number plates in real-time and unlocks the gate if the plate is authorized.

## Features
- Real-time license plate detection
- Unlocks gate on authorized plates
- Stores detected plate images
- Configurable list of authorized plates

## Requirements
```bash
pip install -r requirements.txt
```

## Usage
```bash
python main.py
```

## Files
- `main.py`: Runs the whole system
- `gate_controller.py`: Simulates gate control
- `license_plate_detector.py`: Handles number plate detection
- `authorized_plates.txt`: List of allowed number plates

## Dependencies
- OpenCV
- pytesseract
