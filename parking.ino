#define ir1 8
#define ir2 9
#define ir3 10
#define ir4 19
#include <SoftwareSerial.h>

SoftwareSerial mySerial(6, 7);

void setup() {
  // put your setup code here, to run once:
Serial.begin(9600);
pinMode(ir1,INPUT);
pinMode(ir2,INPUT);
pinMode(ir3,INPUT);
pinMode(ir4,INPUT);
mySerial.begin(9600);
}
int a=0,b=0,c=0,d=0;
void loop() {
  // put your main code here, to run repeatedly:
if((digitalRead(ir1)==LOW)&& a==0)
{

    a=1;
  Serial.print("A");
  mySerial.print("$A#");
}
else if((digitalRead(ir1)==HIGH) && a==1)
{
  a=0;
  mySerial.print("$E#");
}

if((digitalRead(ir2)==LOW)&&b==0)
{

    b=1;
  Serial.print("B");
    mySerial.print("$B#"); 
   
}
else if((digitalRead(ir2)==HIGH) && b==1)
{
  b=0;
  mySerial.print("$F#");
}
if((digitalRead(ir3)==LOW) && c==0)
{
    c=1;
  Serial.print("C");
    mySerial.print("$C#");
}
else if((digitalRead(ir3)==HIGH) && c==1)
{
  c=0;
mySerial.print("$G#");
}
if((digitalRead(ir4)==LOW)&& d==0)
{
    d=1;
  Serial.print("D");
    mySerial.print("$D#");
 
}
else if((digitalRead(ir4)==HIGH) && d==1)
{
  d=0;
  mySerial.print("$H#");
}
}
