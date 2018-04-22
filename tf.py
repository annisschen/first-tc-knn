from collections import Counter
import math


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

def tf(a,file): #a=string 是一个term, file是对应的这篇文章
    TF=0
    n=len(file[1])
    m=Counter()
    m=Counter(file[1])
    TF=m[a]/n
    return TF

def idf(a):
    IDF=0
    with open('idf.txt','r') as file:
        idf_list = file.readline()
        idf_list=idf_list.split()
        i=idf_list.index(a)+1
        IDF = float(idf_list[i])
    return IDF

def passage_tfidf(file):
    f_tfidf = {}
    f_tfidf['categlory']=file[0]
    a=[]
    a=list(set(file[1]))
    file_tfidf=Counter()
    for i in a:
        key = i
        tf_value = tf(key,file)
        idf_value = idf(key)
        tf_idf = tf_value*idf_value
        f_tfidf[key]=tf_idf
    return f_tfidf

def save_tfidf(bigbigfile,a):#a是保存的文件名，bigbigfile eg.train_file
    with open(a,'w') as output:
        for file in bigbigfile:
            f_tfidf = passage_tfidf(file)
            for key in f_tfidf:
                output.write(str(key)+' '+str(f_tfidf[key])+' ')
            output.write('\n')

def all_diction_tfidf(bigbigfile,a):
    all=[]
    for file in bigbigfile:
        f_tfidf = passage_tfidf(file)
        all.append(f_tfidf)

# save_tfidf(train_file,'train_file_tfidf.txt')
# save_tfidf(test_file,'test_file_tfidf.txt')