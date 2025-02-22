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
