# answering module (print)
import time

def pTF(tf):
    if tf:
        print "true"
    if tf:
        print "false"


def pYN(yn):
    if yn:
        print "yes"
    if yn:
        print "no"

def pTime():
    # print "Time:"
    # print time.time(), time.ctime(), time.strftime("%m/%d/%Y")
    # print time.ctime(), "\n"
    print time.strftime("%m/%d/%Y"), "\n"