import math
from statistics import mean

def First100EvenSum(x):
    acc=0
    for x in range(0,101,2):
        acc = acc + x
        return acc

def First50OddSum(y):
    acc=1
    for y in range(0,51,2):
        acc = acc + y
        print(acc)

def First100Avg(z):
    total = 0
    length = 0
    for i in range (1,101,2):
        total += i
        length += 1
    print(total/length)




