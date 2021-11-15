#!/usr/bin/python3
''' Clase FileStorage que serializa instancias en un archivo JSON y
deserializa un archivo JSON en instancias '''

import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


date = {"BaseModel": BaseModel, "User": User, "State": State,
        "Place": Place, "City": City, "Amenity": Amenity, "Review": Review}


class FileStorage:
    ''' Clase que gestiona el almacenamiento de modelos
        hbnb en formato JSON '''
    # cadena: ruta al archivo JSON
    __file_path = "file.json"
    # diccionario - vacío
    __objects = {}

    def all(self):
        ''' Devuelve el diccionario __objects '''
        return FileStorage.__objects

    def new(self, obj):
        ''' establece en __objects el obj con la clave <obj class name>.id '''
        # Almacenará todos los objetos por <nombre de clase>.id
        # Ej. Para almacenar un objeto BaseModel con id = 12121212,
        # la clave será BaseModel.12121212
        key = obj.__class__.__name__ + "." + obj.id
        self.__objects[key] = obj

    def save(self):
        ''' Serializa __objects en el archivo JSON (ruta: __file_path) '''
        dic_obj = {}
        # Operación de escritura:
        # Creo el archivo json donde se almacenara la información a serializar
        with open(self.__file_path, "w", encoding="utf-8") as f:
            # Recorro los valores ingresados
            for key, value in self.__objects.items():
                # Asigno el valor al dic_obj en su clave
                dic_obj[key] = value.to_dict()
                # Convierte los objetos de Python en objetos json apropiados
                # para almacenarse en un archivo
            json.dump(dic_obj, f)

    def reload(self):
        '''
        Deserializa el archivo JSON a __objects
        (solo si el archivo JSON (__file_path) existe; de ​​lo contrario,
        si el archivo no existe, no se debe generar ninguna excepción)
        '''
        try:
            # Operación de lectura:
            # Se abre el archivo para lectura
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                # Se deserializa el archivo
                j_dic = json.load(f)
            # Se recorre el contenido del archivo deserializado
            for key in j_dic:
                value = date[j_dic[key]["__class__"]](**j_dic[key])
                # Establece los nuevos valores del objeto
                self.__objects[key] = value
        # Se genera cuando se solicita un archivo o directorio pero no existe
        except FileNotFoundError:
            pass
