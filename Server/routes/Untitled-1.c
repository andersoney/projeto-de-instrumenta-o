#include <SoftwareSerial.h>
#include <SimpleModbusMaster.h>
#define PIN_TEMP 0  // Setando Pino A0
#define PIN_PRESS 1 // Setando Pino A1
#define PIN_LED 12
float valAnalog = 0; // Iniciando variavel valAnalog como 0
float temp1 = 0;     // Iniciando variavel temp como 0
float pressao = 0;   // Iniciando variavel temp como 0

int x = 0;

// Pinos de comunicacao serial do modulo RS485
#define Pino_RS485_RX 10
#define Pino_RS485_TX 11
// Pino de controle transmissao/recepcao
#define SSerialTxControl 3
#define RS485Transmit HIGH
#define RS485Receive LOW
SoftwareSerial RS485Serial(Pino_RS485_RX, Pino_RS485_TX);
String inputString = "";
// Variavel de string completa
boolean stringComplete = false;
void initModuloRS485(){
    pinMode(SSerialTxControl, OUTPUT);
    digitalWrite(SSerialTxControl, LOW);
    RS485Serial.begin(4800);
}
void setup()
{
    Serial.begin(9600);
    initModuloRS485();
}
void piscaPisca(){
    digitalWrite(PIN_LED, HIGH);
    delay(1000);
    digitalWrite(PIN_LED, LOW);
    delay(1000);
}
void moduloRS485(){
    if (RS485Serial.available())
    {
        while (RS485Serial.available())
        {
            // Recebe os dados e monta a string
            char inChar = (char)RS485Serial.read();
            inputString += inChar;
            Serial.println("inputString");
            if (inChar == 'n')
            {
                // Mostra no Serial Monitor a string recebida
                Serial.print(inputString);
                stringComplete = true;
                inputString = "";
            }
        }
    }
}
void lerSensore(){
  valAnalog = analogRead(PIN_TEMP);
    temp1 = valAnalog;
    
    if (Serial.available() > 0)
    {
        String leitura = Serial.readString();
        if (leitura == "TP")
        {
            temp1 = analogRead(PIN_TEMP);
            pressao = 1023 - (1023 / 2) - analogRead(PIN_PRESS);
            Serial.println("#" + (String)++x + ":" + (String)temp1 + "*" + (String)pressao);
        }
        else if (leitura == "T")
        {
            temp1 = analogRead(PIN_TEMP);
            Serial.println("#" + (String)++x + ":" + (String)temp1);
            x = x + 1;
        }
        else if (leitura == "P")
        {
            pressao = 1023 - 1023 / 2 - analogRead(PIN_PRESS);
            Serial.println("#" + (String)++x + ":" + (String)pressao);
            x = x + 1;
        }
        else
        {
            Serial.println("Vazio");
        }
    }
}
void lerSensoresOnly(){
  temp1 = analogRead(PIN_TEMP);
  pressao = 1023 - (1023 / 2) - analogRead(PIN_PRESS);
  Serial.println("#" + (String)++x + ":" + (String)temp1 + "*" + (String)pressao);
}
void loop()
{
    piscaPisca();
    // moduloRS485();
    lerSensoresOnly();
}