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
                lista_indices=[]
                lista_ordenada=[]
                for y in range(0,len(self.especies_obj)):
                    count=0
                    minimo=1000
                    objeto=-1
                    for x in self.especies_obj:
                        if int(x.id) <minimo and int(x.id) not in lista_indices:
                            minimo=int(x.id)
                            objeto=x
                        count+=1
                    if objeto!=-1:
                        lista_indices.append(minimo)
                        lista_ordenada.append(objeto)
                    else:
                        break
                for especie in lista_ordenada:
                    especie.mostrar_especies(self.peliculas_obj)

            elif menu=='3':
                for planeta in self.planetas_obj:
                    planeta.mostrar_planetas(self.peliculas_obj,self.personajes_obj)

            elif menu=='4':
                nombre_buscado=input('\nIngrese el nombre del personaje que desea buscar: ')
                self.buscar_personajes(nombre_buscado)

            elif menu=='5':
                self.cant_personajes_por_planeta()

            elif menu=='6':
                self.graficos_caracteristicas_naves()

            elif menu=='7':
                self.estadisticas_sobre_naves()

            elif menu=='8':
                self.crear_misiones()

            elif menu=='9':
                self.modificar_misiones()

            elif menu=='10':
                None

            elif menu=='11':
                self.guardar_misiones()
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
            opcion=input('''\nEscoja el indice numerico cuya opcion corresponda al gráfico que desea observar:
    1. Longitud de las naves. 
    2. Capacidad de carga.
    3. Clasificacion de hiperimpulsor.
    4. MGLT (Modern Galactic Light Time).
    5. Volver al menu inicial.
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

            elif opcion=='2':
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

            elif opcion=='3':
                clasificacion_de_hiperimpulsor_navez_csv=[]
                for nave in self.naves_csv_obj:
                    clasificacion_de_hiperimpulsor_navez_csv.append(nave.clasificacion_de_hiperimpulsor)
                fig, ax=plt.subplots()
                ax.bar(lista_naves_csv,clasificacion_de_hiperimpulsor_navez_csv)
                plt.title('Naves vs. Clasificacion del hiperimpulsor')
                plt.xlabel('Naves')
                plt.ylabel('Clasificacion del hiperimpulsor')
                plt.xticks(rotation=90)
                plt.show()
            
            elif opcion=='4':
                mglt_naves_csv=[]
                for nave in self.naves_csv_obj:
                    mglt_naves_csv.append(nave.mglt)
                fig,ax=plt.subplots()
                ax.bar(lista_naves_csv,mglt_naves_csv)
                plt.title('Naves vs. MGLT (Modern Galactic Light Time)')
                plt.xlabel('Naves')
                plt.ylabel('MGLT (Modern Galactic Light Time)')
                plt.xticks(rotation=90)
                plt.show()

            elif opcion=='5':
                break

            else:
                print('\nPor favor, ingrese una opcion contemplada en el menu.')

# CREACION DE LA FUNCION PARA CALCULAR LAS ESTADISCITCAS (MODA, PROMEDIO, MAXIMO Y MINIMO) DE CADA CLASE DE NAVE

    def estadisticas_sobre_naves(self):
        lista_clase_naves_csv=[]
        diccionario_estadisticas_naves={}

        for nave in self.naves_csv_obj:
            if nave.clase_de_nave not in lista_clase_naves_csv:
                lista_clase_naves_csv.append(nave.clase_de_nave)
                diccionario_estadisticas_naves[nave.clase_de_nave]={}

                diccionario_estadisticas_naves[nave.clase_de_nave]['clasificacion_de_hiperimpulsor']=[]
                if nave.clasificacion_de_hiperimpulsor!='':
                    diccionario_estadisticas_naves[nave.clase_de_nave]['clasificacion_de_hiperimpulsor'].append(float(nave.clasificacion_de_hiperimpulsor))
                else:
                    diccionario_estadisticas_naves[nave.clase_de_nave]['clasificacion_de_hiperimpulsor'].append(0)
                
                diccionario_estadisticas_naves[nave.clase_de_nave]['mglt']=[]
                if nave.mglt!='':
                    diccionario_estadisticas_naves[nave.clase_de_nave]['mglt'].append(float(nave.mglt))
                else:
                    diccionario_estadisticas_naves[nave.clase_de_nave]['mglt'].append(0)
                
                diccionario_estadisticas_naves[nave.clase_de_nave]['velocidad_maxima']=[]
                if nave.velocidad_maxima!='':
                    diccionario_estadisticas_naves[nave.clase_de_nave]['velocidad_maxima'].append(float(nave.velocidad_maxima))
                else:
                    diccionario_estadisticas_naves[nave.clase_de_nave]['velocidad_maxima'].append(0)

                diccionario_estadisticas_naves[nave.clase_de_nave]['costo_en_creditos']=[]
                if nave.costo_en_creditos!='':
                    diccionario_estadisticas_naves[nave.clase_de_nave]['costo_en_creditos'].append(float(nave.costo_en_creditos))
                else:
                    diccionario_estadisticas_naves[nave.clase_de_nave]['costo_en_creditos'].append(0)

            else:
                if nave.clasificacion_de_hiperimpulsor!='':
                    diccionario_estadisticas_naves[nave.clase_de_nave]['clasificacion_de_hiperimpulsor'].append(float(nave.clasificacion_de_hiperimpulsor))
                else:
                    diccionario_estadisticas_naves[nave.clase_de_nave]['clasificacion_de_hiperimpulsor'].append(0)
                
                if nave.mglt!='':
                    diccionario_estadisticas_naves[nave.clase_de_nave]['mglt'].append(float(nave.mglt))
                else:
                    diccionario_estadisticas_naves[nave.clase_de_nave]['mglt'].append(0)
                
                if nave.velocidad_maxima!='':
                    diccionario_estadisticas_naves[nave.clase_de_nave]['velocidad_maxima'].append(float(nave.velocidad_maxima))
                else:
                    diccionario_estadisticas_naves[nave.clase_de_nave]['velocidad_maxima'].append(0)

                if nave.costo_en_creditos!='':
                    diccionario_estadisticas_naves[nave.clase_de_nave]['costo_en_creditos'].append(float(nave.costo_en_creditos))
                else:
                    diccionario_estadisticas_naves[nave.clase_de_nave]['costo_en_creditos'].append(0)
        
        self.grafico_estadisticas_naves(diccionario_estadisticas_naves,lista_clase_naves_csv)

# CREACION DE TABLA DE CIERTAS CARACTERISTICAS DE  LAS CLASES DE NAVES UTILIZANDO (MEDIA, PROMEDIO, MAXIMO Y MINIMO). (UTILIZANDO HERRAMIENTAS DE NUMPY)
    
    def grafico_estadisticas_naves(self,diccionario_estadisticas_naves,lista_clase_naves_csv):
        datos=[]
        for clase, dato in diccionario_estadisticas_naves.items():
            lista_clases=[]

            #------ HIPERIMPULSOR ------

            medidas_clasificacion_de_hiperimpulsor='CHD- Moda:'
            moda_hiperimpulsor=np.array(dato['clasificacion_de_hiperimpulsor'])
            moda_hiperimpulsor=np.round(moda_hiperimpulsor,decimals=2)
            valores_unicos, conteos=np.unique(moda_hiperimpulsor,return_counts=True)
            moda_hiperimpulsor=valores_unicos[np.argmax(conteos)]
            medidas_clasificacion_de_hiperimpulsor+=str(moda_hiperimpulsor)+' Promedio: '

            promedio_hiperimpulsor=np.array(dato['clasificacion_de_hiperimpulsor'])
            promedio_hiperimpulsor=np.mean(promedio_hiperimpulsor)
            promedio_hiperimpulsor=np.round(promedio_hiperimpulsor,decimals=2)
            medidas_clasificacion_de_hiperimpulsor+=str(promedio_hiperimpulsor)+' Max: '

            maximo_hiperimpulsor=np.array(dato['clasificacion_de_hiperimpulsor'])
            maximo_hiperimpulsor=np.max(maximo_hiperimpulsor)
            maximo_hiperimpulsor=np.round(maximo_hiperimpulsor,decimals=2)
            medidas_clasificacion_de_hiperimpulsor+=str(maximo_hiperimpulsor)+' Min: '

            minimo_hiperimpulsor=np.array(dato['clasificacion_de_hiperimpulsor'])
            minimo_hiperimpulsor=np.min(minimo_hiperimpulsor)
            minimo_hiperimpulsor=np.round(minimo_hiperimpulsor, decimals=2)
            medidas_clasificacion_de_hiperimpulsor+=str(minimo_hiperimpulsor)
            lista_clases.append(medidas_clasificacion_de_hiperimpulsor)

            #------ MGLT ------

            medidas_mglt='MGLT- Moda:'
            moda_mglt=np.array(dato['mglt'])
            moda_mglt=np.round(moda_mglt,decimals=2)
            valores_unicos, conteos=np.unique(moda_mglt,return_counts=True)
            moda_mglt=valores_unicos[np.argmax(conteos)]
            moda_mglt=np.round(moda_mglt,decimals=2)
            medidas_mglt+=str(moda_mglt)+ ' Prom: '
            
            promedio_mglt=np.array(dato['mglt'])
            promedio_mglt=np.mean(promedio_mglt)
            promedio_mglt=np.round(promedio_mglt,decimals=2)
            medidas_mglt+=str(promedio_mglt)+' Max: '

            maximo_mglt=np.array(dato['mglt'])
            maximo_mglt=np.max(maximo_mglt)
            maximo_mglt=np.round(maximo_mglt, decimals=2)
            medidas_mglt+=str(maximo_mglt)+' Min: '
            
            minimo_mglt=np.array(dato['mglt'])
            minimo_mglt=np.min(minimo_mglt)
            minimo_mglt=np.round(minimo_mglt,decimals=2)
            medidas_mglt+=str(minimo_mglt)
            lista_clases.append(medidas_mglt)

            #------ VELOCIDAD MAXIMA ------

            medidas_velocidad_maxima='Vmax- Moda:'
            moda_velocidad_maxima=np.array(dato['velocidad_maxima'])
            moda_velocidad_maxima=np.round(moda_velocidad_maxima, decimals=2)
            valores_unicos, conteos=np.unique(moda_velocidad_maxima,return_counts=True)
            moda_velocidad_maxima=valores_unicos[np.argmax(conteos)]
            medidas_velocidad_maxima+=str(moda_velocidad_maxima)+' Prom: '

            promedio_velocidad_maxima=np.array(dato['velocidad_maxima'])
            promedio_velocidad_maxima=np.mean(promedio_velocidad_maxima)
            promedio_velocidad_maxima=np.round(promedio_velocidad_maxima,decimals=2)
            medidas_velocidad_maxima+=str(promedio_velocidad_maxima)

            maximo_velocidad_maxima=np.array(dato['velocidad_maxima'])
            maximo_velocidad_maxima=np.max(maximo_velocidad_maxima)
            maximo_velocidad_maxima=np.round(maximo_velocidad_maxima,decimals=2)
            medidas_velocidad_maxima+=str(maximo_velocidad_maxima)+' Min: '

            minimo_velocidad_maxima=np.array(dato['velocidad_maxima'])
            minimo_velocidad_maxima=np.min(minimo_velocidad_maxima)
            minimo_velocidad_maxima=np.round(minimo_velocidad_maxima,decimals=2)
            medidas_velocidad_maxima+=str(minimo_velocidad_maxima)
            lista_clases.append(medidas_velocidad_maxima)

            #------ COSTO EN CREDITOS ------

            medidas_costo_en_creditos='CEC- Moda:'
            moda_costo_en_creditos=np.array(dato['costo_en_creditos'])
            moda_costo_en_creditos=np.round(moda_costo_en_creditos,decimals=2)
            valores_unicos, conteos=np.unique(moda_costo_en_creditos,return_counts=True)
            moda_costo_en_creditos=valores_unicos[np.argmax(conteos)]
            medidas_costo_en_creditos+=str(moda_costo_en_creditos)+' Prom: '

            promedio_costo_en_creditos=np.array(dato['costo_en_creditos'])
            promedio_costo_en_creditos=np.mean([promedio_costo_en_creditos])
            promedio_costo_en_creditos=np.round(promedio_costo_en_creditos,decimals=2)
            medidas_costo_en_creditos+=str(promedio_costo_en_creditos)+' Max: '

            maximo_costo_en_creditos=np.array(dato['costo_en_creditos'])
            maximo_costo_en_creditos=np.max(maximo_costo_en_creditos)
            maximo_costo_en_creditos=np.round(maximo_costo_en_creditos,decimals=2)
            medidas_costo_en_creditos+=str(maximo_costo_en_creditos)+' Min: '

            minimo_costo_en_creditos=np.array(dato['costo_en_creditos'])
            minimo_costo_en_creditos=np.max(minimo_costo_en_creditos)
            minimo_costo_en_creditos=np.round(minimo_costo_en_creditos,decimals=2)
            medidas_costo_en_creditos+=str(minimo_costo_en_creditos)
            lista_clases.append(medidas_costo_en_creditos)
            
            
            datos.append(lista_clases)

        contador=0
        lista_clase_naves_estadisticas=[]
        for clase in lista_clase_naves_csv:
            diccionario_para_cada_clase_nave={}
            diccionario_para_cada_clase_nave[clase]=datos[contador]
            lista_clase_naves_estadisticas.append(diccionario_para_cada_clase_nave)
            contador+=1
            diccionario_para_cada_clase_nave=pd.DataFrame(diccionario_para_cada_clase_nave)
            print(diccionario_para_cada_clase_nave)


### CREACION DE OBJETOS TIPO (MISION) CON LOS DATOS DE LOS CSV

    def crear_misiones(self):
        if self.cantidad_misiones<5:
            nombre_mision=input('\n>> Nombre de la Mision: ')

            count=1
            for planeta in self.planetas_csv_obj:
                print(f'{count}-{planeta.nombre}')
                count+=1
            planeta_destino_mision=input('>> Ingrese el indice numérico correspondiente al Planeta de Destino de la Mision que desea seleccionar: ')
            while planeta_destino_mision.isnumeric()==False or int(planeta_destino_mision)>len(self.planetas_csv_obj):
                planeta_destino_mision=input('>> Ingrese el índice numérico correspondiente del planeta de Destino de la Mision: ')
            planeta_destino_mision=self.planetas_csv_obj[int(planeta_destino_mision)-1]

            count=1
            for nave in self.naves_csv_obj:
                print(f'{count}-{nave.nombre}')
                count+=1
            nave_mision=input('>> Ingrese el indice numérico correpondiente a la Nave a utilizar en la mision: ')
            while nave_mision.isnumeric()==False or int(nave_mision)>len(self.naves_csv_obj):
                nave_mision=input('>> Ingrese el indice numérico correspondiente a la Nave a utilizar en la mision: ')
            nave_mision=self.naves_csv_obj[int(nave_mision)-1]

            lista_indice_armas=[]
            lista_armas=[]
            while len(lista_indice_armas)<7:
                count=1
                for arma in self.armas_csv_obj:
                    print(f'{count}-{arma.nombre}')
                    count+=1
                arma_a_utilizar_mision=input(f'>> Ingrese el indice numérico correspondiente al Arma {len(lista_indice_armas)+1} a utilizar en la mision: ')
                while arma_a_utilizar_mision.isnumeric()==False or int(arma_a_utilizar_mision)>len(self.armas_csv_obj):
                    arma_a_utilizar_mision=input(f'>> Ingrese el indice numérico correspondiente al Arma {len(lista_indice_armas)+1} a utilizar en la mision: ')
                if int(arma_a_utilizar_mision)-1 not in lista_indice_armas:
                    lista_indice_armas.append(int(arma_a_utilizar_mision)-1)
                    arma_a_utilizar_mision=self.armas_csv_obj[int(arma_a_utilizar_mision)-1]
                    lista_armas.append(arma_a_utilizar_mision)
                else:
                    print('Ya fue escogida esta arma')

                if len(lista_indice_armas)>0:
                    opcion=input('''\nPulse:
1. Para seguir eligiendo
2. Para finalizar la eleccion de armas
--> ''')
                    while opcion!='1' and opcion!='2':
                        opcion=input('\nIngrese una opcion válida contemplada en el menú: ')

                    if opcion=='1':
                        continue

                    elif opcion=='2': 
                        break

                

            lista_indice_integrantes_mision=[]
            lista_integrantes_mision=[]
            while len(lista_indice_integrantes_mision)<7:
                count=1
                for integrante in self.personajes_csv_obj:
                    print(f'{count}-{integrante.nombre}')
                    count+=1
                integrante_de_la_mision=input(f'\n>> Ingrese el indice numérico correspondiente al Integrante {len(lista_indice_integrantes_mision)+1} a elegir para que participe en la mision: ')
                while integrante_de_la_mision.isnumeric()==False or int(integrante_de_la_mision)>len(self.personajes_csv_obj):
                    integrante_de_la_mision=input(f'>> Ingrese el indice numérico correspondiente al Integrante {len(lista_indice_integrantes_mision)+1} a elegir para que participe en la mision: ')
                if int(integrante_de_la_mision)-1 not in lista_indice_integrantes_mision:
                    lista_indice_integrantes_mision.append(int(integrante_de_la_mision)-1)
                    integrante_de_la_mision=self.personajes_csv_obj[int(integrante_de_la_mision)-1]
                    lista_integrantes_mision.append(integrante_de_la_mision)
                else:
                    print('Ya fue elegido este integrante para participar en la mision')

                if len(lista_indice_integrantes_mision)>0:
                    opcion=input('''\nPulse:
1. Para seguir eligiendo
2. Para finalizar la eleccion de integrantes para la mision
--> ''')
                    while opcion!='1' and opcion!='2':
                        opcion=input('\nIngrese una opcion válida contemplada en el menú')

                    if opcion=='1':
                        continue

                    elif opcion=='2': 
                        break

            self.misiones_obj.append(Mision(self.cantidad_misiones+1,nombre_mision,planeta_destino_mision,nave_mision,lista_armas,lista_integrantes_mision))
            self.cantidad_misiones+=1

            print(f'\nSu mision ha sido creada exitosamente!')

        else:
            print('Ya han sido creadas el máximo de misiones (7)')

#------------------------------

# CREACION DE LA FUNCION PARA MODIFICAR LOS ATRIBUTOS DE CADA MISION CREADA POR EL USUARIO

    def modificar_misiones(self):
        for mision in self.misiones_obj:
            print(f'>> ID de la Mision: {mision.numero_de_mision} - Nombre de la Mision: {mision.nombre}')
        mision_a_modificar=input('\nIngrese el ID de la mision que desea modificar: ')
        while mision_a_modificar.isnumeric()==False or int(mision_a_modificar)>len(self.misiones_obj):
            mision_a_modificar=input('\nIngrese el ID de la mision que desea modificar: ')
        atributo_a_modificar_de_la_mision=input('''
1. Nombre de la mision.
2. Planeta destino.
3. Nave a utilizar.
4. Armas a utilizar.
5. Integrantes de la mision.
--> ''')
        
        while atributo_a_modificar_de_la_mision!='1' and atributo_a_modificar_de_la_mision!='2' and atributo_a_modificar_de_la_mision!='3' and atributo_a_modificar_de_la_mision!='4' and atributo_a_modificar_de_la_mision!='5':
            atributo_a_modificar_de_la_mision=input('\nIngrese una opcion valida contemplada en el menu: ')
        
        if atributo_a_modificar_de_la_mision=='1':
            nuevo_nombre_mision=input('\nNuevo nombre de la Mision:')
            self.misiones_obj[int(mision_a_modificar)-1].nombre=nuevo_nombre_mision
        
        elif atributo_a_modificar_de_la_mision=='2':
            print()
            contador=1
            for planeta in self.planetas_csv_obj:
                print(f'{contador}. {planeta.nombre}')
                contador+=1
            nuevo_planeta_destino=input('\nIngrese el numero del nuevo planeta destino de la mision: ')
            while nuevo_planeta_destino.isnumeric()==False or int(nuevo_planeta_destino)>len(self.planetas_csv_obj):
                nuevo_planeta_destino=input('Ingrese el numero del nuevo planeta destino: ')
            self.misiones_obj[int(mision_a_modificar)-1].planeta=self.planetas_csv_obj[int(nuevo_planeta_destino)-1]

        elif atributo_a_modificar_de_la_mision=='3':
            print()
            contador=1
            for nave in self.naves_csv_obj:
                print(f'{contador}. {nave.nombre}')
                contador+=1
            nueva_nave_mision=input('\nIngrese el numero correspondiente a la nueva nave a utilizar en la mision: ')
            while nueva_nave_mision.isnumeric()==False or int(nueva_nave_mision)>len(self.naves_csv_obj):
                nueva_nave_mision=input('Ingrese el numero correspondiente a la nueva nade a utilizar en la mision: ')
            self.misiones_obj[int(mision_a_modificar)-1].nave=self.naves_csv_obj[int(nueva_nave_mision)-1]

        elif atributo_a_modificar_de_la_mision=='4':
            opcion=input('''\nIngrese:
1. Para cambiar un arma previamente seleccionada por otra.
2. Para agregar una nueva arma.
3. Para eliminar un arma. 
4. Retroceder al menu principal. 
--> ''')
            while opcion!='1' and opcion!='2' and opcion!='3' and opcion!='4':
                opcion=input('Ingrese una opcion valida contemplada en el menu: ')
            
            if opcion=='1':
                print()
                contador=1
                for arma in self.misiones_obj[int(mision_a_modificar)-1].armas_utilizadas:
                    print(f'{contador}. {arma.nombre}')
                    contador+=1
                arma_a_modificar=input('\nIngrese el numero del arma a modificar: ')
                while arma_a_modificar.isnumeric()==False or int(arma_a_modificar)>len(self.armas_csv_obj):
                    arma_a_modificar=input('Ingrese el numero del arma a modificar: ')
                
                print()
                contador=1
                for arma in self.armas_csv_obj:
                    print(f'{contador}. {arma.nombre}')
                    contador+=1
                nueva_arma_a_seleccionar=input('Ingrese el numero de la nueva arma que reemplazara a la anterior: ') 
                while nueva_arma_a_seleccionar.isnumeric()==False or int(nueva_arma_a_seleccionar)>len(self.armas_csv_obj):
                    nueva_arma_a_seleccionar=input('Ingrese el numero de la nueva arma que reemplazara a la anterior: ')
                self.misiones_obj[int(mision_a_modificar)-1].armas_utilizadas[int(arma_a_modificar)-1]=self.armas_csv_obj[int(nueva_arma_a_seleccionar)-1]

            elif opcion=='2':
                if len(self.misiones_obj[int(mision_a_modificar)-1].armas_utilizadas)<7:
                    print()
                    contador=1
                    for arma in self.armas_csv_obj:
                        print(f'{contador}. {arma.nombre}')
                        contador+=1
                    nueva_arma_a_agregar=input('Ingrese el numero de la arma que desea agregar: ') 
                    while nueva_arma_a_agregar.isnumeric()==False or int(nueva_arma_a_agregar)>len(self.armas_csv_obj):
                        nueva_arma_a_seleccionar=input('Ingrese el numero de la arma que desea agregar: ')
                    self.misiones_obj[int(mision_a_modificar)-1].armas_utilizadas.append(self.armas_csv_obj[int(nueva_arma_a_agregar)-1])

            elif opcion=='3':
                if len(self.misiones_obj[int(mision_a_modificar)-1].armas_utilizadas)>0:
                    print()
                    contador=1
                    for arma in self.misiones_obj[int(mision_a_modificar)-1].armas_utilizadas:
                        print(f'{contador}. {arma.nombre}')
                        contador+=1
                    arma_a_eliminar=input('Ingrese el numero del arma que desea eliminar: ')
                    while arma_a_eliminar.isnumeric()==False or int(arma_a_eliminar)>len(self.misiones_obj[int(mision_a_modificar)-1].armas_utilizadas):
                        arma_a_eliminar=input('Ingrese el numero del arma que desea eliminar: ')
                    self.misiones_obj[int(mision_a_modificar)-1].armas_utilizadas.pop(int(arma_a_eliminar)-1)

                else:
                    print('No hay armas escogidas, por lo que no se puede eliminar ninguna.')

            elif opcion=='4':
                None

            else:      
                print('Ingrese una de las opciones indicadas.')   
            


    def guardar_misiones(self):
        misiones=[]
        for mision in self.misiones_obj:
            mision_diccionario={}
            mision_diccionario["numero_de_mision"]=mision.numero_de_mision

            mision_diccionario["nombre"]=mision.nombre

            mision_planeta_diccionario={}
            mision_planeta_diccionario["id"]=mision.planeta.id
            mision_planeta_diccionario["nombre"]=mision.planeta.nombre
            mision_planeta_diccionario["diametro"]=mision.planeta.diametro
            mision_planeta_diccionario["periodo_de_rotacion"]=mision.planeta.periodo_de_rotacion
            mision_planeta_diccionario["periodo_de_orbita"]=mision.planeta.periodo_de_orbita
            mision_planeta_diccionario["gravedad"]=mision.planeta.gravedad
            mision_planeta_diccionario["poblacion"]=mision.planeta.poblacion
            mision_planeta_diccionario["clima"]=mision.planeta.clima
            mision_planeta_diccionario["terreno"]=mision.planeta.terreno
            mision_planeta_diccionario["superficie_acuatica"]=mision.planeta.superficie_acuatica
            mision_planeta_diccionario["residentes"]=mision.planeta.residentes
            mision_planeta_diccionario["peliculas"]=mision.planeta.peliculas
            mision_diccionario["planeta"]=mision_planeta_diccionario

            mision_nave_diccionario={}
            mision_nave_diccionario["id"]=mision.nave.id
            mision_nave_diccionario["nombre"]=mision.nave.nombre
            mision_nave_diccionario["modelo"]=mision.nave.modelo
            mision_nave_diccionario["fabricante"]=mision.nave.fabricante
            mision_nave_diccionario["costo_en_creditos"]=mision.nave.costo_en_creditos
            mision_nave_diccionario["longitud"]=mision.nave.longitud
            mision_nave_diccionario["velocidad_maxima"]=mision.nave.velocidad_maxima
            mision_nave_diccionario["tripulacion"]=mision.nave.tripulacion
            mision_nave_diccionario["pasajeros"]=mision.nave.pasajeros
            mision_nave_diccionario["capacidad_de_carga"]=mision.nave.capacidad_de_carga
            mision_nave_diccionario["consumibles"]=mision.nave.consumibles
            mision_nave_diccionario["clasificacion_de_hiperimpulsor"]=mision.nave.clasificacion_de_hiperimpulsor
            mision_nave_diccionario["mglt"]=mision.nave.mglt
            mision_nave_diccionario["clase_de_nave"]=mision.nave.clase_de_nave
            mision_nave_diccionario["pilotos"]=mision.nave.pilotos
            mision_nave_diccionario["peliculas"]=mision.nave.peliculas
            mision_diccionario["nave"]=mision_nave_diccionario

            lista_armas=[]
            for arma in mision.armas_utilizadas:
                mision_arma_diccionario={}
                mision_arma_diccionario["id"]=arma.id
                mision_arma_diccionario["nombre"]=arma.nombre
                mision_arma_diccionario["modelo"]=arma.modelo
                mision_arma_diccionario["fabricante"]=arma.fabricante
                mision_arma_diccionario["costo_en_creditos"]=arma.costo_en_creditos
                mision_arma_diccionario["longitud"]=arma.longitud
                mision_arma_diccionario["tipo"]=arma.tipo
                mision_arma_diccionario["descripcion"]=arma.descripcion
                mision_arma_diccionario["peliculas"]=arma.peliculas
                lista_armas.append(mision_arma_diccionario)
            mision_diccionario["armas_utilizadas"]=lista_armas

            lista_integrantes=[]
            for integrante in mision.integrantes_mision:
                mision_integrante_diccionario={}
                mision_integrante_diccionario["id"]=integrante.id
                mision_integrante_diccionario["nombre"]=integrante.nombre
                mision_integrante_diccionario["especie"]=integrante.especie
                mision_integrante_diccionario["genero"]=integrante.genero
                mision_integrante_diccionario["altura"]=integrante.altura
                mision_integrante_diccionario["peso"]=integrante.peso
                mision_integrante_diccionario["color_cabello"]=integrante.color_cabello
                mision_integrante_diccionario["color_ojos"]=integrante.color_ojos
                mision_integrante_diccionario["color_piel"]=integrante.color_piel
                mision_integrante_diccionario["nacimiento"]=integrante.nacimiento
                mision_integrante_diccionario["mundo_natal"]=integrante.mundo_natal
                mision_integrante_diccionario["fallecimiento"]=integrante.fallecimiento
                mision_integrante_diccionario["descripcion"]=integrante.descripcion
                lista_integrantes.append(mision_integrante_diccionario)
            mision_diccionario["integrantes_mision"]=lista_integrantes

            misiones.append(mision_diccionario)

        #with open(".txt","w") as f:
            #f.write(json.dumps(misiones, indent=4))


                


                

            
