# 🚗 Real-Time Vehicle Speed & Number Plate Detection using YOLOv11

This project implements a **real-time computer vision system** to detect vehicles, track them across frames, estimate their speed using **perspective-based distance estimation**, and recognize vehicle **number plates**. Vehicles exceeding a predefined speed limit are highlighted with a **red bounding box**, while others are shown in **green**.

The system is suitable for **traffic monitoring, speed violation detection, and intelligent transportation systems (ITS)**.

---

## 📌 Key Features

- 🚘 Vehicle detection using **YOLOv11**
- 🔍 License plate detection using a **custom-trained YOLO model**
- 🔤 Number plate recognition (OCR) using **EasyOCR**
- 🔁 Multi-object tracking with **DeepSORT**
- 📏 Speed estimation using **distance-over-time with perspective calibration**
- 🎨 Dynamic bounding boxes  
  - 🟥 Red → Speed exceeds limit  
  - 🟩 Green → Within speed limit
- 🎥 Works on real-world traffic videos

---

## 🧠 Technologies Used

| Component | Technology |
|---------|-----------|
| Object Detection | YOLOv11 (Ultralytics) |
| License Plate Detection | Custom YOLO Model |
| Tracking | DeepSORT |
| OCR | EasyOCR |
| Speed Estimation | Perspective Mapping |
| Visualization | OpenCV |
| Language | Python |

---

## 📂 Project Structure

```

Real-Time Vehicle Speed & Number Plate Detection using YOLOv11/
│
├── models/
│   └── plate_model.pt
│
├── Output/
│   └── test_1_out.mp4
│
├── utils/
│   ├── deepsort.py
│   ├── speed.py
│   ├── vehicle.py
│   ├── ocr.py
│   └── Detect_Licence_Plate.ipynb
│
├── Video/
│   └── test_1.mp4
│
├── get_coord.ipynb
├── main.py
├── yolo11n.pt
├── requirements.txt
└── README.md

```

---

## ⚙️ Workflow Overview

1. **Vehicle Detection**
   - YOLOv11 detects vehicles (car, bus, truck, motorbike)

2. **Multi-Object Tracking**
   - DeepSORT assigns a unique ID to each vehicle

3. **Perspective Calibration**
   - Two known reference points are selected in the scene
   - Real-world distance between them is defined
   - Pixel-to-meter ratio is calculated

4. **Speed Estimation**
   - Vehicle centroid movement across frames is tracked
   - Speed is computed using distance over time

5. **License Plate Detection & OCR**
   - License plate is detected inside the vehicle bounding box
   - EasyOCR extracts plate text

6. **Visualization**
   - Bounding box color changes based on speed limit
   - Speed, ID, and plate number are displayed

---

## 📏 Speed Estimation Formula

```

Speed (km/h) = (Pixel Distance × Meter per Pixel) / Time × 3.6

````

Where:
- Pixel Distance → Movement of vehicle centroid
- Meter per Pixel → Derived using perspective calibration
- Time → Frame difference divided by FPS

---

## ▶️ How to Run

### 1️⃣ Clone the Repository

```bash
git clone <repository-url>
cd Project-5-Car-Speed
````

---

### 2️⃣ Create & Activate Virtual Environment

```bash
python -m venv venv
```

**Windows**

```powershell
.\venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4️⃣ Run the Project

```bash
python main.py
```

* Output video will be saved in the `Output/` folder
* Press **Q** to stop execution

---

## 🎯 Speed Threshold Logic

```python
speed_limit = 50  # km/h
```

* 🟥 Speed > limit → Red bounding box
* 🟩 Speed ≤ limit → Green bounding box

---

## 📌 Use Cases

* Traffic speed monitoring
* Automatic speed violation detection
* Smart city surveillance
* Highway traffic analytics
* Intelligent transportation systems

---

