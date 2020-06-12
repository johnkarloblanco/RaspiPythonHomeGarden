# RaspiPythonHomeGarden
This is a program I made for automating our MicroGreens automation system.

Goal:
To automate lighting, humidifier, and fan to reduce man hour spent on the product for maximum profit and optimal plant growth.
Humidity sensor attached for sensing. Still need to use this to make the humidifiers run as needed. Currently runs on scheduled intervals.
The arduino itself could have been enough to run the entire thing but I want to be able to use teamviewer to control and update the 
raspberry pi as needed. I also wanted to test signalings between the rpi and arduino to see how well they work with each other.

How it works:

The raspberrypi is used to send signals to an arduino. The rpi will send the arduino signals to turn the lights depending on the 
time of the day. 
The fan and humidifier are preset to run 10 minutes before the end of the hour. This is enough for our requirements.According to our 
research and the result of our experiments, running a fan helps the plants grow stronger stems andtrunks while also reducing moisture 
on the plant body to reduce occurence of molds and pests. The humidifier reduces the drying rate of the soil on dry days.

