# IT254Project1-Automated-Body-Sensor
This project integrates an Arduino Mega 2560, Google Teachable Machine, and Python to create a face-detection-based security system which can also serve as a body sensor for multitude of reasons. When the system detects a face, it triggers an LED on the Arduino board using Serial Communication.
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Requirements/Materials:

Hardware

Arduino Mega 2560 – The microcontroller to process serial data.

LED + 220Ω Resistor – Used for visual indication.

USB Cable – To connect the Arduino to the PC.

Jumper Wires – To connect the LED and Arduino.

Webcam – Used for real-time face detection.

Software & Libraries

Python – Runs the AI model and processes webcam data.

TensorFlow.js – Loads the trained model.

OpenCV – Captures and processes images from the webcam.

PySerial – Enables communication between Python and Arduino.

Arduino IDE – To upload code to the Arduino Mega 2560.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Installation & Setup

Step 1: Install Required Python Libraries

Open a terminal and run: pip install tensorflow tensorflowjs opencv-python pyserial numpy


pip install tensorflow tensorflowjs opencv-python pyserial numpy

Step 2: Load the Teachable Machine Model

Export your Teachable Machine Image Model in TensorFlow.js format.

Extract and place it in the project folder.

Step 3: Connect the LED to Arduino

Component----------Arduino Pin

LED (Anode +)----> Pin 13 (via 220Ω resistor)

LED (Cathode -)------>GND


PYTHON CODE:

import cv2
import serial
import numpy as np
import tensorflowjs as tfjs
import tensorflow as tf
import json

# Load the Teachable Machine model
MODEL_PATH = "/mnt/data/teachable_machine_model/model.json"

# Load model architecture and weights
with open("/mnt/data/teachable_machine_model/model.json", "r") as f:
    model_json = json.load(f)

model = tf.keras.models.model_from_json(json.dumps(model_json))
model.load_weights("/mnt/data/teachable_machine_model/weights.bin")

# Set up serial communication with Arduino (change 'COM3' to your port)
arduino = serial.Serial('COM3', 9600)

# Start capturing video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize frame to match model input size
    resized_frame = cv2.resize(frame, (224, 224))  
    input_data = np.expand_dims(resized_frame, axis=0).astype(np.float32)

    # Run the model
    predictions = model.predict(input_data)
    
    # Get prediction (Class 0 = No Face, Class 1 = Face Detected)
    face_detected = predictions[0][1] > 0.5  # Adjust threshold if needed

    # Send signal to Arduino
    if face_detected:
        arduino.write(b'1')  # Send '1' if face detected
    else:
        arduino.write(b'0')  # Send '0' if no face

    # Show webcam feed
    cv2.imshow("Face Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()
arduino.close()
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Arduino Code(LED Control via Serial Input):

int ledPin = 13;  
char receivedChar;

void setup() {
    Serial.begin(9600);
    pinMode(ledPin, OUTPUT);
}

void loop() {
    if (Serial.available() > 0) {
        receivedChar = Serial.read();  // Read signal from Python

        if (receivedChar == '1') {
            digitalWrite(ledPin, HIGH);  // Turn LED ON
        } else if (receivedChar == '0') {
            digitalWrite(ledPin, LOW);   // Turn LED OFF
        }
    }
}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Wiring Diagram
Here’s how you should wire the LED:

(+) LED ---- [220Ω Resistor] ---- Pin 13 (Arduino)
(-) LED ---------------------- GND (Arduino)
---------------------------------------------------------------------------------------------------------------------------------
