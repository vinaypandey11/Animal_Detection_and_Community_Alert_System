# Animal Detection & Community Alert System

This project aims to detect and classify dangerous wild animals (like lions, tigers, and leopards) entering human localities using AI and IoT technologies. The system ensures public safety by sending real-time alerts through a Streamlit-based web application and triggering an Arduino-powered siren.

---

## Features
- Real-time animal detection and classification using deep learning models (TensorFlow/Keras).
- Web interface built with Streamlit for monitoring and manual verification.
- IoT-enabled siren alerts using Arduino for real-time public warnings.
- Automatic logging of detection alerts, including timestamps, detected animal name, confidence level, and image.

---

## Technologies Used
- **Programming Language**: Python
- **Libraries/Frameworks**: TensorFlow, Keras, OpenCV, Pandas, Streamlit
- **IoT Integration**: Arduino (with sensors/siren)
- **Frontend**: Streamlit-based monitoring dashboard

---

## Installation and Setup

### 1. Prerequisites
- Python 3.8 or higher
- Arduino IDE (for IoT setup)
- A webcam or external camera for real-time image capture
- Installed libraries:
  ```bash
  pip install tensorflow keras opencv-python-headless pandas streamlit pillow
  ```

---

### 2. Clone the Repository
```bash
git clone https://github.com/username/animal-detection-alert-system.git
cd animal-detection-alert-system
```

---

### 3. Run the Monitoring Application
1. Start the monitoring dashboard to view and manage detected alerts:
   ```bash
   streamlit run monitoring.py
   ```
2. Open the local Streamlit link (http://localhost:8501) in your browser.

---

### 4. Run the Detection Application
1. Start the animal detection system:
   ```bash
   streamlit run detection.py
   ```
2. Use the provided button to capture an image via webcam.
3. The system will detect the animal, log the details, and trigger the IoT siren if it’s a dangerous animal.

---

### 5. Arduino Setup
- Connect a siren or buzzer to your Arduino board.
- Upload the Arduino code (provided in the `arduino/` folder) to your Arduino board using the Arduino IDE.
- Ensure the system communicates with Python via serial communication for triggering sirens.

---

## Directory Structure
```
animal-detection-alert-system/
├── arduino/                    # Arduino scripts for IoT siren integration
├── captured_images/            # Directory to store captured images
├── monitoring.py               # Monitoring application (Streamlit)
├── detection.py                # Animal detection application (Streamlit)
├── alerts.csv                  # Logs of detected animals and alerts
└── README.md                   # Project documentation
```

---

## Steps to Test the System
1. Open the `monitoring.py` and `detection.py` applications in separate terminals.
2. Capture images using the detection system and view the logged alerts in the monitoring dashboard.
3. Test the IoT siren by confirming a dangerous animal detection.

---

## Contributing
Feel free to contribute by creating issues or submitting pull requests to improve the system.

---

## License
This project is licensed under the MIT License.

## Snapshots:
![detection1screen_page-0001](https://github.com/user-attachments/assets/f45bdef9-0498-40fc-a2e6-399b04d95a2d)
![detection_page-0001](https://github.com/user-attachments/assets/1db9250e-b28c-4c08-8395-ce65545b3975)
![detection_page-0002](https://github.com/user-attachments/assets/03d87de0-0a73-4478-a821-df0de88239bd)
![monitoring_page-0001](https://github.com/user-attachments/assets/85ab87a6-e36d-41fe-b372-59ca3250e2d9)
