import time
import machine
import onewire
import ds18x20
import json

# Read configuration from config.json
temp_config = open('config.json')
config = json.load(temp_config)

# Specify the GPIO pin to which the sensor is connected
dat = machine.Pin(config['pin'])

# Create a onewire object
ds = ds18x20.DS18X20(onewire.OneWire(dat))

# Scan for devices on the bus
roms = ds.scan()

# Set the device ID as a string 
unit_id_str = '(B\x05\xefO \x01\xf5'

# Convert the device ID from a string to a bytearray
byte_array = bytearray(unit_id_str, 'utf-8')

# Convert the bytearray to hexadecimal representation
hex_id = ''.join(['{:02x}'.format(byte) for byte in byte_array])

# Loop and print temperature, unit_ID, and sensor_ID 
while True:
    # Trigger temperature conversion and wait
    ds.convert_temp()
    time.sleep_ms(config['interval'])
    
    for rom in roms:
        # Convert ROM to hexadecimal representation
        roms2 = hex(int.from_bytes(rom, 'little'))

        # Print the unit_ID, sensor_ID, and temperature
        print(hex_id, roms2[2:], end='')
        print('', ds.read_temp(rom), end=' ')
    print() # End the line for the next iteration
