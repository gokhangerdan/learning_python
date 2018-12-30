const int analogInPin = A0;
const int analogInPin2 = A1;

int sensorValue = 0;
int sensorValue2 = 0;

void setup() {
  Serial.begin(9600);
}

void loop() {
  sensorValue = analogRead(analogInPin);
  sensorValue2 = analogRead(analogInPin2);

  Serial.print("val1=");
  Serial.print(sensorValue);
  Serial.print("-");
  Serial.print("val2=");
  Serial.print(sensorValue2);
  Serial.print("\n");

  delay(1000);
}