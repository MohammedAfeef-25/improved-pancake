Here’s a suggested **README.md** file for your project based on the information in the document:

---

# Real-Time Object Size Estimation using YOLOv8

## Introduction

This project implements a **real-time object detection and size estimation system** using **YOLOv8**. It estimates the physical dimensions (width and height) of detected objects from a video stream using a predefined pixel-to-centimeter ratio. This is a cost-effective solution that avoids complex calibration techniques.

---

## Project Goals

* Implement a **real-time object detection system** using YOLOv8.
* Estimate **object dimensions (in cm)** using a fixed pixel-to-cm ratio.
* Provide a simple and low-cost alternative to traditional calibration-based systems.

---

## Problem Definition

Most object detection systems identify objects but do not estimate their real-world size. In industries, manual measurement is time-consuming and prone to error. This project aims to automate size estimation without additional hardware or complex camera calibration.

---

## Proposed Methodology

1. **Model Selection:** Use YOLOv8 for object detection.
2. **Video Capture:** Capture real-time video using a webcam.
3. **Detection:** Apply YOLO to detect objects and extract bounding box coordinates.
4. **Size Estimation:** Convert bounding box dimensions from pixels to cm using a fixed ratio.
5. **Visualization:** Display object name, confidence score, and estimated size on the video stream.

---

## ▶️ How to Run

1. **Clone this repository**

   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```
3. **Download YOLOv8 model**

   ```bash
   pip install ultralytics
   yolo detect predict model=yolov8n.pt
   ```
4. **Run the application**

   ```bash
   python main.py
   ```

---

## Requirements

* Python 3.8+
* OpenCV
* Ultralytics YOLOv8
* Numpy

Install all with:

```bash
pip install opencv-python numpy ultralytics
```

---

## Results

Examples:

* **Smartphone** detected → Estimated Width: \~11.4 cm, Height: \~31.0 cm
* **Water Bottle** detected → Dimensions displayed on live feed
* **Toothbrush** detected → Estimated size shown in real-time

---

## Conclusion

The system successfully detects objects and estimates their dimensions using a fixed ratio. It is suitable for scenarios where approximate size estimation is sufficient.

---

## 📚 References

* [YOLOv8 - Ultralytics](https://github.com/ultralytics/ultralytics)
* [YOLOv4 Paper](https://arxiv.org/abs/2004.10934)
* [YOLO Original Paper](https://arxiv.org/abs/1506.02640)

---
