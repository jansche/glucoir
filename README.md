# glucoir
Build a IR blaster on Raspberry Pi and have a script transform your blood glucose levels into color coding of a LED strip

## What's this for?
I wanted to have my desk illuminated in colors representing my current blood glucose level. I'm Type 1 Diabetic (T1D), and I need to keep an eye on my blood glucose (BG) levels. Doing this while coding would mean I'd need to have my phone side by side or a website open, that shows my BG. Being in the flow while working, this is not very convenient. So I tried to find a subtle yet acknowledgeable method. I've put a color controllable LED strip under my glass desk topping, and needed to find a way to auto remote control it's remote control. 

## What you will need
  * A LED strip, that can change RGB colors via IR remote
  * A Raspberry Pi (I used a 3B)
  * A IR receiver diode
  * A IR emitter diode
  * A breadboard
  * Some jumper wires
  * A resistor (220K Ohm)
  * A NightScout site that has your current blood glucose levels.

## Prep
### Getting the Raspberry Pi ready
You have to set up your Pi to be able to receive and emit IR commands. I followed these instructions [](https://tutorials-raspberrypi.de/raspberry-pi-ir-remote-control/) (German language, also I kept to the default GPIO pins 17 and 18). Any Howto on this topic should do it.
### Nomenclature
Name your remote control desk0 when recording and saving your IR commands. Name your color buttons "red", "yellow", "green", "orange". Case sensitive. Or adapt in the Python script.
### Color coding
Make sure your personal limits for high, low and normal blood glucose are represented within the code. These limits are not retrieved from NightScout.
