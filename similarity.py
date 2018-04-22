
import numpy
import math
import random

idf = numpy.zeros((7674,17387))
with open('reslut.txt','r') as file:
    test=[]
    test=file.readlines()
    for i in range(7674):
        test[i]=test[i].strip().split()
        idf[i]=numpy.array(test[i])

print(1)
similarity = numpy.zeros((219,548))

# print(numpy.shape(idf))
def random_without_same(mi, ma, num):
    temp = []
    temp = list(range(mi, ma))
    random.shuffle(temp)
    return temp[0:num]
a=random_without_same(0,5485,548)
with open('a.txt','w') as file:
    file.write(str(a))
print(2)

for i in range(6580,6799):
    target =idf[i]
    test = numpy.zeros(548)
    for j,item in enumerate(a):   #operator idf[j]
        operator = idf[item]
        fenzi=0
        for m in range(17387):
            if target[m]==0 or operator[m]==0:
                continue
            else:
                fenzi += target[m]*operator[m]
        fenmu = math.sqrt((sum(target**2))*sum(operator**2))
        # print(a)
        test[j]=fenzi/fenmu
    similarity[i-6580]=test
    print(i)

print(3)
with open('similarity5.txt','w') as file:
    for i in range(219):
        file.write(str(list(similarity[i])))
        file.write('\n')