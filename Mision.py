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
        print(f'    - Lista de armas: ')
        contador=1
        for arma in self.armas_utilizadas:
            print(f'        {contador}. {arma.nombre}')
            contador+=1
        print(f'    - Lista de integrantes de la mision:')
        contador=1
        for integrante in self.integrantes_mision:
            print(f'        {contador}. {integrante.nombre}')
            contador+=1
        
