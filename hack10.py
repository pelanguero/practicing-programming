class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return


def print_from_stream(n, stream=EvenStream()):
    for s in range(n):
        temp = fileout.readline()
        temp2 = stream.get_next()
        print(temp2, end=" ")
        print(temp, end=" ")
        print(int(temp) == temp2)
    stream = None


fille = open("test10hack.txt", "r")
fileout = open("test10hackout.txt", "r")
queries = int(fille.readline())
for _ in range(queries):
    stream_name, n = fille.readline().split()
    n = int(n)
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())


fille.close()
fileout.close()
