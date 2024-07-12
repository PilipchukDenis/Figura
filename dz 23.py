# 1 задание Создать базовый класс figura с методом для подсчета
# площади. Создать производные классы: прямоугольник,
# круг, прямоугольный треугольник, трапеция со своими
# методами для подсчета площади.


# from abc import ABC, abstractmethod
# import math
# 
# class Shape(ABC):
#     @abstractmethod
#     def calculate_area(self):
#         pass
# 
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
# 
#     def calculate_area(self):
#         return self.width * self.height
# 
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
# 
#     def calculate_area(self):
#         return math.pi * self.radius**2
# 
# class RightTriangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
# 
#     def calculate_area(self):
#         return 0.5 * self.base * self.height
# 
# class Trapezoid(Shape):
#     def __init__(self, base1, base2, height):
#         self.base1 = base1
#         self.base2 = base2
#         self.height = height
# 
#     def calculate_area(self):
#         return 0.5 * (self.base1 + self.base2) * self.height
# 
# 
# rectangle = Rectangle(5, 10)
# print("Площадь прямоугольника:", rectangle.calculate_area())
# 
# circle = Circle(7)
# print("Площадь круга:", circle.calculate_area())
# 
# triangle = RightTriangle(3, 4)
# print("Площадь прямоугольного треугольника:", triangle.calculate_area())
# 
# trapezoid = Trapezoid(4, 6, 5)
# print("Площадь трапеции:", trapezoid.calculate_area())



# 2 задание

# Для классов из задания 1 нужно переопределить магические методы int(возвращает площадь) и str (возвращает
# информацию о фигуре).

# class Shape:
#     def __int__(self):
#         return 0
#
#     def __str__(self):
#         return "Shape"
#
# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
#
#     def __int__(self):
#         return round(3.14159 * self.radius ** 2)
#
#     def __str__(self):
#         return f"Circle with radius {self.radius}"
#
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height
#
#     def __int__(self):
#         return self.width * self.height
#
#     def __str__(self):
#         return f"Rectangle with width {self.width} and height {self.height}"
#
#
# circle = Circle(5)
# print(int(circle))
# print(str(circle))
#
# rectangle = Rectangle(4, 6)
# print(int(rectangle))
# print(str(rectangle))


# 3 Задание

# Создайте базовый класс Shape для рисования плоских фигур.
# Определите методы:
# Show() — вывод на экран информации о фигуре;
# Save() — сохранение фигуры в файл;
# Load() — считывание фигуры из файла.
# Определите производные классы:
# Square — квадрат, который характеризуется координатами левого верхнего угла и длиной стороны;
# Rectangle — прямоугольник с заданными координатами верхнего левого угла и размерами;
# Circle — окружность с заданными координатами центра и радиусом;
# Ellipse — эллипс с заданными координатами верхнего
# угла описанного вокруг него прямоугольника со сторонами, параллельными осям координат, и размерами этого прямоугольника.
# Создайте список фигур, сохраните фигуры в файл, загрузите в другой список и отобразите информацию о каждой из фигур.


# import pickle
#
# class Shape:
#     def __init__(self, shape_type):
#         self.shape_type = shape_type
#
#     def show(self):
#         print(f"Тип фигуры: {self.shape_type}")
#
#     def save(self, file_name):
#         with open(file_name, 'wb') as file:
#             pickle.dump(self, file)
#
#     @classmethod
#     def load(cls, file_name):
#         with open(file_name, 'rb') as file:
#             return pickle.load(file)
#
# class Square(Shape):
#     def __init__(self, shape_type, x, y, side_length):
#         super().__init__(shape_type)
#         self.x = x
#         self.y = y
#         self.side_length = side_length
#
#     def show(self):
#         super().show()
#         print(f"Координаты левого верхнего угла: ({self.x}, {self.y})")
#         print(f"Длина стороны: {self.side_length}")
#
# class Rectangle(Shape):
#     def __init__(self, shape_type, x, y, width, height):
#         super().__init__(shape_type)
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def show(self):
#         super().show()
#         print(f"Координаты верхнего левого угла: ({self.x}, {self.y})")
#         print(f"Ширина: {self.width}")
#         print(f"Высота: {self.height}")
#
#
#
#
# shapes = [
#     Square("Квадрат", 3, 6, 5),
#     Rectangle("Прямоугольник", 2, 2, 6, 4)
# ]
#
#
# with open("shapes.pkl", 'wb') as file:
#     pickle.dump(shapes, file)
#
#
# with open("shapes.pkl", 'rb') as file:
#     loaded_shapes = pickle.load(file)
#
#
# for shape in loaded_shapes:
#     shape.show()
#
#
# # ---------------------2 версия----------------------
#
#
# import json
#
# class Shape:
#     def __init__(self, name):
#         self.name = name
#
#     def show(self):
#         print(f"Shape: {self.name}")
#
#     def save(self, filename):
#         with open(filename, 'w') as file:
#             json.dump(self.__dict__, file)
#
#     def load(self, filename):
#         with open(filename, 'r') as file:
#             data = json.load(file)
#             self.__dict__.update(data)
#
#
# class Square(Shape):
#     def __init__(self, name, x, y, side_length):
#         super().__init__(name)
#         self.x = x
#         self.y = y
#         self.side_length = side_length
#
#     def show(self):
#         super().show()
#         print(f"Position: ({self.x}, {self.y}), Side Length: {self.side_length}")
#
#
# class Rectangle(Shape):
#     def __init__(self, name, x, y, width, height):
#         super().__init__(name)
#         self.x = x
#         self.y = y
#         self.width = width
#         self.height = height
#
#     def show(self):
#         super().show()
#         print(f"Position: ({self.x}, {self.y}), Width: {self.width}, Height: {self.height}")
#
#
# class Circle(Shape):
#     def __init__(self, name, x, y, radius):
#         super().__init__(name)
#         self.x = x
#         self.y = y
#         self.radius = radius
#
# def show(self):
#         super().show()
#         print(f"Center: ({self.x}, {self.y}), Radius: {self.radius}")
#
#
# class Ellipse(Shape):
#     def __init__(self, name, x, y, major_axis, minor_axis):
#         super().__init__(name)
#         self.x = x
#         self.y = y
#         self.major_axis = major_axis
#         self.minor_axis = minor_axis
#
# def show(self):
#         super().show()
#         print(f"Center: ({self.x}, {self.y}), Major Axis: {self.major_axis}, Minor Axis: {self.minor_axis}")
#
#
#
# square = Square("Square", 0, 0, 5)
# square.show()
# square.save("square.json")
#
# loaded_square = Square("Loaded Square", 0, 0, 0)
# loaded_square.load("square.json")
# loaded_square.show()
