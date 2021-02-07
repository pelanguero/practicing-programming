def subs(ssss, tam, vocall):
    retorno = []
    a = 0
    vacales = ["A", "E", "I", "O", "U"]
    if vocall:
        while a+tam-1 < len(ssss):
            if ssss[a] in vacales:
                retorno.append(ssss[a:a+tam])
            a += 1
    else:
        while a+tam-1 < len(ssss):
            if ssss[a] in vacales:
                a = a-1
                a += 1
            else:
                retorno.append(ssss[a:a+tam])

            a += 1

    return retorno


def puntaje(arrey):
    retturn = 0
    temp = []
    for fg in arrey:
        if fg not in temp:
            temp.append(fg)
            da = arrey.count(fg)
            retturn = retturn+da

    return retturn


def kevin(ss):
    rretorno = 0
    ds = 1
    while ds <= len(ss):
        rretorno += puntaje(subs(ss, ds, True))
        ds += 1
    return rretorno


def stuart(sss):
    rretorno = 0
    ds = 1
    while ds <= len(sss):
        rretorno += puntaje(subs(sss, ds, False))
        ds += 1
    return rretorno


def minion_game(string):
    kkevin = kevin(string)
    sstuart = stuart(string)
    if kkevin > sstuart:
        print("Kevin "+str(kkevin))
    elif kkevin == sstuart:
        print("Draw")
    elif kkevin < sstuart:
        print("Stuart "+str(sstuart))

    # your code goes here


if __name__ == '__main__':
    s = input()
    minion_game(s)
