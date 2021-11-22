# 0x01. AirBnB clone - Web static :house_with_garden:

![HNBN](https://github.com/nitaly31/AirBnB_clone/blob/master/web_static/images/HBNB-HolbertonAirbnb.png)

### 📝 Descripción
***
__Airbnb__ is an online platform that connects people who have a home to offer, with people who need a place to stay temporarily.

The first stage of the project was where we started to create The AirBnB Clone and we created a shell to manage the AirBnB objects.

This first stage of the project focused on everything related to Python:

`Import`,` Exceptions`, `Class`, `Private attribute`, `Getter / Setter`, `Class method`, `Static method`, `Inheritance`, `Unittest`, `Read / Write file`, `args` and `kwargs`, `Serialization` / `Deserialization` and `JSON`.

Now that you have a command interpreter for managing your AirBnB objects, it’s time to make them alive!

Before developing a big and complex web application, we will build the front end step-by-step.

The first step is to “design” / “sketch” / “prototype” each element:
* Create simple HTML static pages
* Style guide
* Fake contents
* No Javascript
* No data loaded from anything

__*HTML*__ (HyperText Markup Language)

Provide structure and meaning to content by defining that content, such as headings, paragraphs, or images. Es the structure of your page, it should be the first thing to write.

__*CSS*__ (Cascading Style Sheets)

It is a presentation language created to style the appearance of content, using, for example, fonts or colors. Is the styling of your page, the design.

Phases of the AirBnB clone project:
- [x] **The console**
- [x] **HTML**
- [ ] MySQL
- [ ] Fabric
- [ ] Flask
- [ ] REST API
- [ ] Web dynamic

### 📋 Requirements
***
#### Python Scripts

* Allowed editors: `vi`, `vim`, `emacs`.
* Files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5).
* Files must be executable.
* The length of your files will be tested using `wc`.

#### Python Unit Tests

* All your test files should be inside a folder `tests`.
* You have to use the unittest module.
* All your test files should be python files (extension: `.py`).
* All your test files and folders should start by `test_`.
* All your tests should be executed by using this command: `python3 -m unittest discover tests`.

#### HTML and CSS

* Allowed editors: `vi`, `vim`, `emacs`.
* All your CSS files should be in `styles` folder.
* All your images should be in `images` folder.
* You are not allowed to use `!important` and `id` (`#...` in the CSS file).
* You are not allowed to use tags `img`, `embed` and `iframe`.
* You are not allowed to use Javascript.
* No cross browsers.

### 🎨 Style
***
* Code should use the PEP 8 style (version 2.7.*).
* Your code should be W3C compliant and validate with `W3C-Validator`.

