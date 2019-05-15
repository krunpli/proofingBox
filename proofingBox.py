# encoding: utf-8
from OmegaExpansion import oledExp
import math, time, os


## initialisation
print('Starting the program proofingBox...')

# initialisation the oled expansion
lcd  = oledExp.driverInit()
if lcd != 0:
	print('Error initalizing OLED Expansion')
# set verbosity
oledExp.setVerbosity(0)
# set the brightness
lcd     = oledExp.setBrightness(127)
if lcd != 0:
	print('Error setting the brightness for the OLED Expansion')

# set up the boot display (show an image for 10 seconds)
imgBoot     = "/home/proofingBox/initImg.lcd"
if os.path.exists(imgBoot):
	oledExp.drawFromFile(imgBoot)
time.sleep(1)
oledExp.clear()


## get the target and actual temperature values
## TODO preparation the readout: https://docs.onion.io/omega2-docs/communicating-with-1w-devices.html
tempTrg    = "25"
# tempAct = awk -F= '/t=/ {printf "%.03f\n", $2/1000}' /sys/devices/w1_bus_master1/XXXXX/w1_slave
tempAct    = "21"

## get the relay status


## get the uptime
def get_uptime():
    with open('/proc/uptime', 'r') as f:
        uptimeS = float(f.readline().split()[0])
    	uptimeMin = uptimeS / (60 * 1.0)
    	uptimeH = uptimeMin / (60 * 1.0)
    return uptimeH

## main function
def init(tempTrg,tempAct):
	"teszt"
# here comes the background image (than it won't be overwritten)
oledExp.setImageColumns(0,0)
imgBackground = "/home/proofingBox/background.lcd"
if os.path.exists(imgBackground):
	oledExp.drawFromFile(imgBackground)
else: oledExp.write("No background image")

# display the target temperature value
oledExp.setTextColumns()
oledExp.setCursor(1,7)
oledExp.write("Target:   " + tempTrg + " C")

# display the actual temperature value
oledExp.setTextColumns()
oledExp.setCursor(3,7)
oledExp.write("Actual:   " + tempAct + " C")

# display the time gone (actually uptime of the system)
uptime_h = int(math.modf(get_uptime())[1])
uptime_min = int(math.modf(get_uptime())[0]*60)
oledExp.setTextColumns()
oledExp.setCursor(5,6)
oledExp.write(str(uptime_h) + " h")
oledExp.setTextColumns()
oledExp.setCursor(7,6)
oledExp.write(str(uptime_min) + " min")

# display the heater on/off block
oledExp.setTextColumns()
oledExp.setCursor(6,18)
oledExp.write("OFF")



# at the end: clear the display
time.sleep(5)
lcd     = oledExp.clear()


########################################
# kell még:
# - hőérzékelő értékét beépíteni
# - relét (és fűtést) vezérelni
# - ha a hőmérő szélsőértékeket mutat, jelezzen (buzzer?)