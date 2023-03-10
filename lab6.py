import grovepi
import grove_rgb_lcd

ultrasonic_ranger_port = 2
rotary_angle_sensor_port = 0

grovepi.pinMode(ultrasonic_ranger_port, "INPUT")

threshold_min = 0
threshold_max = 1023

grove_rgb_lcd.setRGB(255, 255, 255)
grove_rgb_lcd.setText("Threshold: ", "")

while True:
  threshold_raw = grovepi.analogRead(rotary_angle_sensor_port)
  threshold = int(grovepi.map(threshold_raw, 0, 1023, threshold_min, threshold_max))
  distance = grovepi.ultrasonicRead(ultrasonic_ranger_port)
  object_present = distance < threshold
  
  top_line = f"Threshold: {threshold}"
  if object_present:
    top_line += " OBJ PRES"
  bottom_line = f"Distance: {distance}"
  grove_rgb_lcd.setText(top_line, bottom_line)
  
  grovepi.delay(50)
