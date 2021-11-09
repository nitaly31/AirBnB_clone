#!/usr/bin/python3
''' clase Amenity que hereda de BaseModel '''

from models.base_model import BaseModel


class Amenity(BaseModel):
    ''' Atributos de clase pública '''
    # Define las comodidades que el usuario
    # puede elegir para ofrecer en su lugar
    name = ""
