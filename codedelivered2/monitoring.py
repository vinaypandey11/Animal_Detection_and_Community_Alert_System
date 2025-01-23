import streamlit as st
import pandas as pd
import os
from PIL import Image

# File to store alerts
ALERTS_FILE = 'alerts.csv'

# Initialize the alerts file if it doesn't exist
if not os.path.exists(ALERTS_FILE):
    df = pd.DataFrame(columns=["Time", "Animal", "Confidence", "Image"])
    df.to_csv(ALERTS_FILE, index=False)

# Function to load alerts from the CSV file
def load_alerts():
    if os.path.exists(ALERTS_FILE):
        return pd.read_csv(ALERTS_FILE)
    return pd.DataFrame(columns=["Time", "Animal", "Confidence", "Image"])

# Streamlit UI for Monitoring
st.title("Forest Department - Animal Detection Monitoring")
st.write("This dashboard monitors dangerous animal alerts detected by the system.")

# Create a placeholder for alerts
alerts_placeholder = st.empty()

# Function to display alerts
def display_alerts(alerts_df):
    # Clear previous alerts
    alerts_placeholder.empty()  # Clear any previous output

    # Check if the DataFrame is empty
    if alerts_df.empty:
        alerts_placeholder.info("No alerts yet.")
    else:
        alerts_placeholder.subheader("Dangerous Animal Alerts")

        # Display column headers
        col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
        with col1:
            st.write("Image")
        with col2:
            st.write("Time")
        with col3:
            st.write("Animal")
        with col4:
            st.write("Confidence")

        # Create a dataframe to hold display data
        display_data = []

        for index, row in alerts_df.iterrows():
            img_path = row["Image"]
            if isinstance(img_path, str) and os.path.exists(img_path):
                image = Image.open(img_path)
                # Save the image in a format suitable for display
                display_data.append({
                    "Time": row["Time"],
                    "Animal": row["Animal"],
                    "Confidence": f"{row['Confidence']:.2f}",
                    "Image": image
                })
            else:
                st.error("Image not found or path is invalid.")

        # Display alerts in a structured table format
        if display_data:
            for item in display_data:
                col1, col2, col3, col4 = st.columns([1, 2, 2, 1])
                with col1:
                    # Display the image with a click-to-zoom effect
                    if item["Image"]:
                        st.image(item["Image"], width=300, use_column_width=True, caption='Click to enlarge', clamp=True)
                    else:
                        st.error("Image not found.")
                with col2:
                    st.write(item["Time"])
                with col3:
                    st.write(item["Animal"])
                with col4:
                    st.write(item["Confidence"])

# Load alerts from the CSV file initially
alerts_df = load_alerts()

# Display the alerts initially
display_alerts(alerts_df)

# Button to refresh the alerts
if st.button("Refresh Alerts"):
    # Load alerts again when the button is pressed
    new_alerts_df = load_alerts()  # Refresh alerts data
    
    # Clear previous alerts and display updated alerts
    if not new_alerts_df.equals(alerts_df):  # Check if new alerts differ
        alerts_df = new_alerts_df  # Update the alerts DataFrame
        display_alerts(alerts_df)  # Display the updated alerts

# Button to delete all alerts
if st.button("Clear Alerts"):
    # Create an empty DataFrame and overwrite the CSV file to delete all alerts
    empty_df = pd.DataFrame(columns=["Time", "Animal", "Confidence", "Image"])
    empty_df.to_csv(ALERTS_FILE, index=False)
    
    # Refresh the alerts after deletion
    alerts_df = load_alerts()
    display_alerts(alerts_df)
    st.success("All alerts have been deleted.")
