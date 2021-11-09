#!/usr/bin/python3
''' clase State que hereda de BaseModel '''

from models.base_model import BaseModel


class State(BaseModel):
    ''' Atributos de clase pública '''
    # clase para crear un estado
    name = ""
