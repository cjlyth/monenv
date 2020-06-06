
This case is something I hacked together with scrap polycarbonate sheets. 

My original design goals were
- Hold battery, sensor, and logger in place
- Allow airflow to the sensor
- Allow for addition of noise sensor (yet to be added)
- Allow easy removal of the SD card
- Allow for access to the USB-C port by drilling into the side 

This design met all criteria:

<img src="assets/desired.jpg"
     alt="Desired Design"
     style="float: left; margin-right: 10px;" />

This seemed to work great except after running it for a day, I realized it was not logging. 
After some trial and error, I realized the OpenLog Artemis requires hitting the reset button to get logging to work when on battery power. 

The power button is on the opposite side of the board from the SD card. 

<img src="assets/reset-button.jpg"
     alt="Desired Design"
     style="float: left; margin-right: 10px;" />

Unfortunately, because of how the components are placed, I can't simply flip the board.
You can see how far back the SD card is set compared to the artemis component. 
This makes it impossible to access when the board is artemis-side-up. 

<img src="assets/sd-card.jpg"
     alt="Desired Design"
     style="float: left; margin-right: 10px;" />

For now, I am going to leave the OpenLog Artemis board loose. 

Disappointing...