import grovepi
import time
from grove_rgb_lcd import *

ultrasonic_ranger = 2
rotary_angle_sensor = 0
lcd_port = 1

setRGB(0,255,0)

threshold = grovepi.analogRead(rotary_angle_sensor)
distance = grovepi.ultrasonicRead(ultrasonic_ranger)

while True:
	new_threshold = grovepi.analogRead(rotary_angle_sensor)
	new_distance = grovepi.ultrasonicRead(ultrasonic_ranger)

	obj_pres = "OBJ PRES" if grovepi.ultrasonicRead(ultrasonic_ranger) < threshold else ""
	if obj_pres:
		setRGB(255,0,0)
		setText_norefresh(str(threshold) + "cm " + obj_pres)
	else:
		setRGB(0,255,0)

	if new_threshold != threshold:
		threshold = new_threshold
		setText_norefresh(str(threshold) + "cm ")

	if new_distance != distance:
		distance = new_distance
		setText_norefresh("\n" + str(distance) + "cm")

	time.sleep(0.01)
