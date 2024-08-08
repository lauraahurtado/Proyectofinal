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
            self.crear_peliculas
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
                None


            elif menu=='2':
                None

            elif menu=='3':
                None

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
                    personajes_pelicula.append(Personaje(id,informacion["name",informacion["gender"]],informacion["height"],informacion["mass"],informacion["hair_color"],informacion["eye_color"],informacion["skin_color"],informacion["birth_year"],informacion["homeworld"]))

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