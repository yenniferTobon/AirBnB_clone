# AirBnB clone - The console
# Description
The AirBnB console is used to store a powerful storage system. This storage engine will give us abstraction between my project “My object” and “How they are stored and persisted”.
This abstraction will also allow you to change the type of storage easily without updating all of your codebase.
## Usage
To start the AirBnB console cd into the project
```sh
$ cd AirBnB_clone
```
Then run the console with
```sh
$ ./console.py
```
You will be prompt with the command interpreter
```sh
(hbnb)
```
Now you are ready to start using it.
The following is the AirBnb console functionality
* quit - This will close the AirBnB console.
* help - This will give you information on how to use the AirBnB console commands.
* create <BaseModel> - Creates a new instance that inheritance from BaseModel class.
* show <BaseModel> <id> - Displays a BaseModel instance object given its id.
* destroy <BaseModel> <id> - Destroys a BaseModel instance object given its id.
* all <optional><BaseModel> - Displays all BaseModel instance objects
* update <BaseModel> <id> <attribute> <value> - Adds or updates a new attribute for a BaseModel instance object given its id and value.
# Example
```sh
(hbnb) create User
e179b963-1d28-4d70-a817-496447137b2a
(hbnb) create Place
98f4f95c-8e11-420d-a728-66450a6c946f
(hbnb) show User e179b963-1d28-4d70-a817-496447137b2a
[User] (e179b963-1d28-4d70-a817-496447137b2a) {'updated_at': datetime.datetime(2019, 11, 13, 10, 52, 2, 874416), 'id': 'e179b963-1d28-4d70-a817-496447137b2a', 'created_at': datetime.datetime(2019, 11, 13, 10, 52, 2, 874493)}
(hbnb) all
["[User] (e179b963-1d28-4d70-a817-496447137b2a) {'updated_at': datetime.datetime(2019, 11, 13, 10, 52, 2, 874416), 'id': 'e179b963-1d28-4d70-a817-496447137b2a', 'created_at': datetime.datetime(2019, 11, 13, 10, 52, 2, 874493)}", "[Place] (98f4f95c-8e11-420d-a728-66450a6c946f) {'updated_at': datetime.datetime(2019, 11, 13, 10, 52, 12, 718413), 'id': '98f4f95c-8e11-420d-a728-66450a6c946f', 'created_at': datetime.datetime(2019, 11, 13, 10, 52, 12, 718462)}"]
(hbnb) destroy Place 98f4f95c-8e11-420d-a728-66450a6c946f
(hbnb) show Place 98f4f95c-8e11-420d-a728-66450a6c946f
** no instance found **
(hbnb) all
["[User] (e179b963-1d28-4d70-a817-496447137b2a) {'updated_at': datetime.datetime(2019, 11, 13, 10, 52, 2, 874416), 'id': 'e179b963-1d28-4d70-a817-496447137b2a', 'created_at': datetime.datetime(2019, 11, 13, 10, 52, 2, 874493)}"]
(hbnb) update User e179b963-1d28-4d70-a817-496447137b2a name "Jhon Doe"
(hbnb) show User e179b963-1d28-4d70-a817-496447137b2a
[User] (e179b963-1d28-4d70-a817-496447137b2a) {'updated_at': datetime.datetime(2019, 11, 13, 10, 52, 2, 874416), 'id': 'e179b963-1d28-4d70-a817-496447137b2a', 'name': 'Jhon Doe', 'created_at': datetime.datetime(2019, 11, 13, 10, 52, 2, 874493)}
(hbnb) quit
```
# Authors
* Yennifer Tobon Yate (https://github.com/yenniferTobon)
* Joshua Hernandez (https://github.com/joshuaciencia)
