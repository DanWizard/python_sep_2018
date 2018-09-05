def a():
    return 5
print(a())

#prediction: will return the value 5 for the function

def a():
    return 5
print(a()+a())

#prediction: will print 10 in console

def a():
    return 5
    return 10
print(a())

#prediction: it will print the value for the first return so in this case 5

def a():
    return 5
    print(10)
print(a())

#prediction: will stop the function after as soon as return is used. so all that will be returned is 5.

def a():
    print(5)
x = a()
print(x)

#prediction: the function will print 5 and then it will print none because when calling the function it will print 5 but the function has no return value

def a(b,c):
    print(b+c)
print(a(1,2) + a(2,3))

#prediction:it will print an error because you never return a value in the function

def a(b,c):
    return str(b)+str(c)
print(a(2,5))

#prediction: will return 25 by turning all types into strings then adding together

def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())

#prediction: will print 100 and return 10

def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))

#prediction:will print 7 then 14 then 21

def a(b,c):
    return b+c
    return 10
print(a(3,5))

#prediction:will return 8 

b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)

#prediction:500, 500, 300, 500

b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)

#prediction:500, 500, 300, 300

def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()

#prediction:1,3,2

def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)

#prediction:1 3 5 10
