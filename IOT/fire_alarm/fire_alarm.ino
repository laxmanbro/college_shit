void setup()
{
  Serial.begin(9600);
}
void loop()
{
int rawvoltage= analogRead(0);
float temp= (rawvoltage/1024.0) * 5000 /10;
  if(temp>31)
  {
  t();
  }
  else 
  {
  if(temp>29)
  {
   t1();
  }
  if(temp<29);
  {
  noTone(7);
  }
}
Serial.println(temp);
}
void t()
{
tone(7, 494, 500);
delay(1000);
}
void t1()
{
  tone(7, 2000, 500);
  delay(2000);
}  
