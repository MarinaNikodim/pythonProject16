class Horse:

    def __init__(self, sound):
        self.dx = None
        self.x_distance = 0 # Пройденный путь
        sound = 'Frrr'
        self.sound = sound

    def run(self, dx):
        self.dx = dx
        self.x_distance += dx


class Eagle:

    def __init__(self, sound):
        sound = 'I train, eat, sleep, and repeat'
        self.dy = None
        self.y_distance = 0  # Высота полета
        self.sound = sound

    def fly(self, dy):
        self.dy = dy
        self.y_distance += dy


class Pegasus(Horse, Eagle):
    def __init__(self, sound, x_distance, y_distance):
        super().__init__(sound)
        Horse.__init__(self, x_distance)
        Eagle.__init__(self, y_distance)

    def move(self, dx, dy):
        self.run(dx)
        self.fly(dy)

    def get_pos(self):
        return self.x_distance, self.y_distance

    def voice(self):
        print(f'Pegasus say: {self.sound}')

print(Pegasus.mro())


p1 = Pegasus('0', 0, 0)
print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()




