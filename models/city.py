#!/usr/bin/python3
''' clase City que hereda de BaseModel '''

from models.base_model import BaseModel


class City(BaseModel):
    ''' Atributos de clase pública '''
    # Define ciudad para buscar
    state_id = ""
    name = ""
