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
        print(f'\tNombre: {self.nombre}')

    

        
        