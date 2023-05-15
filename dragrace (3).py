import machine
import utime

# Assign pins to variables
stop_1_pin = machine.Pin(0, machine.Pin.OUT)
stop_2_pin = machine.Pin(1, machine.Pin.OUT)
prestage_1_pin = machine.Pin(2, machine.Pin.OUT)
prestage_2_pin = machine.Pin(3, machine.Pin.OUT)
racer_1_pin = machine.Pin(4, machine.Pin.OUT)
racer_2_pin = machine.Pin(5, machine.Pin.OUT)
stage_3_1_pin = machine.Pin(6, machine.Pin.OUT)
stage_3_2_pin = machine.Pin(7, machine.Pin.OUT)
stage_2_1_pin = machine.Pin(8, machine.Pin.OUT)
stage_2_2_pin = machine.Pin(9, machine.Pin.OUT)
stage_1_1_pin = machine.Pin(10, machine.Pin.OUT)
stage_1_2_pin = machine.Pin(11, machine.Pin.OUT)
start_1_pin = machine.Pin(12, machine.Pin.OUT)
start_2_pin = machine.Pin(13, machine.Pin.OUT)

button_1_pin = machine.Pin(14, machine.Pin.IN, machine.Pin.PULL_UP)
button_2_pin = machine.Pin(15, machine.Pin.IN, machine.Pin.PULL_UP)
start_button_pin = machine.Pin(17, machine.Pin.IN, machine.Pin.PULL_UP)
buzzer_pin = machine.Pin(20, machine.Pin.OUT)

#LEDs off 
racer_1_pin.off()
racer_2_pin.off()
stage_3_1_pin.off()
stage_3_2_pin.off()
stage_2_1_pin.off()
stage_2_2_pin.off()
stage_1_1_pin.off()
stage_1_2_pin.off()
start_1_pin.off()
start_2_pin.off()
print("Resetting")

# Define buzzer object
#buzzer = machine.PWM(buzzer_pin)
#buzzer.freq(1000)

#initial LED states
stop_1_pin.on()
print("Stop 1 On")
stop_2_pin.on()
print("Stop 2 on")
prestage_1_pin.on()
print("Prestage 1 on")
prestage_2_pin.on()
print("Prestage 2 on")

while True:
    stop_1_pin.on()
    print("Stop 1 On")
    stop_2_pin.on()
    print("Stop 2 on")
    prestage_1_pin.on()
    print("Prestage 1 on")
    prestage_2_pin.on()
    print("Prestage 2 on")

    racer_1_pin.off()
    racer_2_pin.off()
    stage_3_1_pin.off()
    stage_3_2_pin.off()
    stage_2_1_pin.off()
    stage_2_2_pin.off()
    stage_1_1_pin.off()
    stage_1_2_pin.off()
    start_1_pin.off()
    start_2_pin.off()
    print("Resetting")

    # Wait for Button 1 or Button 2 to be pressed
    ready1 = False
    ready2 = False
    while (ready1 != True or ready2 != True):
        if not button_1_pin.value():
            ready1 = True
            racer_1_pin.on()
            buzzer_pin.on()
            utime.sleep(0.05)
            buzzer_pin.off()
            print("Button 1 pushed")
            #break
        if not button_2_pin.value():
            ready2 = True
            racer_2_pin.on()
            buzzer_pin.on()
            utime.sleep(0.05)
            buzzer_pin.off()
            print("Button 2 pushed")
            #break
        utime.sleep(0.05)
    # Wait for both racers to be ready
    #while True:
    #    if racer_1_pin.value() and racer_2_pin.value():
    #        break
    print("Both Racers Ready")

    start = False
    # Wait for Start button to be pressed
    while (start != True):
        if not start_button_pin.value():
            print("Try me")
            start = True
            #break
        print("Race waiting")
        utime.sleep(0.05)
    
    print("Race starting")

    # Start the race
    while True:
        #if racer1 and racer2:
        #    if start_button.value == False:
        if True:
            if True:
                utime.sleep(1)
                
                # Turn on Stage_3 LEDs and play 440Hz tone
                stage_3_1_pin.on()
                stage_3_2_pin.on()
                #gpio.output(stage_3_led_pin1, gpio.HIGH)
                print("Stage 3-1 On")
                #gpio.output(stage_3_led_pin2, gpio.HIGH)
                print("Stage 3-2 On")
                #play_tone(speaker_pin, 440, 0.5)
                print("Buzzer On")

                utime.sleep(0.5)

                # Turn on Stage_2 LEDs, and play 440Hz tone

                #gpio.output(stage_2_led_pin1, gpio.HIGH)
                #print("Stage 2-1 on")
                #gpio.output(stage_2_led_pin2, gpio.HIGH)
                #print("Stage 2-2 On")
                #play_tone(speaker_pin, 440, 0.5)
                #print("Buzzer On")
                stage_2_1_pin.on()
                stage_2_2_pin.on()
                #gpio.output(stage_3_led_pin1, gpio.HIGH)
                print("Stage 2-1 On")
                #gpio.output(stage_3_led_pin2, gpio.HIGH)
                print("Stage 2-2 On")
                #play_tone(speaker_pin, 440, 0.5)
                print("Buzzer On")

                utime.sleep(0.5)

                # Turn off Stage_2 LEDs, turn on Stage_1 LEDs, and play 880Hz tone
                
                stage_1_1_pin.on()
                stage_1_2_pin.on()
                #gpio.output(stage_3_led_pin1, gpio.HIGH)
                print("Stage 1-1 On")
                #gpio.output(stage_3_led_pin2, gpio.HIGH)
                print("Stage 1-2 On")
                #play_tone(speaker_pin, 440, 0.5)
                print("Buzzer On")

                utime.sleep(0.5)

                start_1_pin.on()
                start_2_pin.on()
                stop_1_pin.off()
                stop_2_pin.off()
                #gpio.output(stage_3_led_pin1, gpio.HIGH)
                #print("Stage 1-1 On")
                #gpio.output(stage_3_led_pin2, gpio.HIGH)
                #print("Stage 1-2 On")
                #play_tone(speaker_pin, 440, 0.5)
                print("Buzzer On")

                utime.sleep(5)
                
                break
               

   

               
