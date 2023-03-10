import grovepi
import time

ultrasonic_ranger_pin = 2
rotary_angle_sensor_pin = 0

lcd_screen_pin = 2
lcd_screen_columns = 16

grovepi.pinMode(lcd_screen_pin,"OUTPUT")
grovepi.pinMode(lcd_screen_pin+1,"OUTPUT")
grovepi.pinMode(lcd_screen_pin+2,"OUTPUT")
lcd_screen = grovepi.new_lcd_screen(lcd_screen_pin,lcd_screen_columns)

threshold_distance = 50
rotary_angle_sensor_max = 1023
rotary_angle_sensor_min = 0

ultrasonic_ranger_max = 517
ultrasonic_ranger_min = 0

while True:
    rotary_angle_sensor_value = grovepi.analogRead(rotary_angle_sensor_pin)
    threshold_value = int((rotary_angle_sensor_value - rotary_angle_sensor_min) / (rotary_angle_sensor_max - rotary_angle_sensor_min) * threshold_distance)
    
    ultrasonic_ranger_value = grovepi.ultrasonicRead(ultrasonic_ranger_pin)
    ultrasonic_ranger_value_mapped = int((ultrasonic_ranger_value - ultrasonic_ranger_min) / (ultrasonic_ranger_max - ultrasonic_ranger_min) * 100)
    
    grovepi.setText_norefresh(lcd_screen, "Threshold: " + str(threshold_distance) + " ")
    
    if ultrasonic_ranger_value < threshold_value:
        grovepi.setText_norefresh(lcd_screen, "OBJ PRES", 1, 10)
        
    grovepi.setText_norefresh(lcd_screen, str(ultrasonic_ranger_value_mapped) + "%", 2, 0)
    
    time.sleep(0.1)
