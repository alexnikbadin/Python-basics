class Stationary:
    title = 'Stationary'


    def draw(self):
        print('Start drawing')
        pass

class Pen(Stationary):

    def draw(self):
        print('Start drawing a thin line')
        pass


class Pencil(Stationary):

    def draw(self):
        print('Start drawing a red line')
        pass

class Handle(Stationary):

    def draw(self):
        print('Start drawing a thick line')
        pass


picture = Stationary()
print(picture.title)
picture.draw()

pen_picture = Pen()
pen_picture.draw()

pencil_picture = Pencil()
pencil_picture.draw()

handle_picture = Handle()
handle_picture.draw()