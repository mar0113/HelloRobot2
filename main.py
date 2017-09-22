from gopigo import *
import time


class Piggy(object):

    def __init__(selfself):
        print("I AM ALIVE")

    def pulse(self):
        """check for obstacles, drive fixed amount forward"""
        look = us_dist(15)  # store the distance reading
        if look > 80:
            fwd()
            time.sleep(1)
            stop()

    def cruise(self):
        """drive fwd, stop if sensor detects obstacle"""
        fwd()
        while(True):
            if us_dist(15) < 30:
                stop()
            time.sleep(.2)

    def servo_sweep(self):
        """loops in a 120 degree arc and moves servo"""
        for ang in range(20, 160, 2):
            servo(ang)
            time.sleep(.2)

    def cha_cha(self):
        for x in range(5):
            right_rot()
            time.sleep(.5)
            left_rot()
            time.sleep(.5)
            stop()

# MY APP
p = Piggy()


def menu():
    while True:
        input = raw_input("Press 1 for cruise \n Press 2 for pulse \n Press 3 for sweep")
        if "1" in input:
            p.cruise()
        elif "2" in input:
            p.pulse()
        elif "3" in input:
            p.servo_sweep()



try:
    menu()
except(KeyboardInterrupt, SystemExit):
    from gopigo import *
    stop()
