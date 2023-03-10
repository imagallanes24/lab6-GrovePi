import grovepi
import time

ultrasonic_ranger_pin = 2
rotary_angle_sensor_pin = 0

grovepi.pinMode(ultrasonic_ranger_port, "INPUT")
grovepi.pinMode(rotary_angle_sensor_port, "INPUT")

threshold = 512


threshold_distance = 50
rotary_angle_sensor_max = 1023
rotary_angle_sensor_min = 0

while True:
    threshold_raw = grovepi.analogRead(rotary_angle_sensor_port)
    threshold = int(rotary_value / 1023.0 * 517)
    distance = grovepi.ultrasonicRead(ultrasonic_ranger_port)
    object_present = distance < threshold

    lcd_top_line = str(threshold)
    if object_present:
        lcd_top_line += " OBJ PRES"
    lcd_bottom_line = str(distance)

    setText_norefresh(lcd_top_line + "\n" + lcd_bottom_line)