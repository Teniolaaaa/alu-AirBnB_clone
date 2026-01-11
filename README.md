# AirBnB Clone - The Console

## Description

This is the first step towards building a full web application: the AirBnB clone. This project implements a command-line interpreter (console) to manage AirBnB objects.

The console provides a simple interface to:
- Create new objects (User, State, City, Place, etc.)
- Retrieve objects from file storage
- Perform operations on objects (count, compute stats, etc.)
- Update object attributes
- Destroy objects

This project implements:
- A parent class `BaseModel` for initialization, serialization, and deserialization
- A simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- All classes for AirBnB (User, State, City, Place, Amenity, Review) that inherit from BaseModel
- An abstracted storage engine: File storage
- Comprehensive unit tests to validate all classes and the storage engine

## Command Interpreter

### How to Start

To start the console in interactive mode:
```bash
./console.py
```

### How to Use

The console supports the following commands:

- `quit` or `EOF` - Exit the console
- `help` - Display help information
- `create <class>` - Create a new instance of a class
- `show <class> <id>` - Display an instance based on class name and ID
- `destroy <class> <id>` - Delete an instance based on class name and ID
- `all [class]` - Display all instances, or all instances of a specific class
- `update <class> <id> <attribute> <value>` - Update an instance attribute

### Examples

**Interactive mode:**
```bash
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit  create  show  destroy  all  update

(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) show BaseModel 49faff9a-6318-451f-87b6-910505c55907
[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'id': '49faff9a-6318-451f-87b6-910505c55907', 'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb) update BaseModel 49faff9a-6318-451f-87b6-910505c55907 first_name "Betty"
(hbnb) destroy BaseModel 49faff9a-6318-451f-87b6-910505c55907
(hbnb) quit
$
```

**Non-interactive mode:**
```bash
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit  create  show  destroy  all  update
(hbnb)
$
```

## Files and Directories

- `console.py` - Command interpreter entry point
- `models/` - Contains all model classes
  - `base_model.py` - BaseModel class, parent of all models
  - `user.py` - User class
  - `state.py` - State class
  - `city.py` - City class
  - `amenity.py` - Amenity class
  - `place.py` - Place class
  - `review.py` - Review class
  - `engine/file_storage.py` - FileStorage class for object serialization/deserialization
- `tests/` - Contains all unit tests

## Testing

Run all tests:
```bash
python3 -m unittest discover tests
```

Run a specific test file:
```bash
python3 -m unittest tests/test_models/test_base_model.py
```

## Authors

See the [AUTHORS](AUTHORS) file for a list of contributors to this project.
