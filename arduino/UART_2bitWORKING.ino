#define UART_BAUD_RATE 115200
#define UART_TX_PIN 1  
#define UART_RX_PIN 3 

const int fsrPin = 0; 

void setup() {
  Serial.begin(UART_BAUD_RATE, SERIAL_8N1, UART_RX_PIN, UART_TX_PIN);
  
  while(!Serial) { ; }

}

void loop() {
  int fsrValue = analogRead(fsrPin);
  
  
  uint16_t compressedValue = fsrValue & 0xFFF;
  
  
  uint8_t highByte = (compressedValue >> 8) & 0xFF;
  uint8_t lowByte = compressedValue & 0xFF;
  
  Serial.write(highByte);
  Serial.write(lowByte);
  
  delay(1000);
}
