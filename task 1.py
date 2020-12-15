import time


class Trafficlights():

    __color = 0

    def running (self):
        print('Red signal')
        time.sleep(7)
        print('Yellow signal')
        time.sleep(2)
        print('Green signal')
        time.sleep(5)
        Trafficlights.__color += 1

a = Trafficlights()
a.running()