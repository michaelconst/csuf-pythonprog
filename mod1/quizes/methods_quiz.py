import abc

class B(abc.ABC):
    @abc.abstractmethod
    def f(self, x, y):
        print('in B#f abstract method')

class D(B):
    def f(self, x, y, z=0):
        super().f(x, y)
        print('in D#f method')

b = D()
b.f(2, 3, 4)
b = B()
b.f(5, 6)
