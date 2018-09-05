def makeBig(x):
    for i in range(len(x)):
        if x[i] < 0:
            x[i] = 'big'
    print(x)

makeBig([1,-2,1,1])
        
def countPos(x):
    count = 0
    for i in range(len(x)):
        if x[i] > 0:
            count += 1
    x.pop(-1)
    x.append(count)
    print(x)

countPos([1,1,1,1,1,2])

def sumTotal(x):
    print(sum(x))

sumTotal([1,2,3,4])
            
def Average(x):
    print(sum(x)/len(x))

Average([1,2,3,4,5])

def listLength(x):
    print(len(x))

listLength([1,2,3,4,5,6])

def listMin(x):
     print(min(x))

listMin([1,2,3,4,5,6])

def listMax(x):
    print(max(x))

listMax([1,2,3,4,5])

def ultAnalyze(x):
    anylyze = dict(max = max(x), min = min(x),avg = sum(x)/len(x), sum = sum(x))

    print(anylyze)
ultAnalyze([1,2,3,4,5])

def reverseList(x):
    x.reverse()
    return x

print(reverseList([1,2,3,4,5]))
