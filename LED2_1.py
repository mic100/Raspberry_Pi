# -*- coding: utf-8 -*-

#-----------------------------------------------------------------------------#
#                                                                             #
#                            import libs                                      #
#                                                                             #
#-----------------------------------------------------------------------------#
import time
import MySQLdb as ms
import _mysql_exceptions as M
import RPi.GPIO as GPIO
import os
#-----------------------------------------------------------------------------#

#-----------------------------------------------------------------------------#
#                                                                             #
#                            main dev                                         #
#                                                                             #
#-----------------------------------------------------------------------------#

def light_control() :

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
#    GPIO.setup(17, GPIO.OUT)
#    GPIO.setup(22, GPIO.OUT)
#    GPIO.setup(23, GPIO.OUT)
#    GPIO.setup(24, GPIO.OUT)
    GPIO.setup(17, GPIO.OUT)

    while True :

        T = time.strftime("%a, %d, %b %Y %H:%M:%S", time.gmtime())[18:26]
        T1 = time.strftime("%a, %d, %b %Y %H:%M:%S", time.gmtime())

        light_hour = ['18','19','20','21','22','23','00','01','02','03','04','05']

        print "||DATE:", T1, "||MODE:",

        if T[0:2] in light_hour :
            print "--------    LED_ON    --------"
            led_status = 1
            query(date=T1,led_status=led_status)
#            GPIO.output(17, GPIO.HIGH)
#            GPIO.output(22, GPIO.HIGH)
#            GPIO.output(23, GPIO.HIGH)
#            GPIO.output(24, GPIO.HIGH)
            GPIO.output(17, GPIO.HIGH)
        else :
            print "--------    LED_OFF    --------"
            led_status = 0
            query(date=T1,led_status=led_status)
#            GPIO.output(17, GPIO.LOW)
#            GPIO.output(22, GPIO.LOW)
#            GPIO.output(23, GPIO.LOW)
#            GPIO.output(24, GPIO.LOW)
            GPIO.output(17, GPIO.LOW)
        time.sleep(1)

def query(date,led_status) :

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
        date = time.strftime("%a, %d, %b %Y %H:%M:%S", time.gmtime())
        c.execute("INSERT INTO led_0 (date, led_status) VALUES (%s,%s)""",(date, \
                led_status))
    except(NameError) :
        os.system("sudo reboot")

if __name__ == "__main__" :

    light_control()

    print "the end"
