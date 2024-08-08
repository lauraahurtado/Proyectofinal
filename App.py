### IMPORTACION DE EXTENSIONES Y CLASES

import requests as rq
import json
from Pelicula import Pelicula
from Especie import Especie
from Nave import Nave
from Personaje import Personaje
from Planeta import Planeta
from Vehiculo import Vehiculo
from Mision import Mision











# CREACION DE LA CLASE APP
class App:
    peliculas_obj=[]
    personajes_obj=[]
    naves_obj=[]
    vehiculos_obj=[]
    especies_obj=[]
    planetas_obj=[]
    misiones_obj=[]
    cantidad_misiones=0






    def cargar_API(self,link):
        informacion=rq.get(link).json()
        return informacion
    
    def start(self):
        
        try:
            peliculas=self.cargar_API('https://www.swapi.tech/api/films/')
            self.crear_peliculas(peliculas['result'])
            self.crear_personajes()
            self.crear_especies()
            self.crear_planetas()
            self.crear_naves()
            self.crear_vehiculos()
        except:
            print('''Está fallando la carga de la API, por conexión a internet u otro motivo.
                    Vuelva a correr el programa.''')
            




### MENÚ DEL PROGRAMA
        while True:
            menu=input('''Ingrese el índice numérico correspondiente a la opcion del menu que desea realizar:
1. Ver lista de Peliculas
2. Ver listado de todas las especies de la saga, ordenados por el ID
3. Ver lista de planetas
4. Buscar un personaje de la saga
5. Gráfico de cantidad de personajes nacidos en cada planeta
6. Gráficos de características de naves
7. Tabla estadística sobre naves
8. Construir Mision
9. Modificar Mision                       
10. Visualizar Mision                                           
11. Salir
--->:''')
            
            if menu=="1":
                for pelicula in self.peliculas_obj:
                    pelicula.mostrar_peliculas()


            elif menu=='2':
                None

            elif menu=='3':
                for planeta in self.planetas_obj:
                    planeta.mostrar_planetas(self.peliculas_obj,self.personajes_obj)

            elif menu=='4':
                None

            elif menu=='5':
                None

            elif menu=='6':
                None

            elif menu=='7':
                None

            elif menu=='8':
                None

            elif menu=='9':
                None

            elif menu=='10':
                None

            elif menu=='11':
                
                print('Hasta la proxima aventura estelar')
                break

            else:
                print('Ingrese una opcion contemplada en el menu: ')

