class Warehouse:

    square = 200
    keeping = {'Printers': 10,
               'Copiers': 15,
               'Scans': 20}

    def __init__(self):
        pass

    def __str__(self):
        return

    def get_equipment(self):
        print("We got new equipment.")

    def give_equipment(self, equipment, office):
        self.equipment = equipment
        self.office = office
        print(f'We directed {equipment} to the {office}')

    def keep(self):
        try:
            Warehouse.keeping['Printers'] = int(input('Enter new quantity : '))
        except ValueError:
                print('You entered the string!')


class Equipment:

    power = 220
    maintenance = True
    safety = True

    def __init__(self):
        pass

class Printer (Equipment):
    def __init__(self, color, speed_print):
        super().__init__()
        self.color = color
        self.speed_print = speed_print
        pass



class Copier(Equipment):
    def __init__(self, paper_format, copy_speed):
        super().__init__()
        self.paper_format = paper_format
        self.copy_speed = copy_speed
        pass


class Scanner(Equipment):
    def __init__(self, scan_speed, resolution):
        super().__init__()
        self.scan_speed = scan_speed
        self.resolutoin = resolution
        pass

new_eq = Warehouse()
new_eq.get_equipment()
new_eq.give_equipment('printer', 'office 10')
print(new_eq.keeping)
new_eq.keep()
print(new_eq.keeping)
