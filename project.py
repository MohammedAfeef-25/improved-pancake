from ultralytics import YOLO
import cv2

# ==== SETTINGS ====
FIXED_PIXEL_TO_CM_RATIO = 0.1            # Predefined pixel to cm ratio (example value)
MODEL_PATH = "yolov8n.pt"                 # Path to YOLO model

# ==== INITIALIZATION ====
model = YOLO(MODEL_PATH)
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# Use a fixed pixel-to-cm ratio directly
print(f"[INFO] Using fixed calibration: 1 pixel = {FIXED_PIXEL_TO_CM_RATIO} cm")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model(frame)[0]

    for box in results.boxes:
        x1, y1, x2, y2 = map(int, box.xyxy[0])
        cls_id = int(box.cls[0])
        label = model.names[cls_id]  # Object class label
        conf = float(box.conf[0])    # Confidence of detection
        width_pixels = x2 - x1
        height_pixels = y2 - y1

        # === SIZE ESTIMATION ===
        # Estimate the size in centimeters based on the predefined ratio
        est_width_cm = width_pixels * FIXED_PIXEL_TO_CM_RATIO
        est_height_cm = height_pixels * FIXED_PIXEL_TO_CM_RATIO
        size_text = f"W: {est_width_cm:.1f} cm, H: {est_height_cm:.1f} cm"

        # === DRAWING ===
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label_text = f"{label} {conf:.2f}"
        cv2.putText(frame, label_text, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
        cv2.putText(frame, size_text, (x1, y2 + 20),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)

    cv2.imshow("Object Size Estimation (Fixed Ratio)", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
