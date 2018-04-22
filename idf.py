import math
from collections import Counter


def occur(a):
    m = Counter()
    for i in a:
        b=i[1]
        b=list(set(b))
        m+=Counter(b)
    return m

test_file = open("r8-test-stemmed.txt").readlines()
train_file = open("r8-train-stemmed.txt").readlines()

for i in range(len(test_file)):
    test_file[i] = test_file[i].strip()
    test_file[i] = test_file[i].split()
    test = []
    test.append(test_file[i][0])
    del test_file[i][0]
    test.append(test_file[i])
    test_file[i] = test
for i in range(len(train_file)):
    train_file[i] = train_file[i].strip()
    train_file[i] = train_file[i].split()
    test = []
    test.append(train_file[i][0])
    del train_file[i][0]
    test.append(train_file[i])
    train_file[i] = test

m=occur(train_file)
n=occur(test_file)
occurance = Counter()
occurance=m+n
number_of_dc = len(train_file)+len(test_file)
# print(number_of_dc)

def idf_save(occurance,number_of_dc):
    with open('idf.txt','w') as file:
        for key in occurance:
            a=math.log(math.pi,(number_of_dc/occurance[key]))
            file.write(str(key)+" "+str(a)+' ')

# idf_save(occurance,number_of_dc)

def all_term(bigbigfile):
    test = []
    for item in bigbigfile:
        test.extend(item[1])
    all=list(set(test))
    return all

all1 = all_term(train_file)
all2 = all_term(test_file)
all1.extend(all2)
all=list(set(all1))
with open('all_term.txt','w') as file:
    for item in all:
        file.write(str(item)+' ')