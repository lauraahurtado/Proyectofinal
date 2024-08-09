import requests as rq

class Personaje:
    def __init__(self, id, nombre, genero, altura, peso, color_cabello, color_ojos, color_piel, nacimiento, mundo_natal):
        self.id=id
        self.nombre=nombre
        self.genero=genero
        self.altura=altura
        self.peso=peso
        self.color_cabello=color_cabello
        self.color_ojos=color_ojos
        self.color_piel=color_piel
        self.nacimiento=nacimiento
        self.mundo_natal=mundo_natal

    def mostrar_personajes(self):
        print(f'\tid: {self.id}')
        print(f'\tNombre: {self.nombre}')
        print(f'\tGénero: {self.genero}')
        print(f'\tAltura: {self.altura}')
        print(f'\tPeso: {self.peso}')
        print(f'\tColor de Cabello: {self.color_cabello}')
        print(f'\tColor de ojos: {self.color_ojos}')
        print(f'\tColor de piel: {self.color_piel}')
        print(f'\tFecha de Nacimiento: {self.nacimiento}')
        print(f'\tMundo Natal: {self.mundo_natal}')

    def mostrar_nombre_personajes(self):
        print(f'    Nombre: {self.nombre}')

    def mostrar_personajes_opcion_cuatro(self,peliculas_obj,especies_obj,naves_obj,vehiculos_obj):
        print(f'\n>>  Nombre: {self.nombre}')
        informacion=rq.get(self.mundo_natal).json()
        print(f'    Nombre del planeta origen: {informacion['result']['properties']['name']}')
        for pelicula in peliculas_obj:
            for personaje in pelicula.personajes:
                if self.nombre==personaje.nombre:
                    print(f'    Titulos de los episodios: {pelicula.titulo}')
        print(f'    Genero: {self.genero}')
        for especie in especies_obj:
            for personaje in especie.nombres_personajes_pertenecientes_especies:
                if self.nombre==personaje.nombre:
                    print(f'    Especie: {especie.nombre}')
        for nave in naves_obj:
            for piloto in nave.pilotos:
                if self.nombre==piloto.nombre:
                    print(f'    Nave: {nave.nombre}')
        for vehiculo in vehiculos_obj:
            for piloto in vehiculo.pilotos:
                if self.nombre==piloto.nombre:
                    print(f'    Vehiculo: {vehiculo.nombre}')
        print('')
        
        
        