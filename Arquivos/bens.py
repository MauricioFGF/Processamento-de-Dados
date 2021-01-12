
import textwrap
class Bens:
    def __init__(self, value):
        self.__codigoTipoBem = value[13]
        self.__descricaoTipoBem = value[14]
        self.__desrcricaoDetalhadaBem = value[15]
        self.__valorBem = float(value[16].replace(',','.'))
        self.__idCandidato = value[11]


    def getCodigoTipoBem(self):
        return self.__codigoTipoBem
    def setCodigoTipoBem(self,value):
        self.__codigoTipoBem = value 

    def getDescricaoTipoBem(self):
        return self.__descricaoTipoBem
    def setDescricaoTipoBem(self,value):
        self.__descricaoTipoBem = value

    def getDesrcricaoDetalhadaBem(self):
        return self.__desrcricaoDetalhadaBem
    def setDesrcricaoDetalhadaBem(self,value):
        self.__desrcricaoDetalhadaBem = value

    def getValorBem(self):
        return self.__valorBem
    def setValorBem(self,value):
        self.__valorBem = value
    
    def getIdDoCandidato(self):
        return self.__idCandidato
    def setIdDoCandidato(self,value):
        self.__idCandidato = value

    def __str__(self):
        tipoBem = str (self.getCodigoTipoBem())
        dTipoBem = str(self.getDescricaoTipoBem())
        ddBem =  str(self.getDesrcricaoDetalhadaBem())
        ddBem2 = textwrap.fill(ddBem, width = 80)
        valorBem =  str(self.getValorBem()) 
        return 'Código do tipo de bem: ' + tipoBem +  '  --- Descrição do Tipo bem: '+ dTipoBem + '  --- Valor do Bem: '+ valorBem + '\n' +'Descrição: ' + ddBem2

    def __repr__(self):
        tipoBem = str (self.getCodigoTipoBem())
        dTipoBem = str(self.getDescricaoTipoBem())
        ddBem =  str(self.getDesrcricaoDetalhadaBem())
        ddBem2 = textwrap.fill(ddBem, width = 80)
        valorBem =  str(self.getValorBem()) 
        return 'Bens('+ ' ' + tipoBem + ' '+ dTipoBem + ' '+ ddBem2 +' '+  valorBem + ')'

    def compararValor(self,value,value2):
        a = value.getValorBem()
        b = value2.getValorBem()
        if a == b:
            if self.compararDescricao(value,value2):
                print('São iguais')
                return a
            else:
                return self.compararCodigo(value,value2)
        else:
            if a > b:
                return a
            elif b > a:
                return b

    def compararCodigo(self,value,value2):
        a = value.getCodigoTipoBem()
        b = value2.getCodigoTipoBem()
        if a == b:
            return self.compararDescricao(value,value2)
        else:
            if a > b:
                return a
            elif b > a:
                return b

    def compararDescricao(self,value,value2):
        a = value.getDesrcricaoDetalhadaBem()
        b = value2.getDesrcricaoDetalhadaBem()
        if a == b:
            return True
        else:
            if a > b:
                return a
            elif b > a:
                return b

        
