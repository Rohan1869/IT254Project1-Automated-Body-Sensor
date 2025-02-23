# Arduino Code (LED Control via Serial).cpp

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
