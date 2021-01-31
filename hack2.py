import os
import sys

#
# Complete the timeConversion function below.
#


def timeConversion(s):
    #
    # Write your code here.
    #
    retorno = ""
    hora = int(s[0:2])
    print(hora)
    minuto = s[3:5]
    segundo = s[6:8]
    if hora == 12 and "A" == s[8]:
        hora = 0
        retorno = str(hora)*2+":"
    elif "A" == s[8]:
        if hora < 10:
            retorno = "0"+str(hora)+":"
        else:
            retorno = str(hora)+":"

    if "P" == s[8] and hora != 12:
        hora = hora+12
        retorno = str(hora)+":"
    else:
        retorno = str(hora)+":"
    retorno = retorno+minuto+":"+segundo
    return retorno


if __name__ == '__main__':
    # f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    print(result)
