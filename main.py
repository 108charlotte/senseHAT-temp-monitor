from sense_hat import SenseHat
import time

sense = SenseHat()

def get_cpu_temperature(): 
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        temp = f.read()
    return float(temp) / 1000.0

def get_color_from_temperature(temp):
    if temp < 55:
        return (0, 255, 0) # green
    elif temp < 64:
        return (255, 255, 0)  # yellow
    elif temp < 74:
        return (255, 165, 0)  # orange
    else:
        return (255, 0, 0)  # red

while True: 
    cpu_temp = get_cpu_temperature()
    sense.clear(get_color_from_temperature(cpu_temp))
    time.sleep(2)