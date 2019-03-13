import sys

if __name__ == "__main__":
    a = int(sys.argv[1])
    M = int(sys.argv[2])

    x = []
    buf = input("number1 > ")
    x.append(int(buf))
    buf = input("number2 > ")
    x.append(int(buf))

    c = (x[1] - a * x[0]) % M

    print("c = {}".format(c))
