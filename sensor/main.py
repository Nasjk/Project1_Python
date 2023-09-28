import time
import machine
import onewire
import ds18x20
import json

# Läs in konfiguration från config.json
temp_config = open('config.json')
config = json.load(temp_config)

# Ange vilket GPIO-stift sensorn är ansluten till 
dat = machine.Pin(config['pin'])

# Skapa en onewire-objekt
ds = ds18x20.DS18X20(onewire.OneWire(dat))

# Skanna efter enheter på bussen
roms = ds.scan()
print('Hittade enheter:', roms)

# Ange enhets-ID som en sträng
unit_id_str = '(B\x05\xefO \x01\xf5'

# Konvertera enhets-ID från sträng till en bytearray
byte_array = bytearray(unit_id_str, 'utf-8')

# Konvertera bytearray till hexadecimal representation
hex_id = ''.join(['{:02x}'.format(byte) for byte in byte_array])

# Loopa och skriv ut temperaturen, unit_ID och sensor_ID i all evighet
while True:
    ds.convert_temp()
    time.sleep_ms(config['interval'])
    for rom in roms:
        roms2 = hex(int.from_bytes(rom, 'little'))
        print(hex_id, roms2[2:], end='')
        print('', ds.read_temp(rom), end=' ')
    print()

