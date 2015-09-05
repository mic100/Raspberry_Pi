#!/usr/bin/python
# -*- coding: utf-8 -*-

from cv2 import *
import MySQLdb as ms
import time
import _mysql_exceptions as M
import os

def get_image():
    cam1 = VideoCapture(0)
    cam2 = VideoCapture(1)
    s1, img1 = cam1.read()
    s2, img2 = cam2.read()
    if s1:
        imwrite("test1.jpg",img)
    if s2:
        imwrite("test2.jpg",img)

def read_image():
    fin1 = open("test1.jpg")
    fin2 = open("test2.jpg")
    img1 = fin1.read()
    img2 = fin2.read()
    return img1,img2

def query() :

    try :
        db = ms.connect(host="your_host_name",user="your_user_name",\
                        passwd="your_password",db="your_database_name")
    except(M.OperationalError):
        print '\n', "########ISSUE_%s_Mysqldatabase_########" % ("your_host_name")
        print "########RPi_CANT_REACH_DATABASE########"
        print "########CHECK_WIRES_FROM_RPI_TO_INTERNETPROVIDER'S_ROOTER(BOX)##"
        os.system("sudo reboot")

    data1 = read_image()[0]
    data2 = read_image()[1]

    try :
        #set up of a cursor to be able to execute a query in database.
        c = db.cursor()
        date = time.strftime("%a, %d, %b %Y %H:%M:%S", time.gmtime())
        c.execute("INSERT INTO images(date,cam1,cam2) VALUES (%s,%s,%s)", (date,data1,data2))
        print "<--- Send image --->","--- / date / --- : ",date
    except(NameError) :
        #os.system("sudo reboot")
        print "NameError: ", NameError

if __name__ == "__main__" :

    while True :
        get_image()
        try :
            query()
            #print "Ok test.jpg image found"
        except :
            print "No test.jpg image found"
        #cam get .jpg file and send an image \
        #every 30 minutes=1800 seconds
        #every 5minutes = 300 seconds
        time.sleep(300)
