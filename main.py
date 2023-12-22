# Algoritmo de Dijsktra
class arista:
    def __int__(self, id):
        self.id = id
        self.vecinos = []
        self.visitados = False
        self.padre = None
        #Ponderación o distancia
        #self.distancia= float('inf')
        #Esto puesto que el costo desconocido es infinito hasta recorrerlo

    """
        def agregar_vecino(self, vertice, p):
        if vertice not in self.vecinos:
            self.vecinos.append([vertice, p])
    """

class vertice:
    def __int__(self, vertices):
        self.vertices = {}
        self.distancia = float

class Grafica:
    def __int__(self):
        self.vertices ={}

    def agregar_vecino(self, vertice, p):
        if vertice not in self.vecinos:
            self.vecinos.append([vertice, p])

    def agregar_vertice(self, id):
        if id not in self.vertices:
            self.vertices[id] = vertice(id)

    def agregar_arista(self, vertice_a, vertice_b, peso):
        if vertice_a in self.vertices and vertice_b in self.vertices:
            self.vertices[vertice_a].agregar_vecino(vertice_b, peso)
            self.vertices[vertice_a].agregar_vecino(vertice_b, peso)
            self.G.add_edge(vertice_a,vertice_b,peso)

    def obtener_camino(self, vertice_b):
        camino = 0
        actual = vertice_b
        while (actual != None):
            camino.insert(0, actual)
            actual = self.vertices[actual].padre
        return [camino, self.vertices[vertice_b].distancia]

    def minimo(self,lista):
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia
            vertice = lista[0]
            for e in lista:
                if m>self.vertices[e].distancia:
                    m=self.vertices[e].distancia
                    vertice=e
            return vertice

    def dijkstra(self,vertice_a):
        if vertice in self.vertices:
            self.vertices[vertice_a].distancia = 0
            actual = vertice_a
            no_visitados = []

         # Se agregan todos los nodos no visitados
        for v in self.vertices:
            if v !=vertice_a:
                self.vertices[vertice].distancia= float('inf')
            self.vertices[vertice].padre=None
            no_visitados
        # En esta parte es cuando dado los vertices se toma el camino minimo
        while(len(no_visitados) > 0):
            for vecino in self.vertices[actual].vecinos:
                if self.vertices[vecino[0]].visitado == False:
                    if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                        self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                        self.vertices[vecino[0]].padre = actual
            self.vertices[actual].visitado = True
            no_visitados.remove(actual)
            actual = self.minimo(no_visitados)
        else:
            return False

