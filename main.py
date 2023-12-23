class Vertice:
    def __int__(self,i):
        self.id = i
        self.vecinos = []
        self.visitado = False
        self.padre = None
        self.distancia = float('inf')

    def agregarVecino(self,v,p):
        if v not in self.vecinos:
            self.vecinos.append([v,p])

class Grafica:
    def __int__(self):
        self.vertices = {}

    def agregarVertice(self,id):
        if id not in self.vertices:
            self.vertices[id] = Vertice(id)

    def agregarArista(self,a,b,p):
        if a in self.verticesa and b in self.vertices:
            self.vertices[a].agregarVecino(b,p)
            self.vertices[b].agregarVecino(a,p)

    def imprimirGrafica(self):
        for v in self.vertices:
            print("La distancia entre"+str(v)+"es"+str(self.vertices[v].distancia)+"llegando desde"+str(self.
            vertices[v].padre))

    def camino(self,a,b):
        camino = []
        actual = b
        while actual != None:
            camino.insert(0,actual)
            actual = self.vertices[actual].padre
        return [camino,self.vertices[b].distancia]
    def minimo(self,lista):
        if len(lista) > 0:
            m = self.vertices[lista[0]].distancia
            v = lista[0]
            for e in lista:
                if m > self.vertices[e].distancia:
                    m = self.vertices[e].distancia
                    v = e
            return v

    def dijkstra(self,a):
        if a in self.vertices:
            self.vertices[a].distancia = 0
            actual = a
            noVisitados = []

            for v in self.vertices:
                if v !=a:
                    self.vertices[v].distancia = float('inf')
                self.vertices[v].padre = None
                noVisitados.append(v)
            while len(noVisitados) > 0:
                for vecino in self.vertices[actual].vecino:
                    if self.vertices[vecino[0]].visitado == False:
                        if self.vertices[actual].distancia + vecino[1] < self.vertices[vecino[0]].distancia:
                            self.vertices[vecino[0]].distancia = self.vertices[actual].distancia + vecino[1]
                            self.vertices[vecino[0]].padre = actual

                self.vertices[actual].visitado = True
                noVisitados.remove(actual)
                actual = self.minimo(noVisitados)
        else:
            return False
