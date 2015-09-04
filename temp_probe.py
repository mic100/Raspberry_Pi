# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------#
#                                                                             #
#                            import libs                                      #
#                                                                             #
#-----------------------------------------------------------------------------#
from w1thermsensor import W1ThermSensor
import w1thermsensor as W
import _mysql_exceptions as M
import time
import MySQLdb as ms
import os
#import glob
#import subprocess
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                                                                             #
#                            main dev                                         #
#                                                                             #
#-----------------------------------------------------------------------------#
while True :
    try :
        try :
            os.system("sudo modprobe w1-gpio")
            os.system("sudo modprobe w1-therm")
            #dir = "/sys/bus/w1/devices"
            os.system("cd /sys/bus/w1/devices/28*")
        except(W.core.SensorNotReadyError) :
            print '\n', "--------ISSUE1--------", '\n'

        #set up of the variables to access to the distant database.
        try :
            db = ms.connect(host="ns1075.ifastnet.com",user="oakessoc_admin",\
                            passwd="femmes125.",db="oakessoc_sensors")
        except(M.OperationalError):
            print '\n', "########ISSUE_ns1075.ifastnet.com_Mysqldatabase_########"
            print "########RPi_CANT_REACH_DATABASE########"
            print "########CHECK_WIRES_FROM_RPI_TO_INTERNETPROVIDER'S_ROOTER(BOX)########", '\n'
            os.system("sudo reboot")
        try :
            #set up of a cursor to be able to execute a query in database.
            c = db.cursor()
        except(NameError) :
            os.system("sudo reboot")
        while True :
            try :
                for sensor in W1ThermSensor.get_available_sensors() :
                    #we want to store the date and temperature variables in database.
                    date = time.strftime("%a, %d %b %Y %H:%M:%S", time.gmtime())
                    try :
                        celsius = sensor.get_temperature(W1ThermSensor.DEGREES_C)
                    except(W.core.SensorNotReadyError) :
                        print '\n', "########ISSUE_sensor.get_temperature########", '\n'

                    if sensor.id == '0000065c12c7' :
                        #os.system("cat /sys/bus/w1/devices/28-0000065c12c7/w1_slave")
                        #we excute our query to insert value to the distant db.
                        query = c.execute(
                            "INSERT INTO temp_0 (date, sensor_1) VALUES (%s,%s)""",(date, \
                            celsius)
                            )
                        print "GrowBed(1) T°:", celsius, "date:",date
                    elif sensor.id == '0000065c7fbd' :
                        #os.system("cat /sys/bus/w1/devices/28-0000065c7fbd/w1_slave")
                        #we excute our query to insert value to the distant db.
                        query = c.execute(
                            "INSERT INTO temp_0 (date, sensor_3) VALUES (%s,%s)""",(date, \
                            celsius)
                            )
                        print "Aquarium T°:", celsius, "date:",date
                    elif sensor.id == '0000065bd178' :
                        #os.system("cat /sys/bus/w1/devices/28-0000065bd178/w1_slave")
                        #we excute our query to insert value to the distant db.
                        query = c.execute(
                            "INSERT INTO temp_0 (date, sensor_2) VALUES (%s,%s)""",(date, \
                            celsius)
                            )
                        print "GrowBed(0) T°:", celsius, "date:",date
                    elif sensor.id == '02156299a4ff' :
                        #os.system("cat /sys/bus/w1/devices/28-0000065xxxxx/w1_slave")
                        #we excute our query to insert value to the distant db.
                        query = c.execute(
                            "INSERT INTO temp_0 (date, sensor_4) VALUES (%s,%s)""",(date, \
                            celsius)
                            )
                        print "GrowBed(Fish_Tower) T°:", celsius, "date:",date
                    elif sensor.id == '031563c859ff' :
                        #os.system("cat /sys/bus/w1/devices/28-0000065xxxxx/w1_slave")
                        #we excute our query to insert value to the distant db.
                        query = c.execute(
                            "INSERT INTO temp_0 (date, sensor_5) VALUES (%s,%s)""",(date, \
                            celsius)
                            )
                        print "AmbiantRoom T°:", celsius, "date:",date
                print '\n', '--------    ----------------    --------------------    --------', '\n'
                #time.sleep(1)
            except(W.core.SensorNotReadyError, W.core.NoSensorFoundError) :
                print '\n', "--------ISSUE2--------", '\n'
                os.system("sudo reboot")
    except(W.core.SensorNotReadyError) :
        print '\n', "--------ISSUE3--------", '\n'
