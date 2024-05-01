import numpy as np

def findmin(x,y):
    if x > y : print("Y is the minimum number {}".format(y));
    else: print("X is the minimum number {}".format(x));
    return

def main():

    x = int(input(""))
    y = int(input(""))
    findmin(x,y)
    return

if __name__ == "__main__":
    main()