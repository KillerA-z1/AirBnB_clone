# AirBnB clone Project
---
## Description

This project is the first step towards building an AirBnB clone. The goal is to create a command interpreter that manages AirBnB objects, including a parent class (`BaseModel`), several classes for AirBnB objects(e.g., `User`, `State`, `City`, `Place`,…),
and a simple file storage engine.

## Features

- Command interpreter for managing AirBnB objects
- Serialization and deserialization of objects to JSON
- Classes for User, State, City, Place, and more

## Installation

```bash
$ git clone https://github.com/KillerA-z1/AirBnB_clone.git
```

## Usage

To start the command interpreter, run the `console.py` file:

```bash
./console.py
```
Or run it in non-interactive mode:
```bash
echo "help" | ./console.py
```
## Example Usage

Here are some example commands you can use in the console:

- Create a new `User`:

    ```bash
    (hbnb) create User
    ```

    This will create a new `User` and print its `id`.

- Show the details of a `User`:

    ```bash
    (hbnb) show User <id>
    ```

    Replace `<id>` with the `id` of a `User`. This will print the details of the `User`.

Remember to replace `<id>` with an actual ID from your application.

## Tests

This project includes a test suite for validating the functionality of the command interpreter and the classes. 

To run the tests, navigate to the `tests` directory and run the following command:

```bash
python3 -m unittest discover tests
 ```
Or to run the test file by file run the following command:: 
```bash
python3 -m unittest tests/test_models/test_base_model.py
```

## Commands
In the console, you can create a new object, show an object, delete an object, and do many other operations.

- `create <class>`: Creates a new instance of `<class>`, saves it to the file, and prints its id.
- `show <class> <id>`: Prints the string representation of an instance based on the class name and id.
- `destroy <class> <id>`: Deletes an instance based on the class name and id.
- `all <class>` or `all`: Prints all string representation of all instances based or not on the class name.
- `update <class> <id> <attribute name> <attribute value>`: Updates an instance based on the class name and id by adding or updating attribute.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## Author :black_nib:

* Ahmed Abdulwahid - [KillerA-z1](https://github.com/KillerA-z1)