### CREACION DE OBJETOS TIPO (Pelicula) CON LOS DATOS DE LA API

    def crear_peliculas(self,peliculas):
        count=0
        for pelicula in peliculas:
            if count==0:
                print('pelicula')
                personajes_pelicula=[]
                planetas_pelicula=[]
                naves_pelicula=[]
                vehiculos_pelicula=[]
                especies_pelicula=[]

                for personaje in pelicula['properties']['characters']:
                    print('pelicula personaje')
                    informacion=rq.get(personaje).json()
                    id=informacion["result"]["uid"]
                    informacion=informacion['result']['properties']
                    personajes_pelicula.append(Personaje(id,informacion["name"],informacion["gender"],informacion["height"],informacion["mass"],informacion["hair_color"],informacion["eye_color"],informacion["skin_color"],informacion["birth_year"],informacion["homeworld"]))

                for planeta in pelicula['properties']['planets']:
                    print('pelicula planeta')
                    informacion=rq.get(planeta).json()
                    informacion=informacion['result']['properties']
                    planetas_pelicula.append(Planeta(informacion["name"],informacion["diameter"],informacion["rotation_period"],informacion["orbital_period"],informacion["gravity"],informacion["population"],informacion["climate"],informacion["terrain"],informacion["surface_water"]))

                for nave in pelicula['properties']['starships']:
                    print('pelicula nave')
                    informacion=rq.get(nave).json()
                    informacion=informacion['result']['properties']
                    pilotos_nave=[]
                    for piloto in informacion['pilots']:
                        print('piloto-nave')
                        informacion_nave=rq.get(piloto).json()
                        id=informacion_nave['result']['uid']
                        informacion_nave=informacion_nave['result']['properties']
                        pilotos_nave.append(Personaje(id,informacion_nave["name"],informacion_nave["gender"],informacion_nave["height"],informacion_nave["mass"],informacion_nave["hair_color"],informacion_nave["eye_color"],informacion_nave["skin_color"],informacion_nave["birth_year"],informacion_nave["homeworld"]))
                    naves_pelicula.append(Nave(informacion["name"],informacion["model"],informacion["manufacturer"],informacion["cost_in_credits"],informacion["length"],informacion["max_atmosphering_speed"],informacion["crew"],informacion["passengers"],informacion["cargo_capacity"],informacion["consumables"],informacion["hyperdrive_rating"],informacion["MGLT"],pilotos_nave))

                for vehiculo in pelicula['properties']['vehicles']:
                    print('pelicula vehiculo')
                    informacion=rq.get(vehiculo).json()
                    informacion=informacion['result']['properties']
                    pilotos_vehiculo=[]

                    for piloto in informacion['pilots']:
                        print('piloto-vehiculo')
                        informacion_vehiculo=rq.get(piloto).json()
                        id=informacion_vehiculo['result']['uid']
                        informacion_vehiculo=informacion_vehiculo['result']['properties']
                        pilotos_vehiculo.append(Personaje(id,informacion_vehiculo["name"],informacion_vehiculo["gender"],informacion_vehiculo["height"],informacion_vehiculo["mass"],informacion_vehiculo["hair_color"],informacion_vehiculo["eye_color"],informacion_vehiculo["skin_color"],informacion_vehiculo["birth_year"], informacion_vehiculo["homeworld"]))
                    vehiculos_pelicula.append(Vehiculo(informacion["name"],informacion["model"],informacion["vehicle_class"],informacion["manufacturer"],informacion["cost_in_credits"],informacion["length"],informacion["crew"],informacion["passengers"],informacion["max_atmosphering_speed"],informacion["cargo_capacity"],informacion["consumables"],pilotos_vehiculo))

                for especie in pelicula['properties']['species']:
                    print('pelicula especie')
                    personajes_especie=[]

                    informacion=rq.get(especie).json()
                    id_especie=informacion["result"]["uid"]
                    informacion=informacion['result']['properties']
                    for personaje_esp in informacion['people']:
                        print('pelicula especie personaje')
                        informacion_especie=rq.get(personaje_esp).json()
                        id_personaje=informacion_especie["result"]["uid"]
                        informacion_especie=informacion_especie['result']['properties']
                        personajes_especie.append(Personaje(id_personaje,informacion_especie["name"],informacion_especie["gender"],informacion_especie["height"],informacion_especie["mass"],informacion_especie["hair_color"],informacion_especie["eye_color"],informacion_especie["skin_color"],informacion_especie["birth_year"],informacion_especie["homeworld"]))
                    especies_pelicula.append(Especie(id_especie,informacion["name"],informacion["classification"],informacion["designation"],informacion["average_height"],informacion["average_lifespan"],informacion["hair_colors"],informacion["skin_colors"],informacion["eye_colors"],informacion["language"],informacion["homeworld"],personajes_especie))

                self.peliculas_obj.append(Pelicula(pelicula["properties"]["title"],pelicula["properties"]["episode_id"],pelicula["properties"]["release_date"],pelicula["properties"]["opening_crawl"],pelicula["properties"]["director"],personajes_pelicula, planetas_pelicula, naves_pelicula, vehiculos_pelicula, especies_pelicula, pelicula["properties"]["producer"]))
                count+=1
            print(self.peliculas_obj)

### CREACION DE OBJETOS TIPO (Personaje) CON LOS DATOS DE LA API

    def crear_personajes(self):
        informacion=rq.get('https://www.swapi.tech/api/people/').json()
        informacion_original=informacion
        informacion=informacion['results']
        for personaje in informacion:
            id=personaje['uid']
            informacion_personaje=rq.get(personaje['url']).json()
            print('Personaje')
            self.personajes_obj.append(Personaje(id,informacion_personaje['result']['properties']["name"],informacion_personaje['result']['properties']["gender"],informacion_personaje['result']['properties']["height"],informacion_personaje['result']['properties']["mass"],informacion_personaje['result']['properties']["hair_color"],informacion_personaje['result']['properties']["eye_color"],informacion_personaje['result']['properties']["skin_color"],informacion_personaje['result']['properties']["birth_year"], informacion_personaje['result']['properties']["homeworld"]))

