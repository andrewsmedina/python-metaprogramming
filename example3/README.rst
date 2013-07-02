attribute validator
===================

eg:

    class Product:
        name = String()
        age = Integer()


Solution - part 1
=================

Descriptors


Result:

    class Product:
        name = String('name')
        age = Integer('age')

Problem = part 2
================

Add the name of fields dynamically.

Soluction - part 2
==================

Metaclass


