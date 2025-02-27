# IT254Project1-Automated-Body-Sensor
This project integrates an Arduino Mega 2560, Google Teachable Machine, and Python to create a face-detection-based security system which can also serve as a body sensor for multitude of reasons. When the system detects a face, it triggers an LED on the Arduino board using Serial Communication.
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

FILE INFO:

arduionoledcontrolserial.cpp ---> The code for the Arduino for LED control.

faceserial.py ---> The Python code which reads webcam input and runs it through the teachable model(Sends 0 to Arduino if face is detected otherwise 1. pressing "q" shuts it down).

labels.txt ------> contains data for model determination categories.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------



Requirements/Materials:







HARDWARE:

Arduino Mega 2560 – The microcontroller to process serial data.

LED + 220Ω Resistor – Used for visual indication.

USB Cable – To connect the Arduino to the PC.

Webcam – Used for real-time face detection.




Software & Libraries:

Python – Runs the AI model and processes webcam data.

TensorFlow.js – Loads the trained model.

OpenCV – Captures and processes images from the webcam.

PySerial – Enables communication between Python and Arduino.

Arduino IDE – To upload code to the Arduino Mega 2560.

---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Installation & Setup:

Step 1: Install Required Python Libraries

Open a terminal and run: pip install tensorflow==2.16.1  opencv-python pyserial numpy Pillow hypy



(python version is 3.12.9)

Step 2: Load the Teachable Machine Model

Export your Teachable Machine Image Model in TensorFlow.js format.

Extract and place it in the project folder.

Step 3: Connect the LED to Arduino

Component----------Arduino Pin

LED (Anode +)----> Pin 9 then connect to one end of 220Ω resistor

LED (Cathode -)------>breadboard connected to one resistor end

RESISTOR: then connect the other resistor end to GND of Arduino

![image](https://github.com/user-attachments/assets/fe7a7077-179a-42e6-925d-a3c6e0fd93fc)


---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Running the Project:

1. Upload the Arduino Code
Open Arduino IDE.
Select Tools → Board → Arduino Mega 2560.
Select the correct COM Port.
Copy & paste the Arduino Code above.
Click Upload.

2. Run the Python Script
Open Command Prompt or Terminal.
Navigate to the script directory: cd path/to/your/script

Run the script: python your_script.py


3. Test the System
If a face is detected, the LED turns ON.
If no face is detected, the LED stays OFF.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------

VERSIONS USED:

Python: 3.12.9
TensorFlow: 2.16.1
Keras: Latest
OpenCV: 4.11.0.86
PySerial: 3.5
Pillow: 11.1.0
Arduino IDE: Latest
Hardware: Arduino Mega 2560

-------------------------------------------------------------------------------------------------------------------------------------------------------------------


ENJOY!!!!!




![image](https://github.com/user-attachments/assets/c152e881-0a17-4b33-a061-76b95753e0c9)















