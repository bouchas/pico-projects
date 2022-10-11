import machine
import utime
from neopixel import Neopixel

red = (255, 0, 0)
orange = (255, 165, 0)
yellow = (255, 150, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (75, 0, 130)
violet = (138, 43, 226)
colors = (red, orange, yellow, green, blue, indigo, violet)

brightness = machine.ADC(26)
color = machine.ADC(27)

numpix = 30
strip = Neopixel(numpix, 0, 28, "GRB")
strip.clear()
strip.show()

voltage_factor = 3.3 / (65535)
brightness_factor = 255 / (65535)
color_factor = (len(colors)-1) / (65535)

onboard_led = machine.Pin(25, machine.Pin.OUT)
onboard_led.value(0)

external_led = machine.Pin(15, machine.Pin.OUT)
external_led.value(0)

def mycallback(t):
    print('mycallback')
    timer2.deinit()
    external_led.value(0)

def mycallback2(t):
    if (Shutdown_Strip == 0):
        print('mycallback2')
        brightness_value = brightness.read_u16() * brightness_factor
        color_value = round(color.read_u16() * color_factor)
    #     print('Brightness: %s' % brightness_value)
    #     print(color_value)
    #     print(round(color_value))
    #     print(colors[color_value-1])
        strip.brightness(brightness_value)
        strip.fill(colors[round(color_value)])
        strip.show()

def mycallback3(t):
    print('mycallback3')
    Shutdown_Strip = 1
    timer2.deinit()
    external_led.value(0)
    timer.deinit()
    strip.clear()
    strip.show()


def Pb_Switch_INT(pin):         # PB_Switch Interrupt handler
    global Pb_Switch_State      # reference the global variable
    global Shutdown_Strip
    global timer
    global timer2
    global timer3
    
    Shutdown_Strip = 0
    Pb_Switch.irq(handler = None) # Turn off the handler while it is executing

    if (Pb_Switch.value() == 1) and (Pb_Switch_State == 0):  # Pb_Switch is active (High) and Pb_Switch State is currently Low
        Pb_Switch_State = 1     # Update current state of switch
        onboard_led.value(1)    # Do required action here
        external_led.value(1)
        timer=machine.Timer(period=5000, mode=machine.Timer.ONE_SHOT, callback=mycallback)
        timer2=machine.Timer(period=100, mode=machine.Timer.PERIODIC, callback=mycallback2)
        timer3=machine.Timer(period=2000, mode=machine.Timer.ONE_SHOT, callback=mycallback3)
        print("ON")             # Do required action here

    elif (Pb_Switch.value() == 0) and (Pb_Switch_State == 1): # Pb_Switch is not-active (Low) and Pb_Switch State is currently High
        Pb_Switch_State = 0     # Update current state of switch
        onboard_led.value(0)    # Do required action here
        print("OFF \n")         # Do required action here
        timer3.deinit()

    Pb_Switch.irq(handler = Pb_Switch_INT)


#Creat an 'object' for our Pb_Switch change of state
# Pb_Switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
Pb_Switch = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_DOWN)
#Setup the Interrupt Request Handling for Pb_Switch change of state
Pb_Switch.irq(trigger = machine.Pin.IRQ_RISING | machine.Pin.IRQ_FALLING, handler = Pb_Switch_INT)

#Preset the STATE variable for the Pb_Switch
Pb_Switch_State = Pb_Switch.value()
print("Pb_Switch State=", Pb_Switch_State)

Shutdown_Strip = 0

while True:
    utime.sleep(.0001)
