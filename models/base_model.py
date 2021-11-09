#!/usr/bin/python3
""" Class BaseModel """

import uuid
from datetime import datetime


class BaseModel:
    """
    Clase base que define todos los
    atributos / métodos comunes para otras clases
    """
    def __init__(self):
        # Asigna id aleatorio
        self.id = str(uuid.uuid4)
        # Asigna fecha actual
        self.created_at = datetime.now().isoformat()
        # Actualiza la fecha de la ultima modificación
        self.updated_at = self.created_at

    def __str__(self):
        """ devuelve el nombre de la clase, el ID y
        el diccionario de atributos """
        return ("[{}] ({}) {}"
                .format(self.__class__.__name__, self.id, self.__dic__))

    def save(self):
        """ actualiza el atributo de instancia pública
        updated_at con la fecha y hora actual """
        self.updated_at = datatime.now().isoformat()

    def to_dict(self):
        """ devuelve un diccionario que contiene todas
        las claves / valores de __dict__ de la instancia """
        dictionary = self.__dict__
        dictionary[self.__class__.__name__] = s
        return dictionary
