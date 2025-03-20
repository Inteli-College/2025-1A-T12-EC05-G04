from machine import Pin, ADC
import utime


sensor_pin = ADC(Pin(27))

while True:
    # Read the sensor value
    sensor_value = sensor_pin.read_u16()

    # Print the sensor value to serial
    print("TCRT5000 sensor reading:", sensor_value)

    # Wait for 500 milliseconds
    utime.sleep(0.5)
