class Typed:
    ty = object

    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError('Expected %s' % self.ty)


class String(Typed):
    ty = str


class Integer(Typed):
    ty = int


class Person:
    name = String()
    age = Integer()


person = Person()
person.name = 'andrews'
try:
    person.name = 1 #ops
except TypeError:
    pass

try:
    person.age = "ble"
except TypeError:
    pass
