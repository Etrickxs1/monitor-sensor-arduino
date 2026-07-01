void setup() {
    pinMode(13, OUTPUT);
    Serial.begin(9600);
}

void loop() {
    int valor = 1023 - analogRead(A0);
    Serial.println(valor);
    delay(200);
    
    if (Serial.available() > 0) {
        char comando = Serial.read();
        if (comando == '1') {
            digitalWrite(13, HIGH);
            Serial.println("LED encendido");
        }
        else if (comando == '0') {
            digitalWrite(13, LOW);
            Serial.println("LED apagado");
        }
    }
}