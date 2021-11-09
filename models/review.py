#!/usr/bin/python3
''' Clase Review que hereda de BaseModel '''

from models.base_model import BaseModel


class Review(BaseModel):
    ''' Atributos de clase pública '''
    # Reseñas realizadas por usuarios sobre un lugar
    place_id = ""
    user_id = ""
    text = ""
