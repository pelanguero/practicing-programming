import time
start_time = time.time()


def subs(ssss, tam):
    sretorno = 0
    vretorno = 0
    a = 0
    vacales = ["A", "E", "I", "O", "U"]

    while a+tam-1 < len(ssss):
        if ssss[a] in vacales:
            vretorno = vretorno+1
        else:
            sretorno = sretorno+1

        a += 1

    return sretorno, vretorno


def minion_game(string):
    kkevin = 0
    sstuart = 0
    ds = 1
    while ds <= len(string):
        s, k = subs(string, ds)
        sstuart = sstuart+s
        kkevin += k
        ds += 1
    if kkevin > sstuart:
        print("Kevin "+str(kkevin))
    elif kkevin == sstuart:
        print("Draw")
    elif kkevin < sstuart:
        print("Stuart "+str(sstuart))

    # your code goes here


if __name__ == '__main__':
    fille = open("testhc7.txt", "r")
    s = fille.readline()
    minion_game(s)
    print((time.time() - start_time))
    fille.close()
