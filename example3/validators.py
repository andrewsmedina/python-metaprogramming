class Typed:
    ty = object

    def __init__(self, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError('Expected %s' % self.ty)
        instance.__dict__[self.name] = value

class String(Typed):
    ty = str


class Integer(Typed):
    ty = int


class Person:
    name = String('name')
    age = Integer('age')


person = Person()
person.name = 'andrews'
print(person.name)
try:
    person.name = 1 #ops
except TypeError:
    pass

try:
    person.age = "ble"
except TypeError:
    pass


class OldPerson:
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError('Expected str')
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError('Expected int')
        self._age = value

p = OldPerson()
try:
    p.name = 10
except TypeError:
    pass
