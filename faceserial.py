# Python Script (Face Detection & Serial Communication)

import cv2
import serial
import time
import numpy as np
import h5py
from tensorflow import keras
from tensorflow.keras.optimizers import Adam
from PIL import Image, ImageOps


# Load Teachable Machine model
MODEL_PATH = "keras_model.h5"

# Code to ignore groups from the config
f = h5py.File("keras_model.h5", mode="r+")
model_config_string = f.attrs.get("model_config")

if model_config_string.find('"groups": 1,') != -1:
    model_config_string = model_config_string.replace('"groups": 1,', '')

f.attrs.modify('model_config', model_config_string)
f.flush()

model_config_string = f.attrs.get("model_config")
assert model_config_string.find('"groups": 1,') == -1

# Load model
my_model = keras.models.load_model("./keras_model.h5",compile=False)

# Load label
load_label = open("labels.txt", "r").readlines()

# Initialize Serial Communication with Arduino
arduino = serial.Serial('COM3', 9600)

# Open webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Camera Feed", frame)

# Resize the frame
    size = (224, 224)
    image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

    # Normalize the image
    image_array = np.asarray(image)
    normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

    # Load the image into the array
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    data[0] = normalized_image_array
    prediction = my_model.predict(data)
    index = np.argmax(prediction)
    class_name = load_label[index].strip()
    confidence_score = prediction[0][index]
    if class_name == 0:
        print("No face detected")
        arduino.write(f"{class_name}\n".encode())
        time.sleep(0.05)
    else:
        print("face detected")
        arduino.write(f"{class_name}\n".encode())
        time.sleep(0.05)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

#Turn off LED
arduino.write(f"0\n".encode())
arduino.close()
