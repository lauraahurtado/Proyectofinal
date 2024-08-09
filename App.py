# IMPORTACION DE EXTENSIONES Y CLASES

import requests as rq
import json
from Pelicula import Pelicula
from Especie import Especie
from Nave import Nave
from Personaje import Personaje
from Planeta import Planeta
from Vehiculo import Vehiculo
from Mision import Mision

import csv
from Personaje_csv import Personaje_cvs
from Nave_csv import Nave_cvs
from Arma_csv import Arma_csv
from Planeta_csv import Planeta_csv

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

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

    personajes_csv_obj=[]
    naves_csv_obj=[]
    armas_csv_obj=[]
    planetas_csv_obj=[]

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
            None
        except:
            print('''Está fallando la carga de la API, por conexión a internet u otro motivo.
                    Vuelva a correr el programa.''')
        self.crear_personajes_csv()
        self.crear_naves_csv()
        self.crear_planetas_csv()
        self.crear_armas_csv()



# MENÚ DEL PROGRAMA
        print('\n------------ BIENVENIDO A STARWARS METROPEDIA ------------')
        while True:
            menu=input('''\nIngrese el índice numérico correspondiente a la opcion del menu que desea realizar:
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
---> ''')
            
            if menu=="1":
                for pelicula in self.peliculas_obj:
                    pelicula.mostrar_peliculas()


            elif menu=='2':
                None

            elif menu=='3':
                for planeta in self.planetas_obj:
                    planeta.mostrar_planetas(self.peliculas_obj,self.personajes_obj)

            elif menu=='4':
                nombre_buscado=input('\nIngrese el nombre del personaje que desea buscar: ')
                self.buscar_personajes(nombre_buscado)

            elif menu=='5':
                self.cant_personajes_por_planeta()

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

    
    
# CREACION DE OBJETOS TIPO (Pelicula) CON LOS DATOS DE LA API

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

# CREACION DE OBJETOS TIPO (Personaje) CON LOS DATOS DE LA API

    def crear_personajes(self):
        informacion=rq.get('https://www.swapi.tech/api/people/').json()
        informacion_original=informacion
        informacion=informacion['results']
        for personaje in informacion:
            id=personaje['uid']
            informacion_personaje=rq.get(personaje['url']).json()
            print('Personaje')
            self.personajes_obj.append(Personaje(id,informacion_personaje['result']['properties']["name"],informacion_personaje['result']['properties']["gender"],informacion_personaje['result']['properties']["height"],informacion_personaje['result']['properties']["mass"],informacion_personaje['result']['properties']["hair_color"],informacion_personaje['result']['properties']["eye_color"],informacion_personaje['result']['properties']["skin_color"],informacion_personaje['result']['properties']["birth_year"], informacion_personaje['result']['properties']["homeworld"]))

# CREACION DE OBJETOS TIPO (Especies) CON LOS DATOS DE LA API

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

# CREACION DE OBJETOS TIPO (Planeta) CON LOS DATOS DE LA API

    def crear_planetas(self):
        informacion=rq.get('https://www.swapi.tech/api/planets/').json()
        for planeta in informacion['results']:
            informacion_planeta=rq.get(planeta['url']).json()
            informacion_planeta=informacion_planeta['result']['properties']
            self.planetas_obj.append(Planeta(informacion_planeta["name"],informacion_planeta["diameter"],informacion_planeta["rotation_period"],informacion_planeta["orbital_period"],informacion_planeta["gravity"],informacion_planeta["population"],informacion_planeta["climate"],informacion_planeta["terrain"],informacion_planeta["surface_water"]))
            print("planeta")

# CREACION DE OBJETOS TIPO (Nave) CON LOS DATOS DE LA API

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

# CREACION DE OBJETOS TIPO (Vehiculo) CON LOS DATOS DE LA API


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

# CREACION DE LA FUNCION BUSCAR PERSONAJES EN LA SAGA (PARTE 4 DEL MENU)

    def buscar_personajes(self, nombre_buscado):
        encontrado=0
        for personaje in self.personajes_obj:
            if nombre_buscado.lower() in personaje.nombre.lower():
                personaje.mostrar_personajes_opcion_cuatro(self.peliculas_obj,self.especies_obj,self.naves_obj,self.vehiculos_obj)
                encontrado=1
        if encontrado==0:
            print('No se encontró este personaje en la saga.')

# CREACION DE OBJETOS TIPO (Personaje) CON LOS DATOS DEL CSV

    def crear_personajes_csv(self):
        with open('starwars/csv/characters.csv',newline='') as archivo_csv:
            lector_csv=csv.reader(archivo_csv,delimiter=',')
            contador=0
            for fila in lector_csv:
                if contador>0:
                    self.personajes_csv_obj.append(Personaje_cvs(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11],fila[12]))
                contador+=1

