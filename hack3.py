from itertools import permutations
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    tempx = [h for h in range(0, x+1, 1)]
    print(tempx)
    tempy = [hq for hq in range(0, y+1, 1)]
    print(tempy)
    tempz = [hw for hw in range(0, z+1, 1)]
    print(tempz)
    tempp = [[sx, sy, sz] for sx in tempx for sy in tempy for sz in tempz]
    # o tempp [[sx, sy, sz] for sx in range(0, x+1, 1) for sy in range(0, y+1, 1) for sz in range(0, z+1, 1)]
    print(tempp)
    retorno = [l for l in tempp if sum(l) != n]
    print(retorno)
