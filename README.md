# Raspberry_Pi
<Sensors_alpha>


1)Re_installation of all dependencies :

sudo apt-get udpate
sudo apt-get upgrade

installation of OpenCV (2.4.9 version):
(depending on your raspberry pi processor but it take between 2.5 and 10 hours, be patient!)
sudo apt-get -y install build-essential cmake cmake-curses-gui pkg-config libpng12-0 libpng12-dev libpng++-dev libpng3 libpnglite-dev zlib1g-dbg zlib1g zlib1g-dev pngtools libtiff4-dev libtiff4 libtiffxx0c2 libtiff-tools libeigen3-dev

sudo apt-get -y install libjpeg8 libjpeg8-dev libjpeg8-dbg libjpeg-progs ffmpeg libavcodec-dev libavcodec53 libavformat53 libavformat-dev libgstreamer0.10-0-dbg libgstreamer0.10-0 libgstreamer0.10-dev libxine1-ffmpeg libxine-dev libxine1-bin libunicap2 libunicap2-dev swig libv4l-0 libv4l-dev python-numpy libpython2.6 python-dev python2.6-dev libgtk2.0-dev

wget -O openCV-2.4.9.zip http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/2.4.9/opencv-2.4.9.zip/download
unzip openCV-2.4.9.zip
cd openCV-2.4.9
mkdir release
cd release

Configuration of OpenCV :
sudo ccmake ../
(Press 'c' if empty cache configuration)
Scroll down with pad to "BUILD_JPEG" and press "ENTER" to switch from "OFF" to "ON"
Repeat for "BUILD_PNG"
When done press 'c' to configure and press 'g' to generate the makefile of this OpenCV configuration. 
Then :
sudo make
sudo make install
And wait until it's done! (Be patient it's very long!)


2)Follow up of Wheezy image configuration :
Then do :
sudo apt-get install python-dev
sudo apt-get install python-pip
sudo apt-get install python-mysqldb
sudo apt-get install python-rpi.gpio
sudo pip install w1thermensor (see : https://github.com/timofurrer/w1thermsensor)
cd
sudo nano /boot/config.txt ---->scroll down and add at the end of file dtoverlay=w1-gpio,gpio="the_number_of_your_gpiopin"(example : gpio=4)
verify if all temperature probe are detected :
cd
sudo modprobe w1-gpio
sudo modprobe w1-therm
cd /sys/bus/w1/devices
ls 
if all is good you should be able to see there respective id like mine :
"""28-0000065bd178  28-0000065c12c7  28-0000065c7fbd  28-02156299a4ff  28-031563c859ff  w1_bus_master1"""


3)Then get the python scripts :
Download the zip file : 
wget https://github.com/mic100/Raspberry_Pi/archive/master.zip
unzip master.zip
cd /Raspberry_Pi-master

At last test the python scipts : 
sudo python led_control.py
To interrupt program (control+C)
sudo python temp_control.py
To interrupt program (control+C)
 

End
