import math
import os
import random
import re
import sys


def mesasec(mess):
    if mess == "Jan":
        return 30*0*24*3600
    elif mess == "Feb":
        return 30*1*24*3600
    elif mess == "Mar":
        return 30*2*24*3600
    elif mess == "Apr":
        return 30*3*24*3600
    elif mess == "May":
        return 30*4*24*3600
    elif mess == "Jun":
        return 30*5*24*3600
    elif mess == "Jul":
        return 30*6*24*3600
    elif mess == "Aug":
        return 30*7*24*3600
    elif mess == "Sep":
        return 30*8*24*3600
    elif mess == "Oct":
        return 30*9*24*3600
    elif mess == "Nov":
        return 30*10*24*3600
    elif mess == "Dec":
        return 30*11*24*3600
    else:
        return 0
# Complete the time_delta function below.


def time_delta(t1, t2):
    art1 = str.split(t1, " ")
    art2 = str.split(t2, " ")
    anho = 365*24*3600
    hora = 3600
    minuto = 60
    anho1 = int(art1[3])*anho+int(str.split(art1[4], ":")[0])*hora+int(str.split(art1[4], ":")
                                                                       [1])*minuto+int(str.split(art1[4], ":")[2])+int(art1[1])*3600*24+mesasec(art1[2])
    anho2 = int(art2[3])*anho+int(str.split(art2[4], ":")[0])*hora+int(str.split(art2[4], ":")
                                                                       [1])*minuto+int(str.split(art2[4], ":")[2])+int(art2[1])*3600*24+mesasec(art2[2])
    if art1[5][0] == "+":
        anho1 = anho1-int(art1[5][1:3])*3600-int(art1[5][3:])*60
    else:
        anho1 = anho1+int(art1[5][1:3])*3600+int(art1[5][3:])*60

    if art2[5][0] == "+":
        anho2 = anho2-int(art2[5][1:3])*3600-int(art2[5][3:])*60
    else:
        anho2 = anho2+int(art2[5][1:3])*3600+int(art2[5][3:])*60
    return abs(anho1-anho2)


if __name__ == '__main__':
    test = open("testoupt.txt", "r")
    filee = open("testinpt.txt", "r")
    t = int(filee.readline())
    cont = 0
    for t_itr in range(t):
        t1 = filee.readline()

        t2 = filee.readline()

        delta = time_delta(t1, t2)
        tempS = test.readline()
        if delta == int(tempS):
            print("ACIERTO")
            cont = cont+1
        print(str(delta))
        print(tempS, end="")
        print("--")
    print(str(cont)+" Aciertos")
    filee.close()
    test.close()
