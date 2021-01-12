class No:

    def __init__(self, anterior=None, item=None, proximo=None):
        self.anterior = anterior
        self.item = item
        self.proximo = proximo
    
    def __str__(self):
      return str(self.item)

class Lista:
    def __init__(self):
        self.primeiro = self.ultimo = No()
        self.tamanho = 0
        self.contIter = 0

    def vazia(self):
        return self.primeiro == self.ultimo
      
    def inserir(self, item):
        self.ultimo.proximo = No(self.ultimo, item, None)
        self.ultimo = self.ultimo.proximo
        self.tamanho += 1


    def inserirOrdenado(self, item):
        if self.vazia():
            self.inserir(item)
            return
        anterior = self.primeiro
        atual = self.primeiro.proximo
        while not atual is None and self.comparar(atual.item , item) == - 1:
            anterior = atual
            atual = anterior.proximo
        anterior.proximo = No(anterior, item, atual)
        self.tamanho += 1
        if atual is None:
            self.ultimo = anterior.proximo

    

    
    def remover(self, item):
        noAtual = self.primeiro
        while noAtual is not None:
            if noAtual.item == item:
                if noAtual.anterior is None:
                    self.primeiro = noAtual.proximo
                    noAtual.proximo.anterior = None
                else:
                    noAtual.anterior.proximo = noAtual.proximo
                    noAtual.proximo.anterior = noAtual.anterior
            noAtual = noAtual.proximo
        self.tamanho -=1 

    def comparar(self,value,value2):
        a = value.getNomeCandidato()
        b = value2.getNomeCandidato()
        if a is b:
            return 0
        else:
            x = min(a,b)
            if x == a:
                return -1
            elif x == b:
                return 1

    def __str__(self):
        texto = ''
        anterior = self.primeiro
        atual = self.primeiro.proximo
        while not atual is None:
            if atual.proximo != None:
                texto += str(atual.item)
                texto += '\n'*2
            else:
                texto += str(atual.item)
            anterior = atual
            atual = anterior.proximo
        texto += ''
        return texto
 

    def busca(self, item):
        if self.vazia():
            return None
        aux = self.primeiro.proximo
        while aux.proximo != None:
            if aux.item.getIdCandidato() == item:
                return aux
            aux = aux.proximo

    def __getitem__(self, indice):
        if indice >= self.tamanho:
            raise IndexError("Indice Inexistente")
        no = self.primeiro.proximo
        for contAux in range(indice):
            no = no.proximo
        return no.item

    def __iter__(self):
        return self

    def __next__(self):
        if self.contIter == 0:
            self.raiz = self.primeiro
        if self.tamanho > self.contIter:
            self.raiz = self.raiz.proximo
            self.contIter += 1
            return self.raiz.item
        else:
            del self.raiz
            self.contIter = 0
            raise StopIteration 



'''if __name__ == '__main__':'''
 
    