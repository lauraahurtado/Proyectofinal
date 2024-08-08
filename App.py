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

    # CREACION DE OBJETOS TIPO (Personaje) CON LOS DATOS DEL CSV

    def crear_personajes_csv(self):
        with open('Proyectofinal/starwars/csv/characters.csv',newline='') as archivo_csv:
            lector_csv=csv.reader(archivo_csv,delimiter=',')
            contador=0
            for fila in lector_csv:
                if contador>0:
                    self.personajes_csv_obj.append(Personaje_cvs(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11],fila[12]))
                contador+=1

    # CREACION DE OBJETOS TIPO (Nave) CON LOS DATOS DEL CSV.

    def crear_naves_csv(self):
        with open ('Proyectofinal/starwars/csv/starships.csv',newline='') as archivo_csv:
            lector_csv=csv.reader(archivo_csv,delimiter=',')
            contador=0
            for fila in lector_csv:
                if contador>0:
                    self.naves_csv_obj.append(Nave_cvs(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9],fila[10],fila[11],fila[12],fila[13],fila[14],fila[15]))
                contador+=1
    
    # CREACION DE OBJETOS (Armas) CON LOS DATOS DEL CSV.

    def crear_armas_csv(self):
        with open('Proyectofinal/starwars/csv/weapons.csv',newline='') as archivo_csv:
            lector_csv=csv.reader(archivo_csv,delimiter=',')
            contador=0
            for fila in lector_csv:
                if contador>0:
                    self.armas_csv_obj.append(Arma_csv(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8]))
                contador+=1
    
    # CREACION DE OBJETOS (Planetas) CON LOS DATOS DE CSV.

    def crear_planetas_csv(self):
        with open ('Proyectofinal/starwars/csv/planets.csv') as archivo_csv:
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
        ax.bar(lista_planetas_csv_personajes,lista_planetas_csv_personajes)
        plt.title('Cantidad de personas por planeta')
        plt.xlabel('Planeta')
        plt.ylabel('Cantidad de personas')
        plt.xticks(rotation=90) #Rotacion de la disposicion visula de cada planeta en el eje x para mejor estetica
        plt.show()

    