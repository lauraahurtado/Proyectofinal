class Mision:
    def __init__(self, numero_de_mision, nombre, planeta, nave, armas_utlizadas, integrantes_mision):
        self.numero_de_mision=numero_de_mision
        self.nombre=nombre
        self.planeta=planeta
        self.nave=nave
        self.armas_utilizadas=armas_utlizadas
        self.integrantes_mision=integrantes_mision
    
    def visualizar_mision(self):
        print(f'\n>>  Nombre de la Mision: {self.nombre}')
        print(f'    - Nombre del planeta: {self.planeta.nombre}')
        print(f'    - Nombre de la nave: {self.nave.nombre}')
        print(f'        * ID: {self.nave.id}')
        print(f'        * Modelo: {self.nave.modelo}')
        print(f'        * Fabricante: {self.nave.fabricante}')
        print(f'        * Costo en creditos: {self.nave.costo_en_creditos}')
        print(f'        * Longitud: {self.nave.longitud}')
        print(f'        * Velocidad maxima: {self.nave.velocidad_maxima}')
        print(f'        * Tripulacion: {self.nave.tripulacion}')
        print(f'        * Pasajeros: {self.nave.pasajeros}')
        print(f'        * Capacidad de carga: {self.nave.capacidad_de_carga}')
        print(f'        * Consumibles: {self.nave.consumibles}')
        print(f'        * Clasificacion de hiperimpulsor: {self.nave.clasificacion_de_hiperimpulsor}')
        print(f'        * MGLT: {self.nave.mglt}')
        print(f'        * Clase de nave: {self.nave.clase_de_nave}')
        print(f'        * Piloto: {self.nave.pilotos}')
        print(f'        * Peliculas: {self.nave.peliculas}')
        print(f'    - Lista de armas: ')
        contador=1
        for arma in self.armas_utilizadas:
            print(f'        {contador}. {arma.nombre}')
            print(f'            * ID: {arma.id}')
            print(f'            * Modelo: {arma.modelo}')
            print(f'            * Fabricante: {arma.fabricante}')
            print(f'            * Costo en creditos: {arma.costo_en_creditos}')
            print(f'            * Longitud: {arma.longitud}')
            print(f'            * Tipo: {arma.tipo}')
            print(f'            * Descripcion: {arma.descripcion}')
            print(f'            * Peliculas: {arma.peliculas}')
            contador+=1
        print(f'    - Lista de integrantes de la mision:')
        contador=1
        for integrante in self.integrantes_mision:
            print(f'        {contador}. {integrante.nombre}')
            print(f'            * ID: {integrante.id}')
            print(f'            * Especie: {integrante.especie}')
            print(f'            * Genero: {integrante.genero}')
            print(f'            * Altura: {integrante.altura}')
            print(f'            * Peso: {integrante.peso}')
            print(f'            * Color de cabello: {integrante.color_cabello}')
            print(f'            * Color de ojos: {integrante.color_ojos}')
            print(f'            * Color de piel: {integrante.color_piel}')
            print(f'            * Nacimiento: {integrante.nacimiento}')
            print(f'            * Mundo natal: {integrante.mundo_natal}')
            print(f'            * Fallecimiento:{integrante.fallecimiento}')
            print(f'            * Descripcion: {integrante.descripcion}')
            contador+=1
        
