#!/bin/python3

import math
import os
import random
import re
import sys
# 413962293
# 12527392

# if mess=="Jan":
#         return 30*0*24*3600
#     elif mess=="Feb":
#         return 31*1*24*3600
#     elif mess=="Mar":
#         return 59*24*3600
#     elif mess=="Apr":
#         return 90*4*24*3600
#     elif mess=="May":
#         return 120*5*24*3600
#     elif mess=="Jun":
#         return 151*6*24*3600
#     elif mess=="Jul":
#         return 181*7*24*3600
#     elif mess=="Aug":
#         return 212*8*24*3600
#     elif mess=="Sep":
#         return 243*24*3600
#     elif mess=="Oct":
#         return 273*24*3600
#     elif mess=="Nov":
#         return 304*24*3600
#     elif mess=="Dec":
#         return 334*24*3600
#     else:return 0


def newpos(ccpp, fd, df, rrr):
    vueltas = (fd*df)-((fd-(ccpp*2))*(df-(ccpp*2)))
    xx = 0
    yy = 0
    return xx, yy
# Complete the matrixRotation function below.


def matrixRotation(matrix, r, mm, nn):
    retorno = [[aa*0 for aa in range(1, nn)] for a in range(1, mm)]
    capa = 1
    tr, ty = newpos(capa, mm, nn, r)
    return retorno


if __name__ == '__main__':
    mnr = input().rstrip().split()

    m = int(mnr[0])

    n = int(mnr[1])

    r = int(mnr[2])

    matrix = []

    for _ in range(m):
        matrix.append(list(map(int, input().rstrip().split())))

    matrixRotation(matrix, r, m, n)
