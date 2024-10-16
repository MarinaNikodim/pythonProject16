class Horse:

    def __init__(self, sound = 'Frrr', x_distance=0):
        self.dx = None
        self.x_distance = x_distance # Пройденный путь
        self.sound = sound

    def run(self, dx):
        self.dx = dx
        self.x_distance += dx


class Eagle:

    def __init__(self, sound='I train, eat, sleep, and repeat', y_distance=0):
        self.dy = None
        self.y_distance = y_distance  # Высота полета
        self.sound = sound

    def fly(self, dy):
        self.dy = dy
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self, sound='I train, eat, sleep, and repeat', x_distance=0, y_distance=0):
        Horse.__init__(self, sound, x_distance)
        Eagle.__init__(self, sound, y_distance)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(f'Pegasus says: {self.sound}')

print(Pegasus.mro())


p1 = Pegasus()
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()




