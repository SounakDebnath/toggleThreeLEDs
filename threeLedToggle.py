from signal import pause

count = 0
red = LED(17)
blue = LED(27)
green = LED(22)
button = Button(26)

leds = [red, blue, green]
red.off()
blue.off()
green.off()

count = -1

def inc():
    global count
    time.sleep(0.01)
    count += 1

while True:
    if (button.is_pressed):
        time.sleep(0.01)
        if (button.is_pressed):
            inc()
            leds[count%3].on()
            leds[(count-1)%3].off()
            leds[(count+1)%3].off()
            print(count)
            button.wait_for_release()

pause()