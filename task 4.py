class Car:
    speed = int(input('Enter the speed of the car : '))
    color = input('Enter the color of the car : ')
    name = input('Enter cars name : ')
    is_police = False

    def go(self):
        print('The car is going')

    def stop(self):
        print('The car stopped')

    def turn(self):

        print('The car changed direction')

    def show_speed(self, speed):
        self.speed = speed
        return speed

class Towncar(Car):

    def show_speed(self, speed):
        self.speed = speed
        if speed > 60:
            print(' Your speed is too high')

class Workcar(Car):

    def show_speed(self, speed):
        self.speed = speed
        if speed > 40:
            print('Your speed is too high')
        else:
            print('You are driving slow :-)')

class Policecar(Car):
    got_weapon = True
    got_siren = True


class Sportcar(Car):
    cost = 'cost'
    engine_volume = int(input('Engine volume is : '))





car = Car()
car.go()
print(f'The color of car is : {car.color}')

towncar = Towncar()
towncar.show_speed(100)

workcar = Workcar()
workcar.show_speed(30)

police_car = Policecar()
print(f'This car got weapon : {police_car.got_weapon}')

sport_car = Sportcar()
print(f'The engine volume is {sport_car.engine_volume} l')




