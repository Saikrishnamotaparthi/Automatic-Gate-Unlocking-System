# 🚗 Automatic Gate Unlocking System using Car Number Plate Recognition

This Python-based system uses OpenCV and Tesseract OCR to detect and recognize license plates of vehicles in real-time. If the detected number plate matches one in the authorized list, the gate is automatically unlocked. It simulates a smart security system for residential societies, offices, and parking zones.

---

## 📌 Features

- 🔍 Real-time vehicle license plate detection via webcam  
- 🧠 OCR-based number recognition using Tesseract  
- ✅ Matches with authorized plates  
- 🔓 Simulated gate unlock/lock mechanism  
- 💾 Captures and saves plate images for logging  
- 📁 Modular code design with expandability  

---

## 🛠️ Technologies Used

- Python 3  
- OpenCV  
- Pytesseract  
- Haar Cascade Classifier (for number plate detection)  

---

## 🧱 Project Structure

```
Automatic-Gate-Unlocking-System/
├── main.py                      # Main execution script
├── gate_controller.py          # Gate lock/unlock simulation
├── license_plate_detector.py   # Detection & OCR logic
├── authorized_plates.txt       # Authorized plate list
├── requirements.txt            # Dependencies
├── README.md                   # Documentation
├── assets/
│   └── haarcascade_russian_plate_number.xml  # Pre-trained model
└── captured_plates/            # Saved plate snapshots
```

---

## 🖥️ Setup Instructions

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Install Tesseract OCR
- **Windows**: [Download here](https://github.com/tesseract-ocr/tesseract/wiki)
- **Linux**:
```bash
sudo apt install tesseract-ocr
```

### 3. Run the project
```bash
python main.py
```

---

## ✅ Sample Workflow

1. Start webcam  
2. Detect license plate using Haar cascade  
3. Extract text using Tesseract OCR  
4. Check against `authorized_plates.txt`  
5. If matched → Gate unlocks  
6. Else → Gate remains locked  

---

## 📸 Sample Output

```plaintext
[INFO] Starting camera feed. Press 'q' to quit.
[INFO] Detected plate: AP31AB1234
[ACCESS GRANTED]
🔓 Gate Unlocked!
```

---

## 📈 Future Improvements

- GUI using Tkinter or PyQt  
- Deep learning model (YOLO or EasyOCR) for better accuracy  
- Hardware gate control using Raspberry Pi or Arduino  
- CSV logging of access events  
- Admin mobile app integration  

---

## 🙋 Author

**Sai Krishna Motaparthi**  
Tech enthusiast working on smart automation, robotics, and embedded systems.

---

## 📜 License

This project is licensed under the MIT License.
