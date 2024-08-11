class Planeta:
    def __init__(self, nombre, diametro, periodo_de_rotacion, periodo_de_orbita, gravedad, poblacion, clima, terreno, superficie_acuatica):
        self.nombre=nombre
        self.diametro=diametro
        self.periodo_de_rotacion=periodo_de_rotacion
        self.periodo_de_orbita=periodo_de_orbita
        self.gravedad=gravedad
        self.poblacion=poblacion
        self.clima=clima
        self.terreno=terreno
        self.superficie_acuatica=superficie_acuatica

    def mostrar_planetas(self,peliculas_obj,personajes_obj):
        print(f'\n>>  Nombre: {self.nombre}')
        print(f'    - Periodo de Órbita: {self.periodo_de_orbita}')
        print(f'    - Periodo de Rotacion: {self.periodo_de_rotacion}')
        print(f'    - Cantidad de habitantes: {self.poblacion}')
        print(f'    - Tipo de clima: {self.clima}')
        lista_episodios=[]
        for x in peliculas_obj:
            for y in x.planetas:
                if y.nombre==self.nombre:
                    lista_episodios.append(y.nombre)
        for episodio in lista_episodios:
            print(f'    - Episodio: {episodio}')

        lista_personajes=[]
        for personaje in personajes_obj:
            if self.nombre==personaje.mundo_natal:
                lista_personajes.append(personaje)
        for personaje in lista_personajes:
            episodio.mostrar_nombre_personajes()
            

        

    