# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------#
#                                                                             #
#                            import libs                                      #
#                                                                             #
#-----------------------------------------------------------------------------#
import os
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                                                                             #
#                              main dev                                       #
#                                                                             #
#-----------------------------------------------------------------------------#
#when i need to re install all the program in case of loss
#we can get them back from the run of that python program

#os.system("sudo modprobe w1-gpio")
#os.system("sudo modprobe w1-therm")
#os.system("cd /sys/bus/w1/devices/28*")

os.system("sudo apt-get update")
os.system("sudo apt-get upgrade")
os.system("sudo apt-get install python-pip")
os.system("sudo apt-get install python-dev")
os.system("sudo apt-get install python-rpi.gpio")

#we install the lib to get the temperature of the temp sensors DS18B20
#se more here : https://github.com/timofurrer/w1thermsensor
os.system("sudo pip install w1thermsensor")
#install mysqldb lib for python used in code
os.system("sudo apt-get install python-mysqldb")
#os.system("sudo apt-get install tightvncserver")
os.system("sudo reboot")

print "the end"
