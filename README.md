# **🧠 Face Detection & Real-Time Alert System**

---

## 🔍 Project Overview

This Python-based project performs real-time face recognition from a video stream and sends instant alerts to a Flask web interface when a match is found. It compares faces against known suspects and provides detailed information along with live detection updates using Flask-SocketIO.

---

## 📂 Project Structure

```
face_detection_alert/
├── facedetection.py         # Face recognition and alert emitter
├── app.py                   # Flask web server with SocketIO
├── templates/
│   └── index.html           # Web interface to display alerts
├── person4.jpg              # Known face 1
├── person5.jpg              # Known face 2
├── v7.mp4                   # Input video for face detection
├── .env                     # Environment variables (if needed)
└── README.md                # Project documentation
```

---

## 🔧 Requirements

* Python 3.x
* OpenCV
* face\_recognition
* Flask
* Flask-SocketIO

### 📦 Install Dependencies

```bash
pip install opencv-python face_recognition flask flask-socketio
```

---

## ▶️ How to Run

1. Ensure `person4.jpg`, `person5.jpg`, and `v7.mp4` are placed in the project folder.
2. Start the Flask web server:

```bash
python app.py
```

3. In a separate terminal, run the face detection script:

```bash
python facedetection.py
```

4. Visit `http://127.0.0.1:5000` in your browser to see real-time alerts.

---

## ⚙️ How It Works

* Loads known faces from `person4.jpg` and `person5.jpg`.
* Reads video frames from `v7.mp4`.
* Detects and encodes faces in each frame.
* Compares with known encodings using face\_recognition.
* If a match is found:

  * Displays bounding box and "Suspect Detected".
  * Sends alert and personal info to the web dashboard via SocketIO.

---

## 🧠 Key Features

* Real-time face recognition from video
* Instant alerts with person info to web interface
* Live video frame display with bounding box and label
* Uses SocketIO for seamless Python-to-browser communication

---

## 📌 Parameters

* `tolerance = 0.6`: Face match threshold
* `frame_skip = 2`: Controls frame processing speed
* Personal info can be customized inside `facedetection.py`

---

## 📈 Output

* Detection status in terminal
* Web page showing:

  * Match status
  * Suspect details (name, DOB, contact, etc.)
  * Live real-time updates

---

## 📸 Output Frame Example
![Screenshot 2025-06-16 152156](https://github.com/user-attachments/assets/baa8055d-a6f5-4735-a3c4-f2f08b30b0b6)
![Screenshot 2025-06-16 152216](https://github.com/user-attachments/assets/499913b2-668d-483e-af79-65cc5eb89ade)
![Screenshot 2025-06-16 152227](https://github.com/user-attachments/assets/ae2acc9b-af17-4087-b94d-8b08fc7670e8)
![Screenshot 2025-06-16 152247](https://github.com/user-attachments/assets/dac79293-7965-47e8-996c-7144f922c8c2)


### 📌
### The above face detection is one part of this comprehensive project. 
The Accident Detection and Alert System is a real-time AI-powered solution that identifies road accidents, detects overspeeding vehicles, and recognizes victims using facial recognition technology. By analyzing live or recorded CCTV footage with computer vision models, the system detects incidents instantly and sends alert messages containing the date, time, and exact location to the nearest police station or emergency contact. It maintains privacy by not storing any personal data and dynamically manages traffic flow during emergencies by counting vehicles in all directions and adjusting traffic signals accordingly. This intelligent system enhances road safety, accelerates emergency response, and supports effective traffic management. 

