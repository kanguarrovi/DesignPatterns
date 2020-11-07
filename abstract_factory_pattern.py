from abc import ABC, abstractmethod

# From https://www.tutorialspoint.com/design_pattern/abstract_factory_pattern.htm

class Shape:

    def draw(self):
        pass


class RoundedRectangle(Shape):

    def draw(self):
        print("Inside RoundedRectangle::draw() method.")


class RoundedSquare(Shape):

    def draw(self):
        print("Inside RoundedSquare::draw() method.")


class Rectangle(Shape):

    def draw(self):
        print("Inside Rectangle::draw() method.")


class Square(Shape):

    def draw(self):
        print("Inside Square::draw() method.")


class AbstractFactory(ABC):

    def __init__(self):
        super().__init__()

    @staticmethod
    @abstractmethod
    def get_shape(shape_type: str):
        pass


class ShapeFactory(AbstractFactory):

    @staticmethod
    def get_shape(shape_type):
        if shape_type.upper() == "RECTANGLE":
            return Rectangle()
        elif shape_type.upper() == "SQUARE":
            return Square()
        else:
            return None


class RoundedShapeFactory(AbstractFactory):

    @staticmethod
    def get_shape(shape_type):
        if shape_type.upper() == "RECTANGLE":
            return RoundedRectangle()
        elif shape_type.upper() == "SQUARE":
            return RoundedSquare()
        else:
            return None


def factory_producer(rounded=False):
    return RoundedShapeFactory() if rounded else ShapeFactory()


if __name__ == "__main__":

    # get shape factory
    shapeFactory = factory_producer()
    # get an object of Shape Rectangle
    shape1 = shapeFactory.get_shape(shape_type="RECTANGLE")
    # call draw method of Shape Rectangle
    shape1.draw()
    # get an object of Shape Square
    shape2 = shapeFactory.get_shape(shape_type="SQUARE")
    # call draw method of Shape Square
    shape2.draw()
    # get shape factory
    shapeFactory1 = factory_producer(rounded=True)
    # get an object of Shape Rectangle
    shape3 = shapeFactory1.get_shape(shape_type="RECTANGLE")
    # call draw method of Shape Rectangle
    shape3.draw()
    # get an object of Shape Square
    shape4 = shapeFactory1.get_shape(shape_type="SQUARE")
    # call draw method of Shape Square
    shape4.draw()
