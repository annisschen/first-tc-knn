import numpy
import re
from collections import Counter


def find_max_n(list1,n):
    test = list1
    a=[0]*n
    for i in range(n):
        temp = test.index(max(test))
        a[i]=temp
        test[temp] = 0
    return a

similarity = numpy.zeros((219,548))
with open('similarity5.txt','r')as file:
    test=file.readlines()
    # print(test[0])
    for i in range(len(test)):
        test[i]=test[i].strip()
        test[i]=test[i][1:-2]
        # print(test[0])
        test[i]=test[i].split(',')
        similarity[i] = test[i]
        # print(test[0])
# print(type(similarity[0][1]))

#获得训练集的标签
lable_indexs = []
with open('a.txt')as file:
    temp_string=file.readline().strip()
    temp_string=temp_string[1:-2]
    # print(temp_string)
    lable_indexs=re.split('\,\s',temp_string)

train_lables = []
# print(lable_indexs)
with open("r8-train-stemmed.txt",'r')as file:
    test = file.readlines()

    for a in lable_indexs:
        train_dc = test[int(a)].strip()
        train_dc = train_dc.split('\t')
        train_dc_lable = train_dc[0]
        # print(train_dc_lable)
        train_lables.append(train_dc_lable)

# print(len(train_lables))

#获得训练集

lable_indexs = range(1095,1314)

test_lables = []
with open("r8-test-stemmed.txt",'r')as file:
    test = file.readlines()
    for a in lable_indexs:
        test_dc = test[int(a)].strip()
        test_dc = test_dc.split('\t')
        test_dc_lable = test_dc[0]
        test_lables.append(test_dc_lable)
# print(len(test_lables))



a=[]

for i in range(len(similarity)):
    n=25
    nmax = find_max_n(list(similarity[i]),n)
    for j in range(n):
        nmax[j]=train_lables[nmax[j]]
    a.append(nmax)
# print(a)
predict_result = []
for i in range(len(a)):
    temp = Counter(a[i])
    predict_result.append(temp.most_common(1)[0][0])

# print(test_lables)
# print(predict_result)

number_of_predict = len(predict_result)
categlory = ['acq','crude','earn','grain','interest','money-fx','ship','trade']
confusion_matrix = numpy.zeros((8,8))

for i in range(number_of_predict):
    x=categlory.index(predict_result[i])
    y=categlory.index(test_lables[i])
    confusion_matrix[x][y]+=1

# print(confusion_matrix)
# # print(sum(sum(confusion_matrix)))
# #
# with open('confusion_matrix','w')as file:
#     file.write(str(confusion_matrix))

accuracy = []
for i in range(8):
    print("The accuracy of "+categlory[i])
    if confusion_matrix[i][i]!=0:
        temp = confusion_matrix[i][i]/sum(confusion_matrix[i])
    else:
        temp='data deficiencies'
    print(temp)
    accuracy.append(temp)




recall = []
for i in range(8):
    print("The recall of "+categlory[i])
    if confusion_matrix[i][i]!=0:
        temp = confusion_matrix[i][i]/sum(confusion_matrix[:,i])
    else:
        temp='data deficiencies'
    print(temp)
    recall.append(temp)



print(accuracy)
print(recall)

with open('final_result.txt','w')as file:
    file.write(str(accuracy))
    file.write('\n')
    file.write(str(recall))