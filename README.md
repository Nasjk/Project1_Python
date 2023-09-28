# Project1_Python

Begin by downloading the program Thonny from https://thonny.org/.
Connect your Raspberry Pi Pico to Thonny while selecting the appropriate COM port.

Find or write a test code to try out the sensor, I used:
https://docs.micropython.org/en/latest/esp8266/tutorial/onewire.html. 
Choose the correct GPIO and proceed to test the sensor.

#Usage
Power on the Raspberry Pi Pico
The Raspberry Pi Pico will read temperature data from the DS18B20 sensor based on the configuration in config.json.
Temperature data is transmitted via UART to the Raspberry Pi Pico.
The Raspberry Pi Pico receives and processes the data 

#Installation
Raspberry Pi Pico Setup:

Connect the DS18B20 temperature sensor to the Raspberry Pi Pico.
Flash the MicroPython firmware onto the Raspberry Pi Pico using Thonny IDE.
Upload the MicroPython script to the Raspberry Pi Pico.

Connect the Raspberry Pi Zero to the Raspberry Pi Pico via UART (USB-to-Serial cable).
Upload the Python script to the Raspberry Pi Zero.
Customize the config.json file to match the sender's configuration.


Libraries: 
time
machine
onewire
ds18x20
json

Materials:
Raspberry Pi Pico
USB
Temperature Sensor

