
This project was started to monitor the environment around my printer. 
My primary goal is to determine how well my ventilation performs. 

The hardware is pretty simple, using plug-and-play components from sparkfun. 

### OpenLog Artemis
I chose the [OpenLog Artemis](https://www.sparkfun.com/products/15846) because it has several interesting features.
- LIPO battery support including a charge circuit
- USB-C power input to stream logs and charge/operate the setup
- RTC to track time 
- Qwiic support with a great catalog of sensors

I like the offline capability because I also plan to use this in other projects if it works out well. For example, I would like to add this to my Ural for long road trips to build a map of air quality, elevation, speed ets. 

### SparkFun Environmental Combo Breakout
I chose this [environment sensor](https://www.sparkfun.com/products/14348) as a starting point because it seemed to have the most robust capabilities. 
At this point I am not sure which sensors will work best for the VOCs my printer puts out. 
I also plan to add sound and other sensors but this board provides my core needs (humidity, temperature, TVOCs), and some I dont plan to use.

### Controller
I am using a raspberry pi 4 as the controller for this project because I have one on-hand and it is an easy platform for the rest of my project. 
