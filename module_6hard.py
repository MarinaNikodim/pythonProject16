import webcolors
import math


class Figure:
    def __init__(self, sides, color, filled=False):
        self.__sides = sides  # список сторон (целые числа)
        self.__color = self.__is_valid_color(color) # проверка цвета
        self.filled = filled

    def get_color(self): # возвращает список RGB цветов
        return self.__color

    def __is_valid_color(self, color):
        if isinstance(color, str):
            try:
                rgb = webcolors.name_to_rgb(color)
                return rgb
            except ValueError:
                raise ValueError("Некорректное название цвета.")
        elif isinstance(color, tuple) and len(color) == 3:
            if all(0<=value<=255 for value in color):
                return color
            else:
                raise ValueError("RGB значения должны быть в диапазоне от 0 до 255.")
        else:
            raise ValueError("Цвет должен быть строкой или кортежем из трех значений.")

    def set_color(self, r, g, b):
        new_color = (r, g, b)
        if self.__is_valid_color(new_color):
            self.__color = new_color


    def __is_valid_sides(self, *sides):  # принимает неграниченное количество сторон
        if all(side > 0 for side in sides):
            return sides
        else:
            raise ValueError("Все стороны должны быть положительными.")

    def get_sides(self):
        return self.__sides # Возвращает значение сторон

    def __len__(self):
        return len(self.__sides)  # переопределение метода длины

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = new_sides
        else:
            raise ValueError("Все стороны должны быть положительными.")


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius, filled = False):
        super().__init__([radius], color, filled)
        self.__radius = radius

    def get_square(self):
        return math.pi*(self.__radius**2)
    def get_radius(self):
        return self.__radius
    # def set_radius(self):
    #     if radius > 0:
    #         self.__radius = radius
    #         self.set_sides(radius)
    #     else:
    #         raise ValueError("Радиус должен быть положительным.")

class Triangle(Figure):
    sides_count = 3
    def __init__(self, sides, color, filled):
        super().__init__(sides, color, filled)

    def get_square(self):
        if len(self.get_sides()) != self.sides_count:
            raise ValueError # Должен принимать только три стороны

        side1, side2, side3 = self.get_sides()
        s= sum(self.get_sides())/2 # рассчитать полупериметр
        area_tr = (s*(s - side1)*(s - side2)*(s - side3))**0.5
        return area_tr


class Cube(Figure):
    sides_count = 12
    def __init__(self, color, length, filled = False):
        super().__init__(length, color, filled)
        self.__length = length

    def get_volume(self):
        return self.__length**3

    def get_length(self):
        return self.__length

    # def set_length(self):
    #     if length > 0:
    #         self.__length = length
    #         self.set_sides(length)
    #     else:
    #         raise ValueError("Длина ребра должна быть положительным.")



triangle1 = Triangle([3, 5, 7], (56, 67, 255),  True)
print(triangle1.get_sides())
print(triangle1.get_color())
triangle1.set_color(100, 100, 255)
print(triangle1.get_color())
print(triangle1.get_square())

circle1 = Circle((200, 200, 200), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(100, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides((15)) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))
print(circle1.get_square())

# Проверка объёма (куба):
print(cube1.get_volume())

