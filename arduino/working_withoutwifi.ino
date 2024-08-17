#include <WiFi.h>  // Optional: Keep this if you plan to use WiFi later

const int fsrPin = 0;  // Analog pin connected to FSR402

void setup() {
  Serial.begin(115200);

  // WiFi.begin(ssid, password);  // Commented out for testing without WiFi

  // while (WiFi.status() != WL_CONNECTED) {  // Commented out for testing without WiFi
  //   delay(500);
  //   Serial.println("Connecting to WiFi...");
  // }

  // Serial.println("Connected to WiFi");  // Commented out for testing without WiFi
}

void loop() {
  int fsrValue = analogRead(fsrPin);
  Serial.println(fsrValue);
  
  // Compress fsrValue to fit in 12 bits (0-4095 range)
  int compressedValue = fsrValue & 0xFFF;  // Keep only the lower 12 bits

  // The following lines are commented out to disable WiFi connection and data sending
  // if (!client.connected()) {
  //   if (client.connect(host, port)) {
  //     Serial.println("Connected to server");
  //   } else {
  //     Serial.println("Failed to connect to server");
  //     delay(1000);
  //     return;
  //   }
  // }

  // Convert the compressed value to a 2-byte array
  uint8_t data[2];
  data[0] = (compressedValue >> 8) & 0xFF;  // High byte
  data[1] = compressedValue & 0xFF;         // Low byte

  // Commented out to disable data sending
  // client.write(data, 2);

  delay(1000);  // Adjust delay as necessary, set to 1 second for sensor readings
}