if __name__ =='__main__':
# Aqui se define a las arista como estaciones del metro
# Los vertices como la distancia que hay entre estaciones
    g  = Grafica()
    g.agregar_vertice("Observatorio")
    g.agregar_vertice("Tacubaya")
    g.agregar_vertice("Juanacatlan")
    g.agregar_vertice("Chapultepec")
    g.agregar_vertice("Sevilla")
    g.agregar_vertice("Insurgentes")
    g.agregar_vertice("Cuauhtemoc")
    g.agregar_vertice("Balderas")
    g.agregar_vertice("Salto del agua")
    g.agregar_vertice("Isabel La catolica ")
    g.agregar_vertice("Pino Suarez")
    g.agregar_vertice("Merced")
    g.agregar_vertice("Candelaria")
    g.agregar_vertice("San Lazaro")
    g.agregar_vertice("Moctezuma")
    g.agregar_vertice("Balbuena")
    g.agregar_vertice("Boulevard Puerto Aereo")
    g.agregar_vertice("Gomez Farias")
    g.agregar_vertice("Zaragoza")
    g.agregar_vertice("Pantitlan")
    # Linea 2
    g.agregar_vertice("Cuatro Camino")
    g.agregar_vertice("Panteones")
    g.agregar_vertice("Tacuba")
    g.agregar_vertice("Cuitlahuac")
    g.agregar_vertice("Popotla")
    g.agregar_vertice("Colegio Militar")
    g.agregar_vertice("Normal")
    g.agregar_vertice("San Cosme")
    g.agregar_vertice("Revolucion")
    g.agregar_vertice("Hidalgo")
    g.agregar_vertice("Bellas artes")
    g.agregar_vertice("Allende")
    g.agregar_vertice("Zocalo")
    # Pino Suarez es tranborde
    g.agregar_vertice("San Antonio Abad")
    g.agregar_vertice("Chabacano")
    g.agregar_vertice("Viaducto")
    g.agregar_vertice("Xola")
    g.agregar_vertice("Villa de Cortes")
    g.agregar_vertice("Nativitas")
    g.agregar_vertice("Portales")
    g.agregar_vertice("Ermita")
    g.agregar_vertice("General Anaya")
    g.agregar_vertice("Tasqueña")
    # Linea 3
    g.agregar_vertice("Indios Verdes")
    g.agregar_vertice("Deportivo 18 de Marzo")
    g.agregar_vertice("Potrero")
    g.agregar_vertice("La raza")
    g.agregar_vertice("Tlatelolco")
    g.agregar_vertice("Guerrero")
    # Hidalgo es trasborde
    g.agregar_vertice("Juarez")
    # Balderas es transborde
    g.agregar_vertice("Niños Heroes")
    g.agregar_vertice("Hospital General")
    g.agregar_vertice("Centro Medico")
    g.agregar_vertice("Etiopia")
    g.agregar_vertice("Eugenia")
    g.agregar_vertice("Division del Norte")
    g.agregar_vertice("Zapata")
    g.agregar_vertice("Coyoacan")
    g.agregar_vertice("Viveros")
    g.agregar_vertice("Miguel Angel de Quevedo")
    g.agregar_vertice("Copilco")
    g.agregar_vertice("Universidad")
    # Linea 4
    g.agregar_vertice("Martin Carrera")
    g.agregar_vertice("Talisman")
    g.agregar_vertice("Bondojito")
    g.agregar_vertice("Consulado")
    g.agregar_vertice("Canal del norte")
    g.agregar_vertice("Morelos")
    # Candelaria es transborde
    g.agregar_vertice("")
    g.agregar_vertice("Fray Servando")
    g.agregar_vertice("Jamaica")
    g.agregar_vertice("Santa Anita")
    # Linea 5
    # Pantitlan es transborde
    g.agregar_vertice("Hangares")
    g.agregar_vertice("Terminal area")
    g.agregar_vertice("Oceania")
    g.agregar_vertice("Aragon")
    g.agregar_vertice("Eduardo Molina")
    g.agregar_vertice("Consulado")
    g.agregar_vertice("Valle Gomez")
    g.agregar_vertice("Misterios")
    # La raza es trasborde
    g.agregar_vertice("Autobuses del norte")
    g.agregar_vertice("Instituto del petroleo")
    g.agregar_vertice("Politecnico")
    #Linea 6
    g.agregar_vertice("El rosario")
    g.agregar_vertice("Tezozomoc")
    g.agregar_vertice("UAM Azcapotzalco")
    g.agregar_vertice("Arena Ciudad de Mexico")
    g.agregar_vertice("Norte 45")
    g.agregar_vertice("Vallejo")
    # Instuto del petroleo es transborde
    g.agregar_vertice("Lindavista")
    # Deportivo 18 de marzo es transborde
    g.agregar_vertice("La Villa")
    # Martin Carrera es transborde
    # Linea 7
    # El rosario es transborde
    g.agregar_vertice("Aquiles Serdan")
    g.agregar_vertice("Camarones")
    g.agregar_vertice("Refineria")
    # Tacuba es transborde
    g.agregar_vertice("San Joaquin")
    g.agregar_vertice("Polanco")
    g.agregar_vertice("Auditorio")
    g.agregar_vertice("Constituyentes")
    # Tacubaya es transborde
    g.agregar_vertice("San Pedro de los Pinos")
    g.agregar_vertice("San Antonio")
    g.agregar_vertice("Mixcoac")
    g.agregar_vertice("Barranca del Muerto ")
    # Linea 8
    g.agregar_vertice("Garibaldi")
    # Bellas Artes es transborde
    g.agregar_vertice("San Juan Letran")
    # Salto del agua es transborde
    g.agregar_vertice("Doctores")
    g.agregar_vertice("Obrera")
    # Chabacano es transborde
    g.agregar_vertice("La viga")
    # Santa Anita es transborde
    g.agregar_vertice("Coyuya")
    g.agregar_vertice("Iztacalco")
    g.agregar_vertice("Apatlaco")
    g.agregar_vertice("Aculco")
    g.agregar_vertice("Escuadron 201")
    g.agregar_vertice("Atlalico")
    g.agregar_vertice("Iztapalapa")
    g.agregar_vertice("Cerro de la Estralla")
    g.agregar_vertice("UAMa")
    g.agregar_vertice("Constitucion de 1917")
    # Linea 9
    # Tacubaya es transborde
    g.agregar_vertice("Patriotismo")
    g.agregar_vertice("Chilpancingo")
    # Centro Medico es transborde
    g.agregar_vertice("Lazaro Cardenas")
    # Chabacano es transborde
    # Jamaica es transborde
    g.agregar_vertice("Mixiuhca")
    g.agregar_vertice("Velodromo")
    g.agregar_vertice("Ciudad deportiva")
    g.agregar_vertice("Puebla")
    # Pantitlan es transborde
    # Linea A
    # Pantitlan es transborde
    g.agregar_vertice("Agricola Oriental")
    g.agregar_vertice("Canal de San Juan")
    g.agregar_vertice("Tepalcates")
    g.agregar_vertice("Guelatao")
    g.agregar_vertice("Peñon Viejo")
    g.agregar_vertice("Acatitla")
    g.agregar_vertice("Santa Marta")
    g.agregar_vertice("Los reyes")
    g.agregar_vertice("La paz")
    # Linea B
    g.agregar_vertice("Buenavista")
    # Guerrero es transborde
    # Garibaldi es transborde
    g.agregar_vertice("Lagunilla")
    g.agregar_vertice("Tepito")
    # Morelos es trasborde
    # San lazaro es transborde
    g.agregar_vertice("Ricardo Flores Magon")
    g.agregar_vertice("Romero Rubio")
    # Oceania es transborde
    g.agregar_vertice("Deportivo Oceania")
    g.agregar_vertice("Bosque de Aragon")
    g.agregar_vertice("Villa de Aragon")
    g.agregar_vertice("Nezahualcoyotl")
    g.agregar_vertice("Impulsora")
    g.agregar_vertice("Rio de los remedios")
    g.agregar_vertice("Muzquiz")
    g.agregar_vertice("Ecatepec")
    g.agregar_vertice("Olimpica")
    g.agregar_vertice("Plaza Aragon")
    g.agregar_vertice("Ciudad Azteca")
    #Linea 12
    # Mixcoac
    g.agregar_vertice("Insurgentes Sur")
    g.agregar_vertice("Hospital 20 de Noviembre")
    # Zapata es transborde
    g.agregar_vertice("Parque de los venados")
    g.agregar_vertice("Eje central")
    # Ermita es transborde
    g.agregar_vertice("Mexicaltzingo")
    # Atlatlilco es transborde
    g.agregar_vertice("Culhuacan ")
    g.agregar_vertice("San Andres Tomatlan")
    g.agregar_vertice("Lomas estrella ")
    g.agregar_vertice("Calle 11")
    g.agregar_vertice("Periferico Oriente")
    g.agregar_vertice("Tezonco")
    g.agregar_vertice("Olivos")
    g.agregar_vertice("Nopalera")
    g.agregar_vertice("Zapotitlan")
    g.agregar_vertice("Tlaltenco")
    g.agregar_vertice("Tlahuac")






