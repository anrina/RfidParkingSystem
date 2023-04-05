# Rfid Parking System
Hardware part of the parking system


The hardware part

**1.aMG FiO Glide ESP32**

<img width="494" alt="Screen Shot 2566-04-05 at 19 32 47" src="https://user-images.githubusercontent.com/46740049/230081616-dc08ad9c-2632-4632-a77e-de1e39473997.png">

<img width="489" alt="Screen Shot 2566-04-05 at 20 23 44" src="https://user-images.githubusercontent.com/46740049/230093945-e4d8fe66-0b20-4fe6-b96e-56b12cfc4628.png">

Dtasheet:https://www.aimagin.com/en/productattachment/file/download/id/MC43OTMxODQwMCAxNjIzMDU3NDE0/params/eyJjdXN0b21lcl9pZCI6IjYyIiwiaXAiOiIyMDMuMTMxLjIxNi4xMSIsImNpdHkiOiJLaGxvbmcgTHVhbmciLCJjb3VudHJ5IjoiVEgifQ==

**2.Adafruit PN532 RFID/NFC Breakout and Shield**

<img width="400" alt="Screen Shot 2566-04-05 at 19 40 21" src="https://user-images.githubusercontent.com/46740049/230083134-e0775f34-f39f-4ece-a548-e44de8573cb6.png">

It support SPI, I2C and TX/RX we can place the jumper to choose the mode.

Datasheet:https://cdn-learn.adafruit.com/downloads/pdf/adafruit-pn532-rfid-nfc.pdf

Youtube:https://www.youtube.com/watch?v=2qf6gIqhWNA


The code for find is you connect I2C correctly is in findi2c folder and the code for find type of the card is in readMifareture.
The code that use to read card (Classic) in our project is Project_readMifareClassic.


Pin connect

PN532           aMG FiO Glide ESP32

GND         --> GND

SSEL/SCL/RX --> pin 15

MOSI/SDA/TX --> pin 13

MISO        --> pin 12

SCK         --> pin 14

3.3 v       --> pin 3.3 v
