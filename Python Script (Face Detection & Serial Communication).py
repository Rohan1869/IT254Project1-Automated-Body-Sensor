#Python Script (Face Detection & Serial Communication)

import cv2
import serial
import numpy as np
import tensorflow as tf
import json

# Load Teachable Machine model
MODEL_PATH = "model.json"

# Load model architecture and weights
with open("model.json", "r") as f:
    model_json = json.load(f)

model = tf.keras.models.model_from_json(json.dumps(model_json))
model.load_weights("weights.bin")

# Initialize Serial Communication with Arduino
arduino = serial.Serial('COM3', 9600)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to match model input size
    resized_frame = cv2.resize(frame, (224, 224))
    input_data = np.expand_dims(resized_frame, axis=0).astype(np.float32)

    # Run model prediction
    predictions = model.predict(input_data)
    face_detected = predictions[0][1] > 0.5  # Adjust threshold if needed

    # Send signal to Arduino
    arduino.write(b'1' if face_detected else b'0')

    # Display the webcam feed
    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()
arduino.close()

