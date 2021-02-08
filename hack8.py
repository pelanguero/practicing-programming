def merge_the_tools(string, k):
    # your code goes here
    a = 0
    sabe = []
    while a < len(string):
        if string[a] in sabe:
            a = a
        else:
            print(string[a], end="")
            sabe.append(string[a])
        if ((a+1) % k) == 0:
            print("")
            sabe.clear()
        a += 1


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
