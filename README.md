# *Holberton - Airbnb Clone*

![HBNB](https://camo.githubusercontent.com/4b17643aef1109cde7773d0aeaac596f81575c35c202e6e63b1cbc8aef236b37/68747470733a2f2f7777772e74616262796b61747a2e636f6d2f68626e622e706e67)

### Table of contents

- [Description](#description)
- [Files](#files)
- [Tests](#tests)
- [Console](#console)
- [Usage](#usage)
- [Examples](#examples)
- [Resources](#resources)
- [Credits](#credits)

## Description

This is our implementation of an Airbnb website. In this project we implemented a basic command interpreter interface
and different data models such as Amenities, cities, users, etc.

## Files

- *`Authors`* - File that contains project authors.
- *`README.md`* - File that contains project description.

### Console
- *`console.py`* - Command interpreter entry point.

### Engine
- *`file_storage.py`* - Class *`FileStorage`* that serializes instances to a JSON file and deserializes JSON file to instances

### Models
- *`amenity.py`* - Class *`Amenity`* that inherits from *BaseModel*.
- *`base_model.py`* - Class *`BaseModel`* that defines common attributes/methods for other classes.
- *`city.py`* - Class *`City`* that inherits from *BaseModel*.
- *`place.py`* - Class *`Place`* that inherits from *BaseModel*.
- *`review.py`* - Class *`Review`* that inherits from *BaseModel*.
- *`state.py`* - Class *`State`* that inherits from *BaseModel*.
- *`user.py`* - Class *`User`* that inherits from *BaseModel*.

## Tests

- *`test_amenity.py`* - Unittest for amenity.
- *`test_base_model.py`* - Unittest for base_model.
- *`test_city.py`* - Unittest for city.
- *`test_place.py`* - Unittest for place.
- *`test_review.py`* - Unittest for review.
- *`test_state.py`* - Unittest for state.
- *`test_user.py`* - Unittest for user.
- *`test_file_storage.py`* - Unittest for file_storage.

*Test files are saved in `test\test_models\`*

## Console

This is the main entry point to our command interpreter. To start the command interpreter, run this command:

```c
./console.py
```

## Usage
The interpreter provides commands to interact with the page. The command syntax is the following:

```c
command model [argument_1 argument_2 ...]
```

## Examples
Here are some eamples of the interpreter commands
- Create a User:

```c
create User
```

- Display user (user_id is retrieved when creating the user):

```c
show User 'user_id'
```

- Update User:

```c
update User 'user_id' attribute_name attribute_value
```

- Close interpreter:

```c
quit
```

---

## Resources

- *[Cmd module](https://docs.python.org/3.4/library/cmd.html)*
- *[Uuid module](https://docs.python.org/3.4/library/uuid.html)*
- *[Datetime](https://docs.python.org/3.4/library/datetime.html)*
- *[Unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)*
- *[Args/kwargs](https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/)*
- *[Python test cheatsheet](https://www.pythonsheets.com/notes/python-tests.html)*
- *[Packages concept page](https://www.geeksforgeeks.org/python-packages/)*

## Credits

- *[Louis Toro](https://github.com/Ltoro9)*
- *[Jonathan Pérez](https://github.com/prodjohnper)*
