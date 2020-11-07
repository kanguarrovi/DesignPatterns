# https://www.tutorialspoint.com/design_pattern/factory_pattern.htm

class Shape:

    def draw(self):
        pass


class Rectangle(Shape):

    def draw(self):
        print("Inside Rectangle::draw() method.")


class Square(Shape):

    def draw(self):
        print("Inside Square::draw() method.")


class Circle(Shape):

    def draw(self):
        print("Inside Circle::draw() method.")


def shape_factory(shape_type: str):
    if not shape_type:
        return None
    elif shape_type.upper() == 'CIRCLE':
        return Circle()
    elif shape_type.upper() == 'SQUARE':
        return Square()
    elif shape_type.upper() == 'RECTANGLE':
        return Rectangle()
    else:
        return None


# get an object of Circle and call its draw method.
shape1 = shape_factory("CIRCLE")

# call draw method of Circle
shape1.draw()

# get an object of Rectangle and call its draw method.
shape2 = shape_factory("RECTANGLE")

# call draw method of Rectangle
shape2.draw()

# get an object of Square and call its draw method.
shape3 = shape_factory("SQUARE")

# call draw method of square
shape3.draw()

#  https://realpython.com/python-interface/
#  https://www.tutorialspoint.com/design_pattern/factory_pattern.html
#  https://www.tutorialspoint.com/design_pattern/proxy_pattern.htm