### CREACION DE OBJETOS TIPO (Especies) CON LOS DATOS DE LA API

    def crear_especies(self):
        informacion=rq.get('https://www.swapi.tech/api/species/').json()
        for especie in informacion['results']:
            id_especie=especie['uid']
            informacion_especie=rq.get(especie['url']).json()
            informacion_especie=informacion_especie['result']
            personajes_especie=[]
            print('especie')
            for personaje_esp in informacion_especie['properties']['people']:
                print('especie-personaje')
                informacion_personaje=rq.get(personaje_esp).json()
                id=informacion_personaje['result']['uid']
                informacion_personaje=informacion_personaje['result']['properties']
                personajes_especie.append(Personaje(id,informacion_personaje["name"],informacion_personaje["gender"],informacion_personaje["height"],informacion_personaje["mass"],informacion_personaje["hair_color"],informacion_personaje["eye_color"],informacion_personaje["skin_color"],informacion_personaje["birth_year"],informacion_personaje["homeworld"]))
            
            self.especies_obj.append(Especie(id_especie,informacion_especie['properties']["name"],informacion_especie['properties']["classification"],informacion_especie['properties']["designation"],informacion_especie['properties']["average_height"],informacion_especie['properties']["average_lifespan"],informacion_especie['properties']["hair_colors"],informacion_especie['properties']["skin_colors"],informacion_especie['properties']["eye_colors"],informacion_especie['properties']["language"],informacion_especie['properties']["homeworld"],personajes_especie))

### CREACION DE OBJETOS TIPO (Planeta) CON LOS DATOS DE LA API

    def crear_planetas(self):
        informacion=rq.get('https://www.swapi.tech/api/planets/').json()
        for planeta in informacion['results']:
            informacion_planeta=rq.get(planeta['url']).json()
            informacion_planeta=informacion_planeta['result']['properties']
            self.planetas_obj.append(Planeta(informacion_planeta["name"],informacion_planeta["diameter"],informacion_planeta["rotation_period"],informacion_planeta["orbital_period"],informacion_planeta["gravity"],informacion_planeta["population"],informacion_planeta["climate"],informacion_planeta["terrain"],informacion_planeta["surface_water"]))
            print("planeta")

### CREACION DE OBJETOS TIPO (Nave) CON LOS DATOS DE LA API

    def crear_naves(self):
        informacion=rq.get('https://www.swapi.tech/api/starships/').json()
        for nave in informacion['results']:
            informacion_nave=rq.get(nave["url"]).json()
            informacion_nave=informacion_nave['result']['properties']
            print("nave")

            pilotos_nave=[]
            for piloto in informacion_nave['pilots']:
                print('piloto-nave')
                informacion=rq.get(piloto).json()
                id=informacion['result']['uid']
                informacion=informacion['result']['properties']
                pilotos_nave.append(Personaje(id,informacion["name"],informacion["gender"],informacion["height"],informacion["mass"],informacion["hair_color"],informacion["eye_color"],informacion["skin_color"],informacion["birth_year"],informacion["homeworld"]))
            self.naves_obj.append(Nave(informacion_nave["name"],informacion_nave["model"],informacion_nave["manufacturer"],informacion_nave["cost_in_credits"],informacion_nave["length"],informacion_nave["max_atmosphering_speed"],informacion_nave["crew"],informacion_nave["passengers"],informacion_nave["cargo_capacity"],informacion_nave["consumables"],informacion_nave["hyperdrive_rating"],informacion_nave["MGLT"],pilotos_nave))

### CREACION DE OBJETOS TIPO (Vehiculo) CON LOS DATOS DE LA API


    def crear_vehiculos(self):
        informacion=rq.get('https://www.swapi.tech/api/vehicles/').json()
        for vehiculo in informacion['results']:
            informacion_vehiculo=rq.get(vehiculo["url"]).json()
            informacion_vehiculo=informacion_vehiculo['result']['properties']
            print("vehiculo")

            pilotos_vehiculo=[]
            for piloto in informacion_vehiculo['pilots']:
                print('piloto-nave')
                informacion=rq.get(piloto).json()
                id=informacion['result']['uid']
                informacion=informacion['result']['properties']
                pilotos_vehiculo.append(Personaje(id,informacion["name"],informacion["gender"],informacion["height"],informacion["mass"],informacion["hair_color"],informacion["eye_color"],informacion["skin_color"],informacion["birth_year"],informacion["homeworld"]))
        
            self.vehiculos_obj.append(Vehiculo(informacion_vehiculo["name"],informacion_vehiculo["model"],informacion_vehiculo["vehicle_class"],informacion_vehiculo["manufacturer"],informacion_vehiculo["cost_in_credits"],informacion_vehiculo["length"],informacion_vehiculo["crew"],informacion_vehiculo["passengers"],informacion_vehiculo["max_atmosphering_speed"],informacion_vehiculo["cargo_capacity"],informacion_vehiculo["consumables"],pilotos_vehiculo))
