# encoding: utf-8

from OmegaExpansion import oledExp
import time, os

# initialisation
lcd  = oledExp.driverInit()
if lcd != 0:
	print('Error initalizing OLED Explansion')

# kell ez???
oledExp.setVerbosity(0)
#lcd     = oledExp.setTextColumns()

# set up the display (show an image for 10 seconds)
imgBoot     = "/home/proofingBox/initImg.lcd"
if os.path.exists(imgBoot):
	lcd = oledExp.drawFromFile(imgBoot)
time.sleep(1)
#lcd		= oledExp.clear()

# get target and actual temperature values
tempTrg    = "25 °C"
tempAct    = "3.14 °C"

# set the brightness
lcd     = oledExp.setBrightness(127)

# set up the temperature block
# here comes a pic with a thermometer
#imgTemp = oledExp.setImageColumns(0,0)
#imgTemp = "/home/proofingBox/thermometer-icon.lcd"
#if os.path.exists(imgTemp):
	#lcd = oledExp.drawFromFile(imgTemp)
#else: lcd = oledExp.write("No image")
# here comes the target temperature value
#lcd     = oledExp.setCursor(1, 0)
#lcd     = oledExp.setCulomnAdressing(33, 40)
lcd     = oledExp.write("Target:")
time.sleep(1)
#lcd     = oledExp.setCulomnAdressing(88, 124)
lcd     = oledExp.write(tempTrg)
time.sleep(1)
# here comes the actual temperature value
#lcd     = oledExp.setCursor(3, 0)
#lcd     = oledExp.setCulomnAdressing(33, 40)
lcd     = oledExp.write("Actual:")
time.sleep(1)
#lcd     = oledExp.setCulomnAdressing(88, 124)
lcd     = oledExp.write(tempAct)

# set up the time block

# set up the heater on/off block


# at the end: clear the display
time.sleep(5)
lcd     = oledExp.clear()


########################################
# kell még:
# - hőérzékelő értékét beépíteni
# - relét (és fűtést) vezérelni
# - futó időt kijelezni
# - ha a hőmérő szélsőértékeket mutat, jelezzen (buzzer?)
