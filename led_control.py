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
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.setup(22, GPIO.OUT)
    GPIO.setup(5, GPIO.OUT)
    GPIO.setup(6, GPIO.OUT)
    GPIO.setup(13, GPIO.OUT)
    GPIO.setup(19, GPIO.OUT)
    GPIO.setup(26, GPIO.OUT)

    GPIO.setup(23, GPIO.OUT)
    GPIO.setup(12, GPIO.OUT)
    GPIO.setup(16, GPIO.OUT)
    GPIO.setup(20, GPIO.OUT)
    GPIO.setup(21, GPIO.OUT)

    while True :

        T = time.strftime("%a, %d, %b %Y %H:%M:%S", time.gmtime())[18:26]
        T1 = time.strftime("%a, %d, %b %Y %H:%M:%S", time.gmtime())

        light_hour = ['18','19','20','21','22','23','00','01','02','03','04','05']

        print "||DATE:", T1, "||MODE:",

        if T[0:2] in light_hour :
            print "--------    LED_ON    --------"
            led_status = 1
            query(date=T1,led_status=led_status)
            #attention probleme avec LED LEVEL 1 PIN 17 et 27 fonctionnent mal
            #tout le power est sur pin 17
            GPIO.output(17, GPIO.HIGH) #TOWER_1_LEVEL_0_LIGHT_0 OFF(LOW)/ON(HIGH)
            GPIO.output(27, GPIO.HIGH) #TOWER_1_LEVEL_0_LIGHT_1 OFF(LOW)/ON(HIGH)
            GPIO.output(22, GPIO.HIGH) #TOWER_0_LEVEL_1_LIGHT_0 OFF(LOW)/ON(HIGH)
            GPIO.output(5, GPIO.HIGH) #TOWER_0_LEVEL_1_LIGHT_1 OFF(LOW)/ON(HIGH)
            GPIO.output(6, GPIO.HIGH) #TOWER_0_PUMP OFF(LOW)/ON(HIGH)
            GPIO.output(13, GPIO.HIGH) #TOWER_1_PUMP OFF(LOW)/ON(HIGH)
            GPIO.output(19, GPIO.LOW) #TOWER_0_FISHLED_BLUE OFF(LOW)/ON(HIGH)
            GPIO.output(26, GPIO.HIGH) #TOWER_0_FISHLED_ALL_LIGHTS OFF(LOW)/ON(HIGH)
            GPIO.output(23, GPIO.HIGH) #TOWER_0_LED_GROWBED(INIT_TOWER) OFF(LOW)/ON(HIGH)
            GPIO.output(12, GPIO.LOW) #NOT_USED
            GPIO.output(16, GPIO.LOW) #NOT_USED
            GPIO.output(20, GPIO.LOW) #GPIO CONNECTED TO TEMPERATURES PROBES
            GPIO.output(21, GPIO.LOW) #NOT_USED

        else :
            print "--------    LED_OFF    --------"
            led_status = 0
            query(date=T1,led_status=led_status)
            GPIO.output(17, GPIO.LOW) #TOWER_1_LEVEL_0_LIGHT_0 OFF(LOW)/ON(HIGH)
            GPIO.output(27, GPIO.LOW) #TOWER_1_LEVEL_0_LIGHT_1 OFF(LOW)/ON(HIGH)
            GPIO.output(22, GPIO.LOW) #TOWER_0_LEVEL_1_LIGHT_0 OFF(LOW)/ON(HIGH)
            GPIO.output(5, GPIO.LOW) #TOWER_0_LEVEL_1_LIGHT_1 OFF(LOW)/ON(HIGH)
            GPIO.output(6, GPIO.HIGH) #TOWER_0_PUMP OFF(LOW)/ON(HIGH)
            GPIO.output(13, GPIO.HIGH) #TOWER_1_PUMP OFF(LOW)/ON(HIGH)
            GPIO.output(19, GPIO.HIGH) #TOWER_0_FISHLED_BLUE OFF(LOW)/ON(HIGH)
            GPIO.output(26, GPIO.LOW) #TOWER_0_FISHLED_ALL_LIGHTS OFF(LOW)/ON(HIGH)
            GPIO.output(23, GPIO.LOW) #TOWER_0_LED_GROWBED(INIT_TOWER) OFF(LOW)/ON(HIGH)
            GPIO.output(12, GPIO.LOW) #NOT_USED
            GPIO.output(16, GPIO.LOW) #NOT_USED
            GPIO.output(20, GPIO.LOW) #GPIO CONNECTED TO TEMPERATURES PROBES
            GPIO.output(21, GPIO.LOW) #NOT_USED
        #we print each 60 seconds the stat of the program
        time.sleep(60)

def query(date,led_status) :

    try :
        db = ms.connect(host="your_host_name",user="your_user_name",\
                        passwd="yourpassword",db="your_database_name")
    except(M.OperationalError):
        print '\n', "########ISSUE_%s_Mysqldatabase_########" % ("your_host_name")
        print "########RPi_CANT_REACH_DATABASE########"
        print "########CHECK_WIRES_FROM_RPI_TO_INTERNETPROVIDER'S_ROOTER(BOX)########", '\n'
        os.system("sudo reboot")
    try :
        #set up of a cursor to be able to execute a query in database.
        c = db.cursor()
        date = time.strftime("%a, %d, %b %Y %H:%M:%S", time.gmtime())
        c.execute("INSERT INTO led_1 (date, led_status) VALUES (%s,%s)""",(date, \
                led_status))
    except(NameError) :
        os.system("sudo reboot")
                
if __name__ == "__main__" :

    light_control()

    print "the end"

