def countdown(x):
    z = range(x,0,-1)
    for i in z:
        print(i)

countdown(9)

def printRet(x):
    print(x[0])
    return x[1]
print(printRet([1,2]))

def firstLength(x):
    print(len(x) + x[0])
firstLength([1,2,3,4,5])

def greaterThan(x):
    y = []
    for i in range(len(x)):
        if len(x) < 1:
            return false

        elif x[i] > x[1]:
            y.append(x[i])
    print(y)
    print('y length is',len(y))

greaterThan([1,2,3,4,5])

def lengthAndvalue(size,value):
    y = []
    for i in range(size):
        y.append(value)
    print(y)

lengthAndvalue(5,6)

        
        



