# Real-Time Object Size Estimation using YOLOv8

## 📌 Introduction

This project implements a **real-time object detection and size estimation system** using **YOLOv8**. It estimates the **physical dimensions (width and height)** of detected objects in a video stream using a predefined **pixel-to-centimeter ratio**. This is a cost-effective alternative to complex calibration methods.

---

## 🎯 Project Goals

* Build a **real-time object detection system** using YOLOv8.
* Estimate object **dimensions (in cm)** using a fixed pixel-to-cm ratio.
* Provide a simple and low-cost alternative to traditional calibration-based systems.

---

## 🧩 Problem Definition

Most object detection systems only identify objects—they don't estimate their real-world sizes. In industrial settings, manual measurement is often time-consuming and error-prone. This project aims to **automate size estimation** without requiring extra hardware or complex camera calibration.

---

## 🔍 Methodology

1. **Model Selection**: Use YOLOv8 for object detection.
2. **Video Capture**: Capture real-time video from a webcam.
3. **Object Detection**: Apply YOLO to detect objects and extract bounding box coordinates.
4. **Size Estimation**: Convert bounding box dimensions from pixels to centimeters using a predefined ratio.
5. **Visualization**: Display object label, confidence score, and estimated dimensions on the video feed.

---

## ▶️ How to Run

1. **Clone the Repository**

   ```bash
   git clone https://github.com/MohammedAfeef-25/real-time-size-estimator.git
   cd real-time-size-estimator
   ```

2. ✅ Requirements

   * Python 3.8 or higher
   * OpenCV
   * NumPy
   * Ultralytics YOLOv8

   ```bash
   pip install opencv-python numpy ultralytics
   ```

3. **Run the Application**

   ```bash
   python project.py
   ```

---

## 📷 Sample Results

<img width="523" height="404" alt="image" src="https://github.com/user-attachments/assets/51838bcf-b160-40e0-8021-6325b2890351" />
<img width="545" height="432" alt="image" src="https://github.com/user-attachments/assets/c6f78c7e-6816-4912-934d-63439277a2f8" />



---

## ✅ Conclusion

This system successfully performs **object detection and approximate size estimation** using a fixed ratio. It's ideal for use cases where **approximate dimensions are sufficient** and high-precision calibration is unnecessary.

---

## 📚 References

* [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)
* [YOLOv4: Optimal Speed and Accuracy](https://arxiv.org/abs/2004.10934)
* [YOLO: You Only Look Once (Original Paper)](https://arxiv.org/abs/1506.02640)
