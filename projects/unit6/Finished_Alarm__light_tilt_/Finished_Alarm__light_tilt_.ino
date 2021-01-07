//experimentally set sensor threshold values
#define lightThreshold 100
#define tiltSwitchActive 1
#define motionDetected 1
//pin definitions
#define photoDetectorPin A0
#define buzzerPin 9
#define tiltSwitchPin 2  
#define motionPin 8 //with LDR (light decreasing resistor/light dependant resistor so works in dark) 
void setup() {
  //===== start Serial 
  Serial.begin(9600);
  //===== initiate all I/O
  pinMode(photoDetectorPin, INPUT);
  pinMode(tiltSwitchPin, INPUT_PULLUP);
  pinMode(buzzerPin, OUTPUT);  
  pinMode(motionPin,INPUT);
}
void loop() {
 bool light = lightSensor();
 bool tilt  = tiltSwitch(); 
 bool motion = motionSensor();
  if(  light==1 || tilt==1 || motion==1 )
  {  
    digitalWrite(buzzerPin, HIGH);
    Serial.println("buzzer on");
  } 
  else 
  {
    digitalWrite(buzzerPin, LOW);
    Serial.println("buzzer off");
  }
  delay(50);
}
//======================================
//  custom functions for each sensor
//======================================
bool lightSensor(){ 
  //read the sensor
  int val = analogRead(photoDetectorPin);
  //print the value
  Serial.print(val);
  Serial.print("        ");
  //reductive logic to return a boolean
  if ( val >= lightThreshold){
    return true;  //return true if 'tripped'
  }else{
    return false; //return false if not 'tripped'
  }
}
//======================================
bool tiltSwitch(){
  //read the sensor
  bool val = digitalRead(tiltSwitchPin);
  //print the value
  Serial.print(val);
  Serial.print("        ");
  //reductive logic to return a boolean
  if(val == tiltSwitchActive){ //this may seem unnecessary, but it helps incase the logic is inverted...
    return true;
  }else{
    return false;
  }}
  //===================================
  bool motionSensor(){
  //read the sensor
  bool val = digitalRead(motionPin);
  //print the value
  Serial.print(val);
  Serial.print("        ");
  //reductive logic to return a boolean
  if(val == motionDetected){ //this may seem unnecessary, but it helps incase the logic is inverted...
    return true;
  }else{
    return false;
  }
}
