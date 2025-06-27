import cv2
from license_plate_detector import detect_plate
from gate_controller import unlock_gate, lock_gate

AUTHORIZED_PLATES_FILE = "authorized_plates.txt"

def load_authorized_plates():
    with open(AUTHORIZED_PLATES_FILE, 'r') as f:
        return set(line.strip() for line in f)

def main():
    authorized_plates = load_authorized_plates()
    cap = cv2.VideoCapture(0)

    print("[INFO] Starting camera feed. Press 'q' to quit.")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        plate_number, plate_img = detect_plate(frame)

        if plate_number:
            print(f"[INFO] Detected plate: {plate_number}")
            if plate_number in authorized_plates:
                print("[ACCESS GRANTED]")
                unlock_gate()
            else:
                print("[ACCESS DENIED]")
                lock_gate()

        cv2.imshow("Live Feed", frame)
        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