### 🎯 Repository Projects
***
#### Tasks Python:
| Files | Description |
| --- | --- |
| [`models/base_model.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/models/base_model.py) | Defines all common attributes/methods for other classes. |
| [`models/engine/file_storage.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/models/engine/file_storage.py) | Serializes instances to a JSON file and deserializes JSON file to instances. |
| [`console.py`]() | Contains the entry point of the command interpreter. |
| [`models/user.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/models/user.py) | Defines subclass User. |
| [`models/state.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/models/state.py) | Defines subclass State. |
| [`models/city.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/models/city.py) | Defines subclass City. |
| [`models/amenity.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/models/amenity.py) | Defines subclass Amenity |
| [`models/place.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/models/place.py) | Place file that contains detailed information about the place to be rented. |
| [`models/review.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/models/review.py) | Defines subclass Review. |
| [`tests/test_console.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/tests/test_console.py) | unittests for console. |
| [`tests/test_models/test_base_model.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/tests/test_models/test_base_model.py) | unittests for base_model. |
| [`tests/test_models/test_user.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/tests/test_models/test_user.py) | Unittests for user. |
| [`tests/test_models/test_state.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/tests/test_models/test_state.py) | Unittests for state. |
| [`tests/test_models/test_city.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/tests/test_models/test_city.py) | Unittests for city. |
| [`tests/test_models/test_amenity.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/tests/test_models/test_amenity.py) | Unittests for amenity. |
| [`tests/test_models/test_place.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/tests/test_models/test_place.py) | Unittests for place. |
| [`tests/test_models/test_review.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/tests/test_models/test_review.py) | Unittests for review. |
| [`tests/test_models/test_engine/test_file_storage.py`](https://github.com/nitaly31/AirBnB_clone/blob/master/tests/test_models/test_engine/test_file_storage.py) | Unittests for file_storage. |

#### Folders:
| Folders | Description |
| --- | --- |
| [`models/`](https://github.com/nitaly31/AirBnB_clone/tree/master/models) | Folder containing the Airbnb base structure models. |
| [`models/engine/`](https://github.com/nitaly31/AirBnB_clone/tree/master/models/engine) | Folder containing storage engine abstracted from the project: File storage. |
| [`tests/`](https://github.com/nitaly31/AirBnB_clone/tree/master/tests) | Folder that contains all unittests to validate all our classes and storage engine. |
| [`tests/test_models`](https://github.com/nitaly31/AirBnB_clone/tree/master/tests/test_models) | Folder containing all unit test files in the `models` folder. |
| [`tests/test_models/test_engine`](https://github.com/nitaly31/AirBnB_clone/tree/master/tests/test_models/test_engine) | Folder containing all unit test files in the `engine` subfolder. |
| [`web_static/`](https://github.com/nitaly31/AirBnB_clone/tree/master/web_static) | Contains the main HTML files for the structure of a static page. |
| [`web_static/images/`](https://github.com/nitaly31/AirBnB_clone/tree/master/web_static/images) | Contains the images used in the page or repository. |
| [`web_static/styles/`](https://github.com/nitaly31/AirBnB_clone/tree/master/web_static/styles) | Contains the CSS files for the manipulation of styles on the page. |

### :computer: Console
***
#### Description of the command interpreter :clipboard:

the console contains the entry point of the command interpreter.

### 🛠️ Installation
***
1. Clone this repository:
`https://github.com/nitaly31/AirBnB_clone.git`
2. Access AirBnb directory:
`cd AirBnB_clone`
3. Run hbnb(interactively)
```bash
root@c698ec171c6e:/home/AirBnB_clone# ./console
```
4. When this command is run the following prompt should appear:
```bash
(hbnb)
```
5. This prompt designates you are in the "HBnB" console. There are a variety of commands available within the console program.

| Command | Description |
| --- | --- |
| `create` | Creates a new instance of `BaseModel`, saves it (to the JSON file) and prints the `id`. |
| `show` | Prints the string representation of an instance based on the class name and `id`. |
| `destroy` | Deletes an instance based on the class name and `id` (save the change into the JSON file). |
| `all` | Prints all string representation of all instances based or not on the class name. |
| `update` | Updates an instance based on the class name and `id` by adding or updating attribute (save the change into the JSON file). |
| `quit` and `EOF`| To exit the program. |
| `help` | Shows the commands that can be used in the console. |

### 🧪 Testing
***

```bash
root@c698ec171c6e:/home/AirBnB_clone# ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

##### all
```bash
(hbnb) User.all()
[[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}, [User] (38f22813-2753-4d42-b37c-57a17f1e4f88) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848279), 'updated_at': datetime.datetime(2017, 9, 28, 21, 11, 42, 848291), 'password': 'b9be11166d72e9e3ae7fd407165e4bd2', 'email': 'airbnb@mail.com', 'id': '38f22813-2753-4d42-b37c-57a17f1e4f88'}]
(hbnb) 
```

##### show
```bash
(hbnb) User.show("246c227a-d5c1-403d-9bc7-6a47bb9f0f68")
[User] (246c227a-d5c1-403d-9bc7-6a47bb9f0f68) {'first_name': 'Betty', 'last_name': 'Bar', 'created_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611352), 'updated_at': datetime.datetime(2017, 9, 28, 21, 12, 19, 611363), 'password': '63a9f0ea7bb98050796b649e85481845', 'email': 'airbnb@mail.com', 'id': '246c227a-d5c1-403d-9bc7-6a47bb9f0f68'}
(hbnb) User.show("Bar")
** no instance found **
(hbnb) 
```

#### create
```bash
(hbnb) create BaseModel
49faff9a-6318-451f-87b6-910505c55907
(hbnb) all BaseModel
["[BaseModel] (49faff9a-6318-451f-87b6-910505c55907) {'created_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903293), 'id': '49faff9a-6318-451f-87b6-910505c55907', 'updated_at': datetime.datetime(2017, 10, 2, 3, 10, 25, 903300)}"]
(hbnb)
```

### :black_nib: Authors
***
*Holberton School Students*

Yuri Quezada - [Github](https://github.com/yuriquezada) | [LinkedIn](https://www.linkedin.com/in/yuriquezada/)

Geraldine Meneses - [Github](https://github.com/nitaly31) | [LinkedIn](https://www.linkedin.com/in/geraldine-meneses/)
