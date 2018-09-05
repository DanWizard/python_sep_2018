for i in range(3001):
    if i % 2 != 0:
        print(i)
#prediction: will print all odds from 0 to 3001 excluding 3001

list = [3,5,1,2]
for i in range(list):
    print(i)
#prediction: will not work because list is a list not an integer

list = [3,5,1,2]
for i in range(len(list)):
    print(i)
#prediction: it will print all values less than 4
