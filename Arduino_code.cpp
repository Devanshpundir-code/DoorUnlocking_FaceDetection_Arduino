#define IN1 8  
#define IN2 9  

int receivedData = 0;

void setup() {
    Serial.begin(9600);
    pinMode(IN1, OUTPUT);
    pinMode(IN2, OUTPUT);

    digitalWrite(IN1, LOW);
    digitalWrite(IN2, LOW);  
}

void loop() {
    if (Serial.available() > 0) {
        receivedData = Serial.read();  

        if (receivedData == '1') {  
            Serial.println("Unlocking Door...");
            digitalWrite(IN1, HIGH);
            digitalWrite(IN2, LOW);  
            
            delay(3000);  

            digitalWrite(IN1, LOW);
            digitalWrite(IN2, LOW);  

            delay(10000);  

            Serial.println("Locking Door...");
            digitalWrite(IN1, LOW);
            digitalWrite(IN2, HIGH);  

            delay(3000);  

            digitalWrite(IN1, LOW);
            digitalWrite(IN2, LOW);  
        }
    }
}
