from opencage.geocoder import OpenCageGeocode
from ipyleaflet import *
from pprint import pprint

class Biodiversidade_csv:
    def __init__(self, arquivo):
        self.arquivo = list(open(arquivo))      # Abrindo arquivo como lista (cada linha eh uma lista)

    def qtdLinhasDadosFaltantes(self):
        self.lista_faltantes = []
        titulos = self.arquivo[0].split(";")    # titulos = var local do tipo lista, onde cada item eh uma coluna da linha 0
        
        # self.lista_faltantes[0] recebe titulos, mas sem as marcacoes de nova linha '\n'
        # essa linha eh desprezivel, mas se assim fizer, considerar que o indice 0 ja contera dados do arquivo .csv
        [self.lista_faltantes.append([titulos[i].replace('\n',''),0]) for i in range(0,len(titulos))]

        # Este loop conta o numero de informacoes faltantes em cada coluna.
        # O resultado sera uma lista de listas duplas (self.lista_faltantes)
        #   no formato [['Titulo 1', contador de faltantes 1], ['Titulo 2', contador de faltantes 2], ...]
        for i in range(1,len(self.arquivo)):
            linha = self.arquivo[i].split(";")
            for j in range(0,len(linha)):
                if linha[j] == "" or linha[j].lower() == "sem informações":
                    self.lista_faltantes[j][1] += 1
        
        # copiando a lista de faltantes para a variavel local "media"
        media = self.lista_faltantes[:]
        
        print("--- Media de Dados Faltantes por Coluna ---")
        # Descricao do loop abaixo:
        # - Em cada coluna (indice i) da variavel media, o valor do contador (indice 1) receberar o calculo da media da coluna
        # - A funcao round arredonda o resultado para 3 casas decimais
        # - Cada coluna sera impressa com seu respectivo valor de media
        for i in range(0,len(media)):
            media[i][1] = round(media[i][1] / len(self.arquivo[1:]),3)
            print(media[i])
        
        # Apesar do calculo da media, o desafio pede pra que a funcao retorno a quantidade de linhas faltantes por coluna.
        return self.lista_faltantes

    def nivelTax(self, inicio=1):
        # inico: item inicial a ser impresso ate o ultimo (default = 1)
        
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
        
        return True
    
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
            21- Especieque 
            22- Estado de conservacao
            23- Categoria de Ameaca
            24- Localidade
            25- Pais
            26- Estado/Provincia
            27- Municipio
            28- Status de Sensibilidade
            29- Latitude
            30- Longitude
            31- Outras informacoes da localidade
            32- Jurisdicao
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
    
    def checkLatLong(self):
        self.latLong = []       # Lista de listas: cada sublista esta no formato [lat,long]
<<<<<<< HEAD
        self.city = []          # Lista de cidades 
        self.indexNotOK = []
        [self.latLong.append([i.split(";")[29],i.split(";")[30]]) for i in self.arquivo[1:60]]
        [self.city.append(i.split(";")[27]) for i in self.arquivo[1:60]]

=======
        [self.latLong.append([i.split(";")[29],i.split(";")[30]]) for i in self.arquivo[1:]]
        
        
>>>>>>> bec38997170fcd30f54e09a7ab6da2228957d85d
        key = 'b3581bc610a644f896bd87fc2cd8e6ce'
        geocoder = OpenCageGeocode(key)
        
        for i in range(0,len(self.latLong)):
            results = geocoder.reverse_geocode(self.latLong[i][0], self.latLong[i][1])
            if  self.city[i].lower() != results[0]['components']['city'].lower():
                #self.notOK.append([["City from geocoder: "+results[0]['components']['city']],["City from csv-file: "+self.city[i]],["Index: "+str(i)]])
                self.indexNotOK.append(i)

<<<<<<< HEAD
        print("Indices dos dados conflitantes:",self.indexNotOK)        
=======
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
>>>>>>> bec38997170fcd30f54e09a7ab6da2228957d85d

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
#obj.qtdLinhasDadosFaltantes()                      #OK
#obj.nivelTax()
#obj.filtro_ocorrencias(1,"JBRJ")                   #OK
obj.checkLatLong()