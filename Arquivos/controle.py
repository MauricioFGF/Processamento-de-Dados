import time
from candidatos import *
from bens import *
from lista import *
class Controle:
    def __init__(self):
        self.__lista = Lista()

    def getLista(self):
        return self.__lista

    def inserirCandidatos(self, value):
        arquivo = open(value,'r')
        for linhas in arquivo:
            linhas = linhas.replace('"','')
            linhas = linhas.strip()
            linhas = linhas.split(';')
            if 'DT_GERACAO' == linhas[0] :
                continue  
            m = Candidatos(linhas)
            self.getLista().inserirOrdenado(m)
        arquivo.close()
    
    
    def organizarBens(self,value):
        dicionario = {}
        arquivo = open(value,'r')
        for linhas in arquivo:
            linhas = linhas.replace('"','')
            linhas = linhas.strip()
            linhas = linhas.split(';')
            if 'DT_GERACAO' == linhas[0]:
                continue   
            g = Bens(linhas)
            if g.getIdDoCandidato() not in dicionario:
                dicionario[g.getIdDoCandidato()] = [[g.getCodigoTipoBem(), g.getDesrcricaoDetalhadaBem() ,g.getDescricaoTipoBem(), g.getValorBem()]]
            else:
                dicionario[g.getIdDoCandidato()] += [[g.getCodigoTipoBem(), g.getDesrcricaoDetalhadaBem() ,g.getDescricaoTipoBem(), g.getValorBem()]]
        arquivo.close()
        return dicionario
    
    def inserirBens(self, value):
        bens = self.organizarBens(value)
        for x in self.getLista():
            if x.getIdCandidato() in bens:
                for y in bens[x.getIdCandidato()]:
                    x.incluirBem(y)


    def candidatoPartido(self,value,value2,value3):
        lista = []
        for x in self.getLista():
            if x.getNomePartido()== value and x.valorTotalBens() >= value2 and x.getSituacaoCandidatura() == value3 : 
                lista.append([x.getNomeCandidato(), str(x.valorTotalBens())])
        return lista
            

    def candidatoUf(self,value,value2,value3):
        lista = []
        for x in self.getLista():
            if x.getSiglaUF()== value and x.valorTotalBens() >= value2 and x.getSituacaoCandidatura() == value3 : 
                lista.append([x.getNomeCandidato(), str(x.valorTotalBens())])
        return lista


    def candidatoMunicipio(self,value,value2,value3):
        lista = []
        for x in self.getLista():
            if x.getMunicipioNascimento()== value and x.valorTotalBens() >= value2 and x.getSituacaoCandidatura() == value3 : 
                lista.append([x.getNomeCandidato(), str(x.valorTotalBens())])
        return lista

    def candidatoCargo(self,value,value2,value3):
        lista = []
        for x in self.getLista():
            if x.getDescricaoCargo()== value and x.valorTotalBens() >= value2 and x.getSituacaoCandidatura() == value3 : 
                lista.append([x.getNomeCandidato(), str(x.valorTotalBens())])
        return lista

    def imprimirCandidatos(self,lista):
        nomes = ''
        for y in lista:
            nomes += y[0] + ', ' 
        print('~~~~Candidatos~~~~')    
        print(nomes[:-2])

    def media(self,lista):
        media = 0
        for y in lista:
            y[1] = float(y[1])
            media += y[1]
        media = media/len(lista)
        return media
    
    def mediaPartido(self,value):
        lista = []
        for x in self.getLista():
            if x.getNomePartido() == value : 
                lista.append([x.getNomeCandidato(), str(x.valorTotalBens())])
        media = self.media(lista)
        print(media)
    
    def mediaUF(self,value):
        lista = []
        for x in self.getLista():
            if x.getSiglaUF() == value : 
                lista.append([x.getNomeCandidato(), str(x.valorTotalBens())])
        media = self.media(lista)
        print(media)

    def mediaCargo(self,value):
        lista = []
        for x in self.getLista():
            if x.getDescricaoCargo() == value : 
                lista.append([x.getNomeCandidato(), str(x.valorTotalBens())])
        media = self.media(lista)
        print(media)

    def mediaOcupacao(self,value):
        lista = []
        for x in self.getLista():
            if x.getDescricaoOcupacao() == value : 
                lista.append([x.getNomeCandidato(), str(x.valorTotalBens())])
        media = self.media(lista)
        print(media)

    def mediaNascimento(self,value):
        lista = []
        for x in self.getLista():
            if x.getDataNascimento()[6:] == value : 
                lista.append([x.getNomeCandidato(), str(x.valorTotalBens())])
        media = self.media(lista)
        print(media)

    def removerCandidato(self):
        print( '   ---Menu de Remoção--- \n Remover por Partido Digite - 0 \n Remover por Estado de Eleição Digite - 1 \n Remover por Cargo Digite - 2 \n Remover por Ocupação - 3 \n Remover por Resultado Eleitoral - 4 \n Remover pelo Pós Pleito - 5' )  
        x = input('Digite o valor desejado aqui:')
        x = int(x)
        if 0 > x > 5:
            raise StopIteration
        else:
            if x == 0:
                valor = input('Digite o Nome ou Sigla do Partido:')
                for z in self.getLista():
                    if z.getNomePartido() ==  valor or z.getSiglaPartido() == valor: 
                        self.getLista().remover(z) 
            elif x == 1:
                valor = input('Digite a Sigla do Estado:')
                for z in self.getLista():
                    if z.getSiglaUF() ==  valor: 
                        self.getLista().remover(z)
            elif x == 2:
                valor = input('Digite o Cargo:')
                for z in self.getLista():
                    if z.getDescricaoCargo() ==  valor: 
                        self.getLista().remover(z)
            elif x == 3:
                valor = input('Digite a Ocupação:')
                for z in self.getLista():
                    if z.getDescricaoOcupacao() ==  valor: 
                        self.getLista().remover(z)
            elif x == 4:
                valor = input('Digite a Situação da Candidatura:')
                for z in self.getLista():
                    if z.getSituacaoCandidatura() ==  valor: 
                        self.getLista().remover(z)
            elif x == 5:
                valor = input('Digite a Situação Pós Pleito:')
                for z in self.getLista():
                    if z.getSituacaoPosPleito() ==  valor: 
                        self.getLista().remover(z)



        
if __name__ == '__main__':   
    m = Controle()
    m.inserirCandidatos('candidatos.txt')
    m.inserirBens('Bens.txt')
    x = time.time()
    m.removerCandidato()
    e = time.time()
    print(e - x)


 
