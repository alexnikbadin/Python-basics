class Road:

    _length = 'length'
    _width = 'width'

    def count(self, _length, _width, mass, height):
        self._width = _width
        self._length = _length
        self.mass = mass
        self.height = height
        total_mass = _width * _length * mass * height
        return total_mass

asphalt_mass = Road()
print(asphalt_mass.count(_length=int(input('Enter the length of the road in metres: ')), _width=int(input('Enter the width of the road in metres : ')), mass=int(input('Enter the mass of the road in kg : ')), height=int(input("Enter the height of the road in sm : "))))


