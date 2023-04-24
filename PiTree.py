import RPi.GPIO as GPIO
import time

# Set up GPIO pins
GPIO.setmode(GPIO.BCM)

# Assign pins to LEDS and buttons
stop_red = 3
pre_staging_white = 5
stage_orange_1 = 7
stage_orange_2 = 8
stage_yellow_3 = 10
stage_yellow_2 = 11
stage_yellow_1 = 12
start_green = 13
buzzer = 15
button_racer_1 = 16
button_racer_2 = 18
button_official = 19

# Set up GPIO pins
GPIO.setup(stop_red, GPIO.OUT)
GPIO.setup(pre_staging_white, GPIO.OUT)
GPIO.setup(stage_orange_1, GPIO.OUT)
GPIO.setup(stage_orange_2, GPIO.OUT)
GPIO.setup(stage_yellow_3, GPIO.OUT)
GPIO.setup(stage_yellow_2, GPIO.OUT)
GPIO.setup(stage_yellow_1, GPIO.OUT)
GPIO.setup(start_green, GPIO.OUT)
GPIO.setup(buzzer, GPIO.OUT)
GPIO.setup(button_racer_1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_racer_2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(button_official, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Turn on pre-staging and stop LEDs
GPIO.output(pre_staging_white, GPIO.HIGH)
GPIO.output(stop_red, GPIO.HIGH)

# Wait for either button 1 or 2 to be pressed
while True:
    if GPIO.input(button_racer_1) == GPIO.LOW:
        GPIO.output(stage_orange_1, GPIO.HIGH)
        break
    elif GPIO.input(button_racer_2) == GPIO.LOW:
        GPIO.output(stage_orange_2, GPIO.HIGH)
        break

# Wait for button 3 to be pressed and both staging LEDs to be on
while True:
    if GPIO.input(button_official) == GPIO.LOW and GPIO.input(stage_orange_1) == GPIO.HIGH and GPIO.input(stage_orange_2) == GPIO.HIGH:
        break

# Countdown timer
for stage in [stage_yellow_3, stage_yellow_2, stage_yellow_1, start_green]:
    # Turn on the stage LED
    GPIO.output(stage, GPIO.HIGH)

    # Play buzzer for half a second on stage 3, 2, and 1
    if stage in [stage_yellow_3, stage_yellow_2, stage_yellow_1]:
        GPIO.output(buzzer, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(buzzer, GPIO.LOW)

    # Wait for 1 second before proceeding to the next stage
    time.sleep(1)

# Reset the process
GPIO.output(stop_red, GPIO.HIGH)
GPIO.output(pre_staging_white, GPIO.HIGH)
GPIO.output(stage_orange_1, GPIO.LOW)
GPIO.output(stage_orange_2, GPIO.LOW)
GPIO.output(stage_yellow_3, GPIO.LOW)
GPIO.output(stage_yellow_2, GPIO.LOW)
GPIO.output(stage_yellow_1, GPIO.LOW)
GPIO.output(start_green, GPIO.LOW)
GPIO.output(buzzer, GPIO.LOW)
