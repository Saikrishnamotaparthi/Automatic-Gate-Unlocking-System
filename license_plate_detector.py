import cv2
import pytesseract
import os
from datetime import datetime

PLATE_CASCADE = "assets/haarcascade_russian_plate_number.xml"
SAVE_DIR = "captured_plates"

if not os.path.exists(SAVE_DIR):
    os.makedirs(SAVE_DIR)

def detect_plate(image):
    plate_cascade = cv2.CascadeClassifier(PLATE_CASCADE)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    plates = plate_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in plates:
        roi = image[y:y+h, x:x+w]
        text = pytesseract.image_to_string(roi, config='--psm 8').strip().replace(" ", "")
        if text:
            filename = f"{SAVE_DIR}/plate_{datetime.now().strftime('%Y%m%d_%H%M%S')}.jpg"
            cv2.imwrite(filename, roi)
            return text, roi
    return None, None