# CREACION DE OBJETOS TIPO (Nave) CON LOS DATOS DEL CSV.

    def crear_naves_csv(self):
        with open ('starwars/csv/starships.csv',newline='') as archivo_csv:
            lector_csv=csv.reader(archivo_csv,delimiter=',')
            contador=0
            for fila in lector_csv:
                if contador>0:
                    self.naves_csv_obj.append(Nave_cvs(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11],fila[12],fila[13],fila[14],fila[15]))
                contador+=1
    
# CREACION DE OBJETOS (Armas) CON LOS DATOS DEL CSV.

    def crear_armas_csv(self):
        with open('starwars/csv/weapons.csv',newline='') as archivo_csv:
            lector_csv=csv.reader(archivo_csv,delimiter=',')
            contador=0
            for fila in lector_csv:
                if contador>0:
                    self.armas_csv_obj.append(Arma_csv(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8]))
                contador+=1
    
# CREACION DE OBJETOS (Planetas) CON LOS DATOS DE CSV.

    def crear_planetas_csv(self):
        with open ('starwars/csv/planets.csv') as archivo_csv:
            lector_csv=csv.reader(archivo_csv,delimiter=',')
            contador=0
            for fila in lector_csv:
                if contador>0:
                    self.planetas_csv_obj.append(Planeta_csv(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11]))
                contador+=1

# CREACION DE LA FUNCION CUYO OBJETIVO ES GRAFICAR LA CANTIDAD DE PERSONAJES QUE HAY POR PLANETA.

    def cant_personajes_por_planeta(self):
        lista_planetas_csv_personajes=[]
        lista_cantidad_planetas_csv_personajes=[]
        for personaje in self.personajes_csv_obj:
            if personaje.mundo_natal not in lista_planetas_csv_personajes:
                lista_planetas_csv_personajes.append(personaje.mundo_natal)
        diccionario_planetas_csv_personajes={}

        for personaje in lista_planetas_csv_personajes:
            diccionario_planetas_csv_personajes[personaje]=0

        for personaje in self.personajes_csv_obj:
            diccionario_planetas_csv_personajes[personaje.mundo_natal]+=1

        for personaje, cantidad in diccionario_planetas_csv_personajes.items():
            lista_cantidad_planetas_csv_personajes.append(cantidad)

        self.grafico_cant_personajes_por_planeta(lista_planetas_csv_personajes,lista_cantidad_planetas_csv_personajes)

        
# CREACION DE LA FUNCION PARA GRAFICAR LA CANTIDAD DE PERSONAJES EXISTENTES POR PLANETA
     
    def grafico_cant_personajes_por_planeta(self,lista_planetas_csv_personajes,lista_cantidad_planetas_csv_personajes):
        fig, ax=plt.subplots()
        ax.bar(lista_planetas_csv_personajes,lista_cantidad_planetas_csv_personajes)
        plt.title('Cantidad de personajes por planeta')
        plt.xlabel('Planeta')
        plt.ylabel('Cantidad de personajes')
        plt.xticks(rotation=90) #Rotacion de la disposicion visula de cada planeta en el eje x para mejor estetica
        plt.show()

# CREACION DE FUNCION PARA GRAFICAR CIERTAS CARACTERISTICAS DE CADA NAVE

    def graficos_caracteristicas_naves(self):
        while True:
            opcion=input('''Escoja el indice numerico cuya opcion corresponda al gráfico que desea observar:
    1. Longitud de las naves. 
    2. Capacidad de carga.
    3. Clasificacion de hiperimpulsor.
    4. MGLT (Modern Galactic Light Time).
    5. Retroceder.
    --> ''')
            
            lista_naves_csv=[]
            for nave in self.naves_csv_obj:
                lista_naves_csv.append(nave.nombre)
            
            if opcion=='1':
                longitud_naves_csv=[]
                for nave in self.naves_csv_obj:
                    longitud_naves_csv.append(nave.longitud)
                fig, ax=plt.subplots()
                ax.bar(lista_naves_csv,longitud_naves_csv)
                plt.title('Naves vs. Longitud Naves')
                plt.xlabel('Naves')
                plt.ylabel('Longitud de Naves')
                plt.xticks(rotation=90)
                plt.show()

            if opcion=='2':
                capacidad_de_carga_naves_csv=[]
                for nave in self.naves_csv_obj:
                    capacidad_de_carga_naves_csv.append(nave.capacidad_de_carga)
                fig, ax=plt.subplots()
                ax.bar(lista_naves_csv,capacidad_de_carga_naves_csv)
                plt.title('Naves vs Capacidad de carga')
                plt.xlabel('Naves')
                plt.ylabel('Capacidad de carga de naves')
                plt.xticks(rotation=90)
                plt.show()