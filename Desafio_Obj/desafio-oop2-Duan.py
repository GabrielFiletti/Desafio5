from opencage.geocoder import OpenCageGeocode
from ipyleaflet import *
from pprint import pprint

class Biodiversidade_csv:
    def __init__(self, arquivo):
        self.arquivo = list(open(arquivo))

    def qtdLinhasDadosFaltantes(self):
        self.lista_faltantes = []
        titulos = self.arquivo[0].split(";")
        
        [self.lista_faltantes.append([titulos[i].replace('\n',''),0]) for i in range(0,len(titulos))]
        #for i in range(0,len(titulos)):
        #    self.lista_faltantes.append([titulos[i].replace('\n',''),0])

        for i in range(1,len(self.arquivo)):
            linha = self.arquivo[i].split(";")
            for j in range(0,len(linha)):
                if linha[j] == "" or linha[j].lower() == "sem informações":
                    self.lista_faltantes[j][1] += 1
        
        media = self.lista_faltantes[:]
        
        for i in range(0,len(media)):
            media[i][1] = round(media[i][1] / len(self.arquivo[1:]),3)
        
        print("--- Media de Dados Faltantes por Coluna ---")
        print(media)
        

    def nivelTax(self, inicio=1):
        # inico = item inicial a ser impresso ate o ultimo (default = 1)
        # pegando indice da coluna "Nivel taxonomico"
        # pra garantir q a funcao funcionara caso a coluna mude de posicao
        ind = self.arquivo[0].split(";").index("Nivel taxonomico")
        
        # inicializando lista com valores da coluna "Nivel taxonomico"
        nvTax = []
        for i in range(1,len(self.arquivo)):
            # append somente dos valores da coluna "Nivel taxonomico"
            nvTax.append(self.arquivo[i].split(";")[ind])
        
        print("--- Maximo Nivel Taxonomico Encontrado ---")
        for i in range(inicio,len(nvTax)):
            print("Item",i+1,":",nvTax[i])
    
    def filtro_ocorrencias(self, categoria, filtro):
        ''' --- DESCRICAO DE USO DO PARAMETRO "filtro" ---
        > A funcao ira retornar os itens que possuem o conteudo do filtro
          em comum.
        > Parametro 1: insira o numero correspondente a categoria desejada
        > Parametro 2: insira o valor correspondente a categoria escolhida
        > Opcoes de filtro:
            0- Nome da instituicao
            1- Sigla da instituicao
            2- Nome da base de dados
            3- Sigla da base de dados
            4- Responsavel pelo registro
            5- Numero do registro no portal
            6- Numero do registro na base de dados	
            7- Data do registro
            8- Data do evento
            9- Data de Carencia
            10- Nome cientifico
            11- Nome comum
            12- Nome cientifico na base de dados
            13- Nivel taxonomico
            14- Numero de individuos
            15- Reino
            16- Filo
            17- Classe
            18- Ordem
            19- Familia
            20- Genero
            21- Especie
            22- Estado de conservacao
            23- Categoria de Ameaca
            24- Localidade
            25- Pais
            26- Estado/Provincia
            27- Municipiofrom pprint import pprint
            28- Status defrom pprint import pprint
            29- Latitude
            30- Longitudefrom pprint import pprint
            31- Outras infrom pprint import pprint
            32- Jurisdicafrom pprint import pprint
            33- Destino do Material

            Exemplo de uso: 
                obj = Biodiversidade_csv()
                obj.filtro_ocorrencias(1,"JBRJ")
                --- OUTPUT:
                    Numero de ocorrencias do filtro: 10
        '''
        self.ocorrencia = []
        for i in range(0,len(self.arquivo[1:])):
            if self.arquivo[i].split(";")[categoria].lower() == filtro.lower():
                self.ocorrencia.append([self.arquivo[i].split(";")]) 
        if len(self.ocorrencia) == 0:
            print("Nao ha ocorrencias do filtro inserido ou a categoria inserida eh invalida.")
        else:       
            print("Numero de ocorrencias do filtro:",len(self.ocorrencia))
        return self.ocorrencia
    
    def mapa(self):
        self.latLong = []       # Lista de listas: cada sublista esta no formato [lat,long]
        [self.latLong.append([i.split(";")[29],i.split(";")[30]]) for i in self.arquivo[1:]]
        
        
        key = 'b3581bc610a644f896bd87fc2cd8e6ce'
        geocoder = OpenCageGeocode(key)

        #center = (-23.3245302,-51.1692355)  #coordenadas
        results = geocoder.reverse_geocode(self.latLong[32][0], self.latLong[32][1])
        pprint(results)
        
        """ BLIND TRY
        for i in self.latLong:
            if (cidade no arquivo [iteracao i] == cidade no geocoder[iteracao i]):
                return True
            else:
                return False
        """


        #print(len(self.latLong))

        #[self.latLong.append([self.arquivo[i][29],self.arquivo[i+1][30]]) for i in range(0,len(self.arquivo[1:]))]
        
        #print(self.latLong)
        '''
        key = "b3581bc610a644f896bd87fc2cd8e6ce"
        geocoder = OpenCageGeocode(key)

        center = (-23.3245302,-51.1692355)  #coordenadas
        map = Map(center=center, zoom = 6)  # centraliza
        marker = Marker(location=center, draggable=False)
        marker2 = Marker(location=(-23.4,-51.2), draggable=False)
        map.add_layer(marker)
        map.add_layer(marker2)
        map
        pass
        '''


        
obj = Biodiversidade_csv("portalbio_export_17-10-2019-13-06-22.csv")
#obj.qtdLinhasDadosFaltantes()
#obj.nivelTax()
#obj.filtro_ocorrencias(1,"JBRJ")                   #OK
obj.mapa()