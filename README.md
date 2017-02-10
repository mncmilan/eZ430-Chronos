# eZ430-Chronos
This software enables acceleration data adquisition from eZ430-Chronos watch by Texas Instruments. It intends to capture human hand-movement, in order to create a new flight control system for drones (**CUBA** - Control for UAS Based on Accelerometers https://github.com/mncmilan/CUBA). If you want further information about the project, you can also check: http://steelhummingbird.blogspot.com.es/ 

## Requirements
The code was tested with the following setup:
* Python 3.5.2
* Pyserial 3.2.1

## Getting started
Once acceleration data is obtained, it is processed to determine hand-movement direction, then a filter is applied in order to disregard hand trembling or minor involuntary hand movements, thus a stable value is achieved.

### Communications protocol
There are three defined messages to communicate with Chronos so as to make him perform some task, that is:
* Start communications: [255, 7, 3]
* Stop communications: [255, 9, 3]
* Acceleration data request: [255, 8, 7, 0, 0, 0, 0]

After some research I found that the response that Chronos gives to the acceleration data request is 7 bytes long, and the fourth byte indicates whether the data is valid or not:
* If the 4th byte = 255 (0xFF), then there is no acceleration data.
* If the 4th byte = 1, then the array contains valid data.

### Defined modes
It has been created different types of filtering:

* **Free mode** - It eliminates the noise in X and Y axis.
* **Single axis mode** - It eliminates the noise in X and Y axis and it only considers the movement in the axis where there's a bigger acceleration change.
* **Rough mode** - It eliminates the noise in X and Y axis and it only considers the movement in the axis where there's an acceleration change bigger than a defined threshold, setting the other one constant at the initial value. Thus only rough or high range hand movements are detected.

## Repository
The public repository is located here:

git://github.com/mncmilan/eZ430-Chronos.git

## License
This software is published under the terms of the Creative Commons license.

https://creativecommons.org/

## Author
Mónica Milán (@mncmilan)

mncmilan@gmail.com