if __name__ == '__main__':
    g = Grafica()
    g.agregarVertice("Observatorio")
    g.agregarVertice("Tacubaya")
    g.agregarVertice("Juanacatlan")
    g.agregarVertice("Chapultepec")
    g.agregarVertice("Sevilla")
    g.agregarVertice("Insurgentes")
    g.agregarVertice("Cuauhtemoc")
    g.agregarVertice("Balderas")
    g.agregarVertice("Salto del agua")
    g.agregarVertice("Isabel La catolica ")
    g.agregarVertice("Pino Suarez")
    g.agregarVertice("Merced")
    g.agregarVertice("Candelaria")
    g.agregarVertice("San Lazaro")
    g.agregarVertice("Moctezuma")
    g.agregarVertice("Balbuena")
    g.agregarVertice("Boulevard Puerto Aereo")
    g.agregarVertice("Gomez Farias")
    g.agregarVertice("Zaragoza")
    g.agregarVertice("Pantitlan")
    # Linea 2
    g.agregarVertice("Cuatro Camino")
    g.agregarVertice("Panteones")
    g.agregarVertice("Tacuba")
    g.agregarVertice("Cuitlahuac")
    g.agregarVertice("Popotla")
    g.agregarVertice("Colegio Militar")
    g.agregarVertice("Normal")
    g.agregarVertice("San Cosme")
    g.agregarVertice("Revolucion")
    g.agregarVertice("Hidalgo")
    g.agregarVertice("Bellas artes")
    g.agregarVertice("Allende")
    g.agregarVertice("Zocalo")
    # Pino Suarez es tranborde
    g.agregarVertice("San Antonio Abad")
    g.agregarVertice("Chabacano")
    g.agregarVertice("Viaducto")
    g.agregarVertice("Xola")
    g.agregarVertice("Villa de Cortes")
    g.agregarVertice("Nativitas")
    g.agregarVertice("Portales")
    g.agregarVertice("Ermita")
    g.agregarVertice("General Anaya")
    g.agregarVertice("Tasqueña")
    # Linea 3
    g.agregarVertice("Indios Verdes")
    g.agregarVertice("Deportivo 18 de Marzo")
    g.agregarVertice("Potrero")
    g.agregarVertice("La raza")
    g.agregarVertice("Tlatelolco")
    g.agregarVertice("Guerrero")
    # Hidalgo es trasborde
    g.agregarVertice("Juarez")
    # Balderas es transborde
    g.agregarVertice("Niños Heroes")
    g.agregarVertice("Hospital General")
    g.agregarVertice("Centro Medico")
    g.agregarVertice("Etiopia")
    g.agregarVertice("Eugenia")
    g.agregarVertice("Division del Norte")
    g.agregarVertice("Zapata")
    g.agregarVertice("Coyoacan")
    g.agregarVertice("Viveros")
    g.agregarVertice("Miguel Angel de Quevedo")
    g.agregarVertice("Copilco")
    g.agregarVertice("Universidad")
    # Linea 4
    g.agregarVertice("Martin Carrera")
    g.agregarVertice("Talisman")
    g.agregarVertice("Bondojito")
    g.agregarVertice("Consulado")
    g.agregarVertice("Canal del norte")
    g.agregarVertice("Morelos")
    # Candelaria es transborde
    g.agregarVertice("Fray Servando")
    g.agregarVertice("Jamaica")
    g.agregarVertice("Santa Anita")
    # Linea 5
    # Pantitlan es transborde
    g.agregarVertice("Hangares")
    g.agregarVertice("Terminal area")
    g.agregarVertice("Oceania")
    g.agregarVertice("Aragon")
    g.agregarVertice("Eduardo Molina")
    # Consulado es transborde
    g.agregarVertice("Valle Gomez")
    g.agregarVertice("Misterios")
    # La raza es trasborde
    g.agregarVertice("Autobuses del norte")
    g.agregarVertice("Instituto del petroleo")
    g.agregarVertice("Politecnico")
    # Linea 6
    g.agregarVertice("El rosario")
    g.agregarVertice("Tezozomoc")
    g.agregarVertice("UAM Azcapotzalco")
    g.agregarVertice("Arena Ciudad de Mexico")
    g.agregarVertice("Norte 45")
    g.agregarVertice("Vallejo")
    # Instuto del petroleo es transborde
    g.agregarVertice("Lindavista")
    # Deportivo 18 de marzo es transborde
    g.agregarVertice("La Villa")
    # Martin Carrera es transborde
    # Linea 7
    # El rosario es transborde
    g.agregarVertice("Aquiles Serdan")
    g.agregarVertice("Camarones")
    g.agregarVertice("Refineria")
    # Tacuba es transborde
    g.agregarVertice("San Joaquin")
    g.agregarVertice("Polanco")
    g.agregarVertice("Auditorio")
    g.agregarVertice("Constituyentes")
    # Tacubaya es transborde
    g.agregarVertice("San Pedro de los Pinos")
    g.agregarVertice("San Antonio")
    g.agregarVertice("Mixcoac")
    g.agregarVertice("Barranca del Muerto ")
    # Linea 8
    g.agregarVertice("Garibaldi")
    # Bellas Artes es transborde
    g.agregarVertice("San Juan Letran")
    # Salto del agua es transborde
    g.agregarVertice("Doctores")
    g.agregarVertice("Obrera")
    # Chabacano es transborde
    g.agregarVertice("La viga")
    # Santa Anita es transborde
    g.agregarVertice("Coyuya")
    g.agregarVertice("Iztacalco")
    g.agregarVertice("Apatlaco")
    g.agregarVertice("Aculco")
    g.agregarVertice("Escuadron 201")
    g.agregarVertice("Atlalico")
    g.agregarVertice("Iztapalapa")
    g.agregarVertice("Cerro de la Estralla")
    g.agregarVertice("UAM")
    g.agregarVertice("Constitucion de 1917")
    # Linea 9
    # Tacubaya es transborde
    g.agregarVertice("Patriotismo")
    g.agregarVertice("Chilpancingo")
    # Centro Medico es transborde
    g.agregarVertice("Lazaro Cardenas")
    # Chabacano es transborde
    # Jamaica es transborde
    g.agregarVertice("Mixiuhca")
    g.agregarVertice("Velodromo")
    g.agregarVertice("Ciudad deportiva")
    g.agregarVertice("Puebla")
    # Pantitlan es transborde
    # Linea A
    # Pantitlan es transborde
    g.agregarVertice("Agricola Oriental")
    g.agregarVertice("Canal de San Juan")
    g.agregarVertice("Tepalcates")
    g.agregarVertice("Guelatao")
    g.agregarVertice("Peñon Viejo")
    g.agregarVertice("Acatitla")
    g.agregarVertice("Santa Marta")
    g.agregarVertice("Los reyes")
    g.agregarVertice("La paz")
    # Linea B
    g.agregarVertice("Buenavista")
    # Guerrero es transborde
    # Garibaldi es transborde
    g.agregarVertice("Lagunilla")
    g.agregarVertice("Tepito")
    # Morelos es trasborde
    # San lazaro es transborde
    g.agregarVertice("Ricardo Flores Magon")
    g.agregarVertice("Romero Rubio")
    # Oceania es transborde
    g.agregarVertice("Deportivo Oceania")
    g.agregarVertice("Bosque de Aragon")
    g.agregarVertice("Villa de Aragon")
    g.agregarVertice("Nezahualcoyotl")
    g.agregarVertice("Impulsora")
    g.agregarVertice("Rio de los remedios")
    g.agregarVertice("Muzquiz")
    g.agregarVertice("Ecatepec")
    g.agregarVertice("Olimpica")
    g.agregarVertice("Plaza Aragon")
    g.agregarVertice("Ciudad Azteca")
    # Linea 12
    # Mixcoac
    g.agregarVertice("Insurgentes Sur")
    g.agregarVertice("Hospital 20 de Noviembre")
    # Zapata es transborde
    g.agregarVertice("Parque de los venados")
    g.agregarVertice("Eje central")
    # Ermita es transborde
    g.agregarVertice("Mexicaltzingo")
    # Atlatlilco es transborde
    g.agregarVertice("Culhuacan ")
    g.agregarVertice("San Andres Tomatlan")
    g.agregarVertice("Lomas estrella ")
    g.agregarVertice("Calle 11")
    g.agregarVertice("Periferico Oriente")
    g.agregarVertice("Tezonco")
    g.agregarVertice("Olivos")
    g.agregarVertice("Nopalera")
    g.agregarVertice("Zapotitlan")
    g.agregarVertice("Tlaltenco")
    g.agregarVertice("Tlahuac")
    g.agregarArista("Pantitlan","Zaragoza",1320)
    g.agregarArista("Zaragoza","Gomez Farias",762)
    g.agregarArista("Gomez Farias","Boulevard Puerto Aereo",611)
    g.agregarArista("Boulevard Puerto Aereo","Balbuena",595)
    g.agregarArista("Balbuena","Moctezuma",703)
    g.agregarArista("Moctezuma","San lazaro",478)
    g.agregarArista("San Lazaro","Candelaria",866)
    g.agregarArista("Candelaria","Merced",698)
    g.agregarArista("Merced","Pino Suarez",745)
    g.agregarArista("Pino Suarez","Isabel La Catolica",382)
    g.agregarArista("Isabel La Catolica","Salto del Agua",445)
    g.agregarArista("Salto del Agua","Balderas",458)
    g.agregarArista("Balderas","Cuauhtemoc",409)
    g.agregarArista("Cuauhtemoc","Insurgentes",793)
    g.agregarArista("Insurgentes","Sevilla",645)
    g.agregarArista("Sevilla","Chapultepec",501)
    g.agregarArista("Chapultepec","Juanacatlan",973)
    g.agregarArista("Juanacatlan","Tacubaya",1158)
    g.agregarArista("Tacubaya","Observatorio",1262)
    g.agregarArista("Cuatro Caminos","Panteones",1639)
    g.agregarArista("Panteones","Tacuba",1416)
    g.agregarArista("Tacuba","Cuitlahuac",637)
    g.agregarArista("Cuitlahuac","Popotla",620)
    g.agregarArista("Popotla","Colegio Militar",462)
    g.agregarArista("Colegio Militar","Normal",516)
    g.agregarArista("Normal","San Cosme",657)
    g.agregarArista("San Cosme","Revolucion",537)
    g.agregarArista("Revolucion","Hidalgo",587)
    g.agregarArista("Hidalgo","Bellas Artes",447)
    g.agregarArista("Bellas Artes","Allende",387)
    g.agregarArista("Allende","Zocalo",602)
    g.agregarArista("Zocalo","Pino Suarez",745)
    g.agregarArista("Pino Suarez","San Antonio Abad",817)
    g.agregarArista("San Antonio Abad","Chabacano",642)
    g.agregarArista("Chabacano","Viaducto",774)
    g.agregarArista("Viaducto","Xola",490)
    g.agregarArista("Xola","Villa de Cortes",698)
    g.agregarArista("Villa de Cortes","Nativitas",750)
    g.agregarArista("Nativitas","Portales",924)
    g.agregarArista("Portales","Ermita",748)
    g.agregarArista("Ermita","General Anaya",838)
    g.agregarArista("General Anaya","Tasqueña",1330)
    g.agregarArista("Indios Verdes","Deportivo 18 de Marzo",1166)
    g.agregarArista("Deportivo 18 de Marzo","Potrero",966)
    g.agregarArista("Potrero","La Raza",1106)
    g.agregarArista("La Raza","Tlatelolco",1445)
    g.agregarArista("Tlatelolco","Guerrero",1042)
    g.agregarArista("Guerrero","Hidalgo",702)
    g.agregarArista("Hidalgo","Juarez",251)
    g.agregarArista("Juarez","Balderas",659)
    g.agregarArista("Balderas","Niños Heroes",665)
    g.agregarArista("Niños Heroes","Hospital General",559)
    g.agregarArista("Hospital General","Centro Medico",653)
    g.agregarArista("Centro Medico","Etiopia",1119)
    g.agregarArista("Etiopia","Eugenia",950)
    g.agregarArista("Eugenia","Division del Norte",715)
    g.agregarArista("Division del Norte","Zapata",794)
    g.agregarArista("Zapata","Coyoacan",1153)
    g.agregarArista("Coyoacan","Viveros",908)
    g.agregarArista("Viveros","Miguel Angel de Quevedo",824)
    g.agregarArista("Miguel Angel de Quevedo","Copilco",1295)
    g.agregarArista("Copilco","Universidad",1306)
    g.agregarArista("Santa Anita","Jamaica",758)
    g.agregarArista("Jamaica","Fray Servenado",1033)
    g.agregarArista("Fray Servando","Candelaria",633)
    g.agregarArista("Candelaria","Morelos",1062)
    g.agregarArista("Morelos","Canal del Norte",910)
    g.agregarArista("Canal del Norte","Consulado",884)
    g.agregarArista("Consulado","Bondojito",645)
    g.agregarArista("Bondojito","Talisman",959)
    g.agregarArista("Talisman","Martin Carrera",1129)
    g.agregarArista("Politecnico","Instituto del Petroleo",1188)
    g.agregarArista("Instituto del Petroleo","Autobuses del Norte",1067)
    g.agregarArista("Autobuses del Norte","La Raza",975)
    g.agregarArista("La Raza","Misterios",892)
    g.agregarArista("Misterios","Valle Gomez",969)
    g.agregarArista("Valle Gomez","Consulado",679)
    g.agregarArista("Consulado","Eduardo Molina",815)
    g.agregarArista("Eduardo Molina","Aragon",860)
    g.agregarArista("Aragon","Oceania",1219)
    g.agregarArista("Oceania","Terminal Aerea",1174)
    g.agregarArista("Terminal Aerea","Hangares",1153)
    g.agregarArista("Hangares","Pantitlan",1644)
    g.agregarArista("El Rosario","Tezozomoc",1257)
    g.agregarArista("Tezozomoc","Azcapotzalco",973)
    g.agregarArista("Azcapotzalco","Ferreria",1173)
    g.agregarArista("Ferreria","Norte 45",1072)
    g.agregarArista("Norte 45","Vallejo",660)
    g.agregarArista("Vallejo","Instituto del Petroleo",755)
    g.agregarArista("Instituto del Petroleo","Lindavista",1258)
    g.agregarArista("Lindavista","Deportivo de 18 de Marzo",1075)
    g.agregarArista("deportivo 18 de Marzo","La Villa",570)
    g.agregarArista("La Villa","Martin Carrera",1141)
    g.agregarArista("El Rosario","Aquiles Serdan",1615)
    g.agregarArista("Aquiles Serdan","Camarones",1402)
    g.agregarArista("Camarones","Refineria",952)
    g.agregarArista("Refineria","Tacuba",1295)
    g.agregarArista("Tacuba","San Joaquin",1433)
    g.agregarArista("San Joaquin","Polanco",1163)
    g.agregarArista("Polanco","Auditorio",812)
    g.agregarArista("Auditorio","Constituyentes",1430)
    g.agregarArista("Contituyentes","Tacubaya",1005)
    g.agregarArista("Tacubaya","San Pedro de los pinos",1084)
    g.agregarArista("San Pedro de los pinos","San Antonio",606)
    g.agregarArista("San Antonio","Mixcoac",788)
    g.agregarArista("Mixcoac","Barranca del Muerto",1476)
    g.agregarArista("Garibaldi","Bellas Artes",634)
    g.agregarArista("Bellas Artes","San Juan de Letran",456)
    g.agregarArista("San Juan de Letran","Salto del agua",292)
    g.agregarArista("Salto del Agua","Doctores",564)
    g.agregarArista("Doctores","Obrera",761)
    g.agregarArista("Obrera","Chabacano",1143)
    g.agregarArista("Chabacano","La Viga",843)
    g.agregarArista("La Viga","Santa Anita",633)
    g.agregarArista("Santa Anita","Coyuya",968)
    g.agregarArista("Coyuya","Iztacalco",993)
    g.agregarArista("Iztacalco","Apatlaco",910)
    g.agregarArista("Apatlaco","Aculco",534)
    g.agregarArista("Aculco","Escuadrom 201",789)
    g.agregarArista("Escuadron 201","Atlalilco",1738)
    g.agregarArista("Atlalico","Iztapalapa",732)
    g.agregarArista("Iztapalapa","Cerro de la Estrella",717)
    g.agregarArista("Cerro de la Estrella","UAM",1135)
    g.agregarArista("UAM","Constitucion de 1917",1137)
    g.agregarArista("Pantitlan","Puebla",1380)
    g.agregarArista("Puebla","Ciudad Deportiva",800)
    g.agregarArista("Ciudad Deportiva","Velodoromo",1110)
    g.agregarArista("Velodromo","Mixiuhca",821)
    g.agregarArista("Mixiuhca","Jamaica",942)
    g.agregarArista("Jamaica","Chabacano",1031)
    g.agregarArista("Chabacano","Lazaro Cardenas",1000)
    g.agregarArista("Lazaro Cardenas","Centro Medico",1059)
    g.agregarArista("Centro Medico","Chilpancingo",1152)
    g.agregarArista("Chilpancingo","Patriotismo",955)
    g.agregarArista("Patriotismo","Tacubaya",1133)
    g.agregarArista("Pantitlan","Agricola Oriental",1409)
    g.agregarArista("Agricola Oriental","Canal de San Juan",1093)
    g.agregarArista("Canal de San Juan","Tepalcates",1456)
    g.agregarArista("Tepalcates","Guelatao",1161)
    g.agregarArista("Guelatao","Peñon Viejo",2206)
    g.agregarArista("Peñon viejo","Acatitla",1379)
    g.agregarArista("Acatitla","Santa Marta",1100)
    g.agregarArista("Santa Marta","Los Reyes",1783)
    g.agregarArista("Los Reyes","La Paz",1956)
    g.agregarArista("Ciudad Azteca","Plaza Aragon",574)
    g.agregarArista("Plaza Aragon","Olimpica",709)
    g.agregarArista("Olimpica","Ecatepec",596)
    g.agregarArista("Ecatepec","Muzquiz",1485)
    g.agregarArista("Muzquiz","Rio de los Remedios",1155)
    g.agregarArista("Rio de los Remedios","Impulsora",436)
    g.agregarArista("Impulsora","Nezahualcoyotl",1393)
    g.agregarArista("Nezahualcoyotl","Villa de Aragon",1335)
    g.agregarArista("Villa de Aragon","Bosques de Aragon",784)
    g.agregarArista("Bosques de Aragon","Deportivo Oceania",1165)
    g.agregarArista("Deportivo Oceania","Oceania",863)
    g.agregarArista("Oceania","Romero Rubio",809)
    g.agregarArista("Romero Ruibio","Ricardo Flores Magon",908)
    g.agregarArista("Ricardo Flores Magon","San Lazaro",907)
    g.agregarArista("San Lazaro","Morelos",1296)
    g.agregarArista("Morelos","Tepito",498)
    g.agregarArista("Tepito","Lagunilla",611)
    g.agregarArista("Lagunilla","Garibaldi",474)
    g.agregarArista("Garibaldi","Guerrero",757)
    g.agregarArista("Guerrero","Buenavista",521)
    g.agregarArista("Tlahuac","Tlatenco",1298)
    g.agregarArista("Tlatenco","Zapotitlan",1115)
    g.agregarArista("Zapotitlan","Nopalera",1276)
    g.agregarArista("Nopalera","Olivos",1360)
    g.agregarArista("Olivos","Tezonco",490)
    g.agregarArista("Tezonco","Periferico Oriente",1545)
    g.agregarArista("Periferico Oriente","Calle 11")
    g.agregarArista("Calle 11","Lomas Estrella",906)
    g.agregarArista("Lomas Estrella","San Andres Tomatlan",1060)
    g.agregarArista("San Andres Tomatlan","Culhuacan",990)
    g.agregarArista("Culhuacan","Atlalilco",1671)
    g.agregarArista("Atlalilco","Mexicaltzingo",1922)
    g.agregarArista("Mexicaltzingo","Ermita",1805)
    g.agregarArista("Ermita","Eje Central",895)
    g.agregarArista("Eje Central","Parque de los venados",1280)
    g.agregarArista("Parque de los venados","Zapata",563)
    g.agregarArista("Zapata","Hospital 20 de Noviembre",450)
    g.agregarArista("Hospital 20 de Noviembre","Insurgentes Sur",725)
    g.agregarArista("Insurgentes Sur","Mixcoac",651)

    print("⧹n⧹nLa ruta mas rapida por Dijkstra junto con su costo es:")
    g.dijkstra(1)
    print(g.camino("Normal","Universidad"))
    print("⧹n Los valores finales de la grafica son los siguientes:")
    g.imprimirGrafica()



