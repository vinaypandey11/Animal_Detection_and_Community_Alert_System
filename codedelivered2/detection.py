import streamlit as st
import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import pandas as pd
from datetime import datetime
import cv2
import os
import time

# Load pre-trained MobileNetV2 model
model = MobileNetV2(weights='imagenet')

# Directory to save captured images
IMAGE_DIR = 'captured_images'
if not os.path.exists(IMAGE_DIR):
    os.makedirs(IMAGE_DIR)

# File to store alerts
ALERTS_FILE = 'alerts.csv'

# Function to log alerts into a CSV file
def log_alert(animal_name, confidence, image_path):
    if not os.path.exists(ALERTS_FILE):
        df = pd.DataFrame(columns=["Time", "Animal", "Confidence", "Image"])
    else:
        df = pd.read_csv(ALERTS_FILE)

    new_alert = pd.DataFrame({
        "Time": [datetime.now().strftime('%Y-%m-%d %H:%M:%S')],
        "Animal": [animal_name],
        "Confidence": [confidence],
        "Image": [image_path]  # Save the image path
    })
    
    df = pd.concat([df, new_alert], ignore_index=True)
    df.to_csv(ALERTS_FILE, index=False)

# Function to predict the animal in the image
def predict_animal(img):
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)
    
    predictions = model.predict(img_array)
    label = decode_predictions(predictions, top=1)[0][0]
    return label[1], label[2]  # return name and confidence

# Function to capture image from webcam
def capture_image():
    # Initialize webcam
    video_capture = cv2.VideoCapture(0)

    # Check if the webcam is opened successfully
    if not video_capture.isOpened():
        st.error("Unable to open the webcam. Please check your webcam connection.")
        return

    # Set up the OpenCV window
    video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    # Display the webcam feed
    st.write("Webcam Feed")
    frame_container = st.empty()
    timer_text = st.empty()

    # Initialize timer
    timer_seconds = 5
    start_time = time.time()

    while time.time() - start_time < timer_seconds:
        ret, frame = video_capture.read()
        if not ret:
            st.error("Failed to capture frame from the webcam.")
            break

        # Display the frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame_container.image(frame, channels="RGB")

        # Update timer
        remaining_time = int(timer_seconds - (time.time() - start_time))
        timer_text.text(f"Time remaining: {remaining_time} seconds")

    # Capture picture automatically
    ret, frame = video_capture.read()
    if ret:
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        file_path = os.path.join(IMAGE_DIR, f"captured_{timestamp}.jpg")
        cv2.imwrite(file_path, frame)
        st.success("Image captured successfully!")

        # Process the captured image
        img = image.load_img(file_path, target_size=(224, 224))
        
        # Predict the animal
        animal_name, confidence = predict_animal(img)
        st.write(f"Predicted animal: **{animal_name}** with confidence **{confidence:.2f}**")
        
        # Dangerous animal list
        dangerous_animals = ["lion", "tiger", "leopard"]
        
        # Check if the animal is dangerous
        if animal_name.lower() in dangerous_animals:
            st.warning(f"Warning! Dangerous animal detected: {animal_name}")
            log_alert(animal_name, confidence, file_path)  # Pass the image path
            st.success(f"Alert logged for {animal_name}")
        else:
            st.info(f"Detected animal: {animal_name} is not a threat.")
    else:
        st.error("Failed to capture image from the webcam.")

    video_capture.release()  # Release the webcam

# Streamlit UI
st.title("Forest Department Animal Classifier")
st.write("Click the button to capture an image of the animal using your webcam.")

if st.button("Capture Image"):
    capture_image()
