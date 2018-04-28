from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report


with open('r8-train-stemmed.txt')as file:
    train_file = file.readlines()
    for i in range(5485):
        train_file[i]=train_file[i].strip().split('\t')
        # train_file[i][1]=train_file[i][1].split()

with open('r8-test-stemmed.txt')as file:
    test_file = file.readlines()
    for i in range(5485,7674):
        train_file.append(test_file[i-5485].strip().split('\t'))
        # train_file[i][1]=train_file[i][1].split()
print(train_file[0])
all_file = train_file
corpus = []
for i in range(7674):
    corpus.append(all_file[i][1])
print(corpus)

vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频
transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值
tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵
word=vectorizer.get_feature_names()#获取词袋模型中的所有词语
weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重
weight = np.array(weight)
print(np.shape(weight))

train_data = []
test_data=[]

train_data = weight[0:5485]
test_data = weight[5485:7674]
train_lables=[]
test_lables=[]
for i in range(5485):
    train_lables.append(train_file[i][0])
for i in range(5485,7674):
    test_lables.append(train_file[i][0])


print(train_lables)
categlory = ['acq', 'crude', 'earn', 'grain', 'interest', 'money-fx', 'ship','trade']

knn = KNeighborsClassifier()

knn.fit(train_data,train_lables)
predict = knn.predict(test_data)

print(classification_report(test_lables, predict,target_names=categlory))