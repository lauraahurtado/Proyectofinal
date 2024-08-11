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
        self.color_piel=color_piel
        self.color_ojos=color_ojos
        self.lengua_materna=lengua_materna
        self.mundo_natal=mundo_natal
        self.nombres_personajes_pertenecientes_especie=nombres_personajes_pertenecientes_especie

    def mostrar_especies(self,peliculas_obj):
        print(f'\n>>  id: {self.id}')
        print(f'    - Nombre: {self.nombre}')
        print(f'    - Altura: {self.altura}')
        print(f'    - Clasificacion: {self.clasificacion}')
        print(f'    - Nombre del planeta de origen: {rq.get(self.mundo_natal).json()['result']['properties']['name']}')
        print(f'    - Lengua materna: {self.lengua_materna}')
        for personaje in self.nombres_personajes_pertenecientes_especie:
            personaje.mostrar_nombre_personajes()
        lista_episodios=[]
        for x in peliculas_obj:
            for y in x.especies:
                if y.nombre==self.nombre:
                    lista_episodios.append(x.titulo)
        for episodio in lista_episodios:
            print(f'    - Episodio: {episodio}')
        


    