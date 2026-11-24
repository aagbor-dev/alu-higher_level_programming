# Python - Almost a circle

A small project that builds classes for geometric shapes with Python.

- `models/base.py`: the Base class, which manages the id of all the other classes
- `models/rectangle.py`: the Rectangle class, with validated attributes and an area method
- `tests/`: unittests for both classes, run with `python3 -m unittest discover tests`
- `models/square.py`: the Square class, which inherits from Rectangle
- Rectangle also has `display()`, `__str__()` and `update()`
- Square has a `size` property and its own `update()`
- `to_dictionary()` on Rectangle and Square returns a dictionary of the attributes
- `Base.to_json_string()` turns a list of dictionaries into a JSON string
- `Base.save_to_file()` writes a list of instances to `<Class name>.json`
- `Base.from_json_string()` turns a JSON string back into a list
- `Base.create()` builds an instance from a dictionary
- `Base.load_from_file()` reads the instances saved in `<Class name>.json`
