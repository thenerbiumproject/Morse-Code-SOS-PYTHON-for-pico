from machine import Pin
import utime
led = Pin(25,Pin.OUT)
first_sos = 3.0
second_sos = 0.2
third_sos = 3.0

while True:
    led.high()
    utime.sleep(first_sos)
    led.low()
    utime.sleep(first_sos)
    led.high()
    utime.sleep(first_sos)
    led.low()
    utime.sleep(first_sos)
    led.high()
    utime.sleep(first_sos)
    led.low()
    utime.sleep(first_sos)
    led.high()
    utime.sleep(second_sos)
    led.low()
    utime.sleep(second_sos)
    led.high()
    utime.sleep(second_sos)
    led.low()
    utime.sleep(second_sos)
    led.high()
    utime.sleep(second_sos)
    led.low()
    utime.sleep(second_sos)
    led.high()
    utime.sleep(third_sos)
    led.low()
    utime.sleep(third_sos)
    led.high()
    utime.sleep(third_sos)
    led.low()
    utime.sleep(third_sos)
    led.high()
    utime.sleep(third_sos)
    led.low()
    utime.sleep(third_sos)
    utime.sleep()
    
    