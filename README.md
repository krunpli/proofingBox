name: proofingBox
credit: David Stenszky, david.stenszky@gmail.com
license: MIT License

goal: The goal of this Project ist to build an (DIY) electric driven proofing box for dough (for bread).

concept: In an isolation box a heat source warms up the dough (with bowl) and keep the temperature of them constant. To achieve this, a temperature sensor is placed into the dough and a microcontroller switches the heat source according to the achieed temperature. Outside of the isolation box, the electric part takes place in a smaller box, where a display shows additional informations, such as the actual (and target) temperatures and the elapsed time.

needed parts/ what I have:
1, a thermal isolation box
2, a heater, I bought a ca. 25-30 W infrared heater ("25cmX50cm Far Infrared Film Warm Floor for Pet Waterloo Electric Underfloor Heating Mats", from aliexpress; Power:220W/m2, Voltage:220/240V 50/60Hz)
3, a temperature sensor ("1PCS DS1820 Stainless steel package Waterproof DS18b20 temperature probe temperature sensor 18B20 for arduino" from aliexpress)
4, a microprocessor (onion omega 2+ with dock, relay (for 240V) and oled expansions)
5, an outer box
6, power supply for the microprocessor (220V/5V/1A in my case)
7, a lot of cables
maybe:
8, reflection foil for the cap of the isolation box
9, time-reset button
10, on/off button

TODO:
- python code to readout the temperature sensor
- python code to control the relays
- python code for the time-reset button
- assembly

DONE:
- the python core program (rough frame)
- python code to measure the time
- the boot and background images
- python code to display data
