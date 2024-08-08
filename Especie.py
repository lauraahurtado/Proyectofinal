import requests as rq
from Personaje import Personaje
class Especie:
    def __init__(self, id, nombre, clasificacion, designacion, altura, vida_promedio, color_cabello, color_piel, color_ojos, lengua_materna, mundo_natal, nombres_personajes_pertenecientes_especie):
        self.id=id
        self.nombre=nombre
        self.clasificacion=clasificacion
        self.designacion=designacion
        self.altura=altura
        self.vida_promedio=vida_promedio
        self.color_cabello=color_cabello
        self.color_piel=color_cabello
        self.color_ojos=color_ojos
        self.lengua_materna=lengua_materna
        self.mundo_natal=mundo_natal
        self.nombres_personajes_pertenecientes_especies=nombres_personajes_pertenecientes_especie

    