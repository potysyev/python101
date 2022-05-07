class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Start draw")


class Pen(Stationary):
    def draw(self):
        print("Start draw with pen")


class Pencil(Stationary):
    def draw(self):
        print("Start draw with pencil")


class Handle(Stationary):

    def draw(self):
        print("Start draw with handle")


pen1 = Pen("Pen")
pencil1 = Pencil("Pencil")
handle1 = Handle("Handle")
pen1.draw()
pencil1.draw()
handle1.draw()
