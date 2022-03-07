int pinoTempA0 = 0;    //Setando Pino A0
int pinoTempA1 = 0;    //Setando Pino A0
float valAnalog = 0;    // Iniciando variavel valAnalog como 0
float temp1 = 0;        //Iniciando variavel temp como 0
float temp2 = 0;        //Iniciando variavel temp como 0
#define PIN 12
int x=0;
void setup(){
    Serial.begin(9600);
    pinMode(PIN,OUTPUT);
}
 
void loop(){
  valAnalog = analogRead(pinoTempA0);
  temp1 = valAnalog;
  digitalWrite(PIN,HIGH);
  delay(1000);
  digitalWrite(PIN,LOW);
  delay(1000);
  if (Serial.available() > 0){
    if (Serial.readString() == "tp"){
      temp1 = analogRead(pinoTempA0);
      temp2 = analogRead(pinoTempA1);
      Serial.println("#"+(String)++x+":"+(String)temp1+"-"+(String)temp1);
    }else if (Serial.readString() == "t"){
      
    }else if (Serial.readString() == "t"){ // letra t
          temp1 = analogRead(pinoTempA0);
          temp2 = analogRead(pinoTempA1);
          Serial.println("#"+(String)++x+":"+(String)temp1+"-"+(String)temp1);
          x=x+1;
      }else{
        Serial.println("Vazio");
      }
  }
}