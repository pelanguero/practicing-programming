

def subs(ssss):
    sretorno = 0
    vretorno = 0
    a = 0
    vacales = ["A", "E", "I", "O", "U"]
    while a < len(ssss):
        if ssss[a] in vacales:
            vretorno = vretorno+len(ssss)-a
        else:
            sretorno = sretorno+len(ssss)-a

        a += 1

    return sretorno, vretorno


def minion_game(string):
    kkevin = 0
    sstuart = 0
    s, k = subs(string)
    sstuart = sstuart+s
    kkevin += k
    if kkevin > sstuart:
        print("Kevin "+str(kkevin))
    elif kkevin == sstuart:
        print("Draw")
    elif kkevin < sstuart:
        print("Stuart "+str(sstuart))


if __name__ == '__main__':
    fille = open("testhc7.txt", "r")
    s = fille.readline()
    minion_game(s)
    print((time.time() - start_time))
    fille.close()
