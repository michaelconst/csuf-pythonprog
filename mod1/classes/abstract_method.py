import abc


class Shape:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def draw(self):
        '''draw the shape'''


class Circle(Shape):
    def draw(self):
        print('drawing the circle')


if __name__ == '__main__':
    shape = Shape()