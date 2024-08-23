#define UART_BAUD_RATE 115200
#define UART_TX_PIN 1  
#define UART_RX_PIN 3 

const int fsrPin = 0; 
const int R_fixed = 10000;  // 10k ohms pull-down resistor
const float V_in = 3.0;   

void setup() {
  Serial.begin(UART_BAUD_RATE, SERIAL_8N1, UART_RX_PIN, UART_TX_PIN);
  
  while(!Serial) { ; }

}

void loop() {
  int fsrValue = analogRead(fsrPin);

  float V_out = (fsrValue / 4095.0) * V_in;
  float R_fsr = R_fixed * (V_in / V_out - 1);
  //Serial.println(R_fsr);
  
  
  uint16_t compressedValue = fsrValue & 0xFFF;
  
  
  uint8_t highByte = (compressedValue >> 8) & 0xFF;
  uint8_t lowByte = compressedValue & 0xFF;
  
  Serial.write(highByte);
  Serial.write(lowByte);
  
  delay(100);
}
