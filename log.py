import time
import datetime
from envirophat import light, motion, weather, leds

now = datetime.datetime.now()
nows = str(now)
filename = 'sensordata'+' '+ nows+'.txt'
print("Saving as...")
print(filename)

out = open(filename, 'w')
out.write('light\trgb\tmotion\theading\ttemp\tpress\n')

try:
    while True:
        lux = light.light()
        leds.on()
        rgb = str(light.rgb())[1:-1].replace(' ', '')
        leds.off()
        acc = str(motion.accelerometer())[1:-1].replace(' ', '')
        heading = motion.heading()
        temp = weather.temperature()
        press = weather.pressure()
        out.write('%f\t%s\t%s\t%f\t%f\t%f\n' % (lux, rgb, acc, heading, temp, press))
        print('light, rgb, acc, heading, tempature, pressure')
        print('%f\t%s\t%s\t%f\t%f\t%f\n' % (lux, rgb, acc, heading, temp, press))
        time.sleep(1)

except KeyboardInterrupt:
    leds.off()
    out.close()

