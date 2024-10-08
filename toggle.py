from machine import Pin

# Initialize LED1 on GPIO 18 as an output pin
led1 = Pin(18, Pin.OUT)

# Initialize switch 5 on GPIO 22 as an input pin with a pull-down resistor
sw5 = Pin(22, Pin.IN, Pin.PULL_DOWN)

# Initialize LED2 on GPIO 20 as an output pin
led2 = Pin(20, Pin.OUT)

# Initialize switch 3 on GPIO 12 as an input pin with a pull-down resistor
sw3 = Pin(12, Pin.IN, Pin.PULL_DOWN)

# Infinite loop to constantly check the state of the switches and control the LEDs
while True:
    # Check if switch 5 is pressed (sw5.value() returns 1 when pressed)
    if sw5.value():
        # Turn on LED1
        led1.value(1)
        
    # Check if switch 3 is pressed (sw3.value() returns 1 when pressed)
    elif sw3.value():
        # Turn on LED2
        led2.value(1)
        
    # If neither switch is pressed, turn off both LEDs
    else:
        led1.value(0)
        led2.value(0)
