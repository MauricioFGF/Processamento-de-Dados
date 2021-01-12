from bens import *
class Candidatos:
    def __init__(self, value):
        self.__anoEleicao = value[2]
        self.__siglaUF = value[10]
        self.__codigoCargo = value[13]
        self.__descricaoCargo = value[14]
        self.__nomeCandidato = value[17]
        self.__idCandidato = value[15]
        self.__numeroUrna = value[16]
        self.__cpf = value[21]
        self.__nomeUrna = value[18]
        self.__numeroPartido = value[27]
        self.__nomePartido = value[29]
        self.__siglaPartido = value[28]
        self.__codigOcupacao = value[49]
        self.__descricaoOcupacao = value[50]
        self.__dataNascimento = value[38]
        self.__genero = value[42]
        self.__grauInstrucao = value[44]
        self.__estadoCivil = value[46]
        self.__ufNascimento = value[35]
        self.__municipioNascimento = value[37]
        self.__situacaoPosPleito = value[53]
        self.__situacaoCandidatura = value[25]
        self.__listaBens = []
   


    def getAnoEleicao(self):
        return self.__anoEleicao
    def setAnoEleicao(self, value):
        self.__anoEleicao = value

    def getSiglaUF(self):
        return self.__siglaUF
    def setSiglaUF(self, value):
        self.__siglaUF = value
    
    def getCodigoCargo(self):
        return self.__codigoCargo
    def setCodigoCargo(self, value):
        self.__codigoCargo = value

    def getDescricaoCargo(self):
        return self.__descricaoCargo
    def setDescricaoCargo(self, value):
        self.__descricaoCargo = value

    def getNomeCandidato(self):
        return self.__nomeCandidato
    def setNomeCandidato(self, value):
        self.__nomeCandidato = value
    
    def getIdCandidato(self):
        return self.__idCandidato
    def setIdCandidato(self, value):
        self.__idCandidato = value
    
    def getNumeroUrna(self):
        return self.__numeroUrna
    def setNumeroUrna(self, value):
        self.__numeroUrna = value
    
    def getCpf(self):
        return self.__cpf
    def setCpf(self, value):
        self.__cpf = value
    
    def getNomeUrna(self):
        return self.__nomeUrna
    def setnomeUrna(self, value):
        self.__nomeUrna = value

    def getNumeroPartido(self):
        return self.__numeroPartido
    def setNumeroPartido(self, value):
        self.__numeroPartido = value

    def getNomePartido(self):
        return self.__nomePartido
    def setNomePartido(self, value):
        self.__nomePartido = value
    
    def getSiglaPartido(self):
        return self.__siglaPartido
    def setSiglaPartido(self, value):
        self.__siglaPartido = value

    def getCodigOcupacao(self):
        return self.__codigOcupacao
    def setCodigOcupacao(self, value):
        self.__codigOcupacao = value

    def getDescricaoOcupacao(self):
        return self.__descricaoOcupacao
    def setDescricaoOcupacao(self, value):
        self.__descricaoOcupacao = value

    def getDataNascimento(self):
        return self.__dataNascimento
    def setDataNascimento(self, value):
        self.__dataNascimento = value

    def getGenero(self):
        return self.__genero
    def setGenero(self, value):
        self.__genero = value
    
    def getGrauInstrucao(self):
        return self.__grauInstrucao
    def setGrauInstrucao(self, value):
        self.__grauInstrucao = value

    def getEstadoCivil(self):
        return self.__estadoCivil
    def setEstadoCivil(self, value):
        self.__estadoCivil = value
    
    def getUfNascimento(self):
        return self.__ufNascimento
    def setUfNascimento(self, value):
        self.__ufNascimento = value

    def getMunicipioNascimento(self):
        return self.__municipioNascimento
    def setMunicipioNascimento(self, value):
        self.__municipioNascimento = value

    def getSituacaoPosPleito(self):
        return self.__situacaoPosPleito
    def setSituacaoPosPleito(self, value):
        self.__situacaoPosPleito = value

    def getSituacaoCandidatura(self):
        return self.__situacaoCandidatura
    def setSituacaoCandidatura(self, value):
        self.__situacaoCandidatura = value

    def getListaBens(self):
        return self.__listaBens
    def setListaBens(self, value):
        self.__listaBens.append(value)

    def incluirBem(self,value):
        self.setListaBens(value)

    def valorTotalBens(self):
        valor = 0
        for x in self.getListaBens():
            valor += x[3]
        return valor
    
    def imprimirBens(self):
        dicionario = {}
        for x in self.getListaBens():
            if int(x[0]) not in dicionario:
                dicionario[int(x[0])] = x[2:]
            else:
                dicionario[int(x[0])] += x[3:]
        return dicionario

    def impressao(self):
        valor =''
        n =''
        for x in self.imprimirBens():
            nome = self.imprimirBens()[x][0]
            for z in self.imprimirBens()[x][1:]:
                z = str(z)
                valor+= z
            n +='Nome do Bem: '+  nome +'  |  Valor do Bem: '+ str(valor) + '\n'
            valor = ''
        return (n)

    def imprimirBemDetalhado(self):
        nome = ''
        for x in self.getListaBens():
            nome += (x[1]) + ' '+ 'R$' + ' ' + str(x[3]) + '\n'
        return nome[:-1]
        
           
    def __str__(self):
        nomeDaUrna = str (self.getNomeUrna())
        numeroDaUrna = str(self.getNumeroUrna())
        siglaDoPartido =  str(self.getSiglaPartido()) 
        cargoDisputado =  str(self.getDescricaoCargo()) + '('+ str(self.getSiglaUF())+')'
        municipioDeNascimento = str(self.getMunicipioNascimento()) + '('+ str(self.getSiglaUF())+')'
        return ( ' Nome da urna: ' + nomeDaUrna + '   Número da Urna: '+ numeroDaUrna + '   Sigla do Partido: ' + siglaDoPartido + '\n' + 'Cargo Disputado: '+ cargoDisputado + '   Município de Nascimento: '+ municipioDeNascimento + '\n' +'---Resumo dos Bens---'+ '\n' +'Valor Total de Bens: R$ '+ str(self.valorTotalBens()) + '\n' +  str(self.impressao()))
       

    def __repr__ (self):
        nomeDaUrna = str (self.getNomeUrna())
        numeroDaUrna = str(self.getNumeroUrna())
        siglaDoPartido =  str(self.getSiglaPartido()) 
        cargoDisputado =  str(self.getDescricaoCargo()) + '('+ str(self.getSiglaUF())+')'
        municipioDeNascimento = str(self.getMunicipioNascimento()) + '('+ str(self.getSiglaUF())+')'
        return 'Candidatos('+ nomeDaUrna + ', ' + numeroDaUrna + ', ' +  siglaDoPartido + ', ' + cargoDisputado + ', ' + municipioDeNascimento +  ', ' + str(self.valorTotalBens()) + ', ' +str( self.impressao()) + ')' 

    def __comparacao(self,value):
        if  self.getNomeCandidato == value.getNomeCandidato() and self.getCpf == value.getCpf():
            return True
        else:
            return False


"""if __name__ == '__main__':"""
