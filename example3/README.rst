attribute validator
===================

eg:

    class Person:
        name = String()
        age = Integer()


Solution - part 1
=================

Descriptors


Result:

    class Person:
        name = String('name')
        age = Integer('age')

Problem = part 2
================

Add the name of fields dynamically.

Soluction - part 2
==================

Metaclass


