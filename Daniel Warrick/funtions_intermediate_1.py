#def beCheerful():
 #   print("be cheerful"*98)

#beCheerful()
import random

def randmInt(max = 0, min = 0):

    if max == 0 and min == 0 :
        print(int(random.random()*100))

    if type(max) == int or type(max) == float:
        difference= max - min
        print(int(random.random()*(max-min))+min)

randmInt( max =10, min=5)
