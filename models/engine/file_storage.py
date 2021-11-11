#!/usr/bin/python3
''' Clase FileStorage que serializa instancias en un archivo JSON y
deserializa un archivo JSON en instancias '''

import json
from models.basemodel import BaseModel


class FileStorage:
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
        FileStorage.__objects[key] = obj

    def save(self):
        ''' Serializa __objects en el archivo JSON (ruta: __file_path) '''
        dic_obj = {}
        # Recorro los valores ingresados
        for key, value in self.__objects.items():
            # Asigno el valor al dic_obj en su clave
            dic_obj[key] = vlaue.to_dic()
        # Creo el archivo json donde se almacenara la información a serializar
        with open(FileStorage.file_path, "w", encoding="utf-8") as f:
            # Convierte los objetos de Python en objetos json apropiados para
            # almacenarse en un archivo
            json.dump(dic_obj, f, indent="")

    def reload(self):
        ''' Deserializa el archivo JSON a __objects
        (solo si el archivo JSON (__file_path) existe; de ​​lo contrario,
        si el archivo no existe, no se debe generar ninguna excepción) '''
        file = FileStorage.__file_path
        class_dic = {'BaseModel': BaseModel, 'User': User}
        try:
            # Se abre el archivo para lectura
            with open(file, "r", encoding="utf-8") as f:
                # Se deserializa el archivo
                json_dic = json.load(f)
                # Se recorre el contenido del archivo deserializado
                for key, value in json_dic.items():
                    # Establece los nuevos valores del objeto
                    self.new(class_dic[value['__class__']]('**value'))
        # Se genera cuando se solicita un archivo o directorio pero no existe
        except FileNotFoundError:
            pass
