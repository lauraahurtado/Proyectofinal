class Pelicula:
    def __init__(self, titulo, numero_del_episodio, fecha_de_lanzamiento, opening_crawl, nombre_del_director, personajes, planetas, naves, vehiculos, especies, productor):
        self.titulo=titulo
        self.numero_del_episodio=numero_del_episodio
        self.fecha_de_lanzamiento=fecha_de_lanzamiento
        self.opening_crawl=opening_crawl
        self.nombre_del_director=nombre_del_director
        self.personajes=personajes
        self.planetas=planetas
        self.naves=naves
        self.vehiculos=vehiculos
        self.especies=especies
        self.productor=productor

    def mostrar_peliculas(self):
        print(f'\tTítulo: {self.titulo}')
        print(f'\tNúmero del episodio: {self.numero_del_episodio}')
        print(f'\tFecha de Lanzamiento: {self.fecha_de_lanzamiento}')
        print(f'\tOpening crawl: {self.opening_crawl}')
        print(f'\tNombre del director: {self.nombre_del_director}')