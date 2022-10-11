import machine
import utime

brightness = machine.ADC(26)
color = machine.ADC(27)

# conversion_factor = 3.3 / (65535)

while True:
#    voltage = potentiometer.read_u16() * conversion_factor
#    print(voltage)
    brightness_level = (brightness.read_u16() - 100) / 65535 * 100
    color_level = (color.read_u16() - 100) / 65535 * 100
    print(round(brightness_level))
    print(round(color_level))
    utime.sleep(2)
