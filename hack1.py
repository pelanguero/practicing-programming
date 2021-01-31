def imprimirtop(strrr, obtj):
    strr = sorted(strrr)
    top1 = ["", -1]
    top2 = ["", -1]
    top3 = ["", -1]
    top4 = ["", -1]
    cont = -1
    while cont < len(strr)-1:
        cont = cont+1
        if cont == 0:
            top1[0] = strr[cont]
            top1[1] = obtj[strr[cont]]
            print(strr[cont]+str(1))
            continue
        if top1[1] < obtj[strr[cont]]:
            top3[0] = top2[0]
            top3[1] = top2[1]
            top2[0] = top1[0]
            top2[1] = top1[1]
            top1[0] = strr[cont]
            top1[1] = obtj[strr[cont]]
            print(strr[cont]+str(1))
            continue
        if top2[1] < obtj[strr[cont]]:
            top3[0] = top2[0]
            top3[1] = top2[1]
            top2[0] = strr[cont]
            top2[1] = obtj[strr[cont]]
            print(strr[cont]+str(2))
            continue
        if top3[1] < obtj[strr[cont]]:
            top4[0] = top3[0]
            top4[1] = top3[1]
            top3[0] = strr[cont]
            top3[1] = obtj[strr[cont]]
            print(strr[cont]+str(3))
            continue
    print(top1[0]+" "+str(top1[1]))
    print(top2[0]+" "+str(top2[1]))
    print(top3[0]+" "+str(top3[1]))
    print(top4[0]+" "+str(top4[1]))


arch = open("inputt.txt", "r")
s = arch.readline()
objeto = {"test": "pro"}
ss = ""
for chhar in s:
    if chhar not in ss:
        ss = ss+chhar
        objeto[chhar] = 0
    objeto[chhar] = objeto[chhar]+1
imprimirtop(ss, objeto)

arch.close()
