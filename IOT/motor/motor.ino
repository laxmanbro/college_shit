float temp; 
int tempPin = A0; //arduino pin used for temperature sensor
int tempMin = 15;   // the temperature to start the buzzer
int tempMax = 70;   
int fan = 6;       // the pin where fan is connected
int fanSpeed = 0;

void setup() {
 pinMode(fan, OUTPUT);
 pinMode(tempPin, INPUT);
 Serial.begin(9600);
}
void loop() {
  temp = analogRead(tempPin);
  temp = (temp *5.0*100.0)/1024.0; 
  Serial.println(temp);
  delay(1000);        // delay in between reads for stability
  if(temp < tempMin) {   // if temp is lower than minimum temp
       fanSpeed = 0;      // fan is not spinning
       digitalWrite(fan, LOW);
   } 
   if((temp >= tempMin) && (temp <= tempMax))  //if temperature is higher than the minimmum range
   { 
       fanSpeed = map(temp, tempMin, tempMax, 100, 255); // the actual speed of fan
       analogWrite(fan, fanSpeed);  // spin the fan at the fanSpeed speed
       Serial.println(fanSpeed);
   } 
}
