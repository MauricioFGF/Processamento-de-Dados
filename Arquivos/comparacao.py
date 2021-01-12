




def compararNomeDecrescente(value,value2):
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

def compararNomeCrescente(value,value2):
    a = value.getNomeCandidato()
    b = value2.getNomeCandidato()
    if a is b:
        return 0
    else:
        x = max(a,b)
        if x == a:
            return 1
        elif x == b:
            return -1

def compararBensCrescente(value,value2):
    a = value.getListaBens()
    b = value2.getListaBens()
    if a is b :
        return 0
    else:
        x = max(a,b)
        if x == a:
            return 1
        elif x == b:
            return -1


def compararBensDecrescente(value,value2):
    a = value.getListaBens()
    b = value2.getListaBens()
    if a is b :
        return 0
    else:
        x = min(a,b)
        if x == a:
            return -1
        elif x == b:
            return - 1

def compararNascimentoCrescente(value,value2):
    a = invert(value.getDataNascimento())
    b = invert(value2.getDataNascimento())
    if a is b :
        return 0
    elif a > b:
        return  1
    elif a < b:
        return -1


def invert(valor):
    valor = valor[6:] + valor[3:5] + valor[:2]
    return valor

