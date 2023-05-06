#include <cvzone.h>

SerialData seriaIData(2, 1); //(numOfVaIsRec,digitsPerValRec)
int vaIsRec[2]; // array of int with size numOfValsRec

void setup() ( 
pinMode(13, OUTPUT); 
pinMode(12, OUTPUT);
seriaIData.begin();
}

void loop() {
serialData.Get(valsRec);
digitaIWrite(13, vaIsRec[0]); //white led
digitaIWrite(12, vaIsRec[1]); // red led 
delay(10);
}
