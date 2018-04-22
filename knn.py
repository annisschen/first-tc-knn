# import re
#
# import numpy
# from sklearn.neighbors import KNeighborsClassifier
#
# all_terms = []
#
# with open('all_term.txt','r') as file:
#     test=[]
#     test = file.readline()
#     test=test.strip().split()
#     all_terms=test
#
# def alltfidf(a):    #a=string is txt's name
#     test=[]
#     all=[]
#     with open(a) as file:
#         test=file.readlines()
#         for item in test:
#             item=item.strip().split()
#             del item[0]
#             all.append(item)
#     return all
#
# all_tfidf=list()
# all_tfidf.extend(alltfidf('train_file_tfidf.txt'))
# all_tfidf.extend(alltfidf('test_file_tfidf.txt'))
#
# # print(len(all_terms))
# tfidf = numpy.zeros((7674,17387))
# # print(all_tfidf[3556])
#
# for i in range(7674):
#     for m in range(len(all_terms)):
#         key=all_terms[m]
#         a=0
#         test=[]
#         test = all_tfidf[i][1:-1]
#         if key in test:
#             index_of_tfidf = test.index(key)
#             a=all_tfidf[i][index_of_tfidf+2]
#             # print(a)
#             tfidf[i][m]=float(a)
#             continue
# # p_arr = np.append(p_arr,p_)
#
# # with open("reslut.txt",'w') as file:
# #     for item in tfidf:
# #         for cont in item:
# #             file.write(str(cont)+' ')
# #         file.write('\n')
# # for i in range(len(tfidf)):
#     # tfidf[i]=numpy.append(tfidf[i],deal_whole_dataset(i))
#
# train_data = []             #【【term1,term2,……】【】【】【】】
# train_labels = []           #【label1,label2,……】
# regex = re.compile('\t+')
# with open("r8-train-stemmed.txt") as ifile:
#     for line in ifile:
#         line=line.strip()
#         tokens = regex.split(line)
#         train_data.append(tokens[1])
#         train_labels.append(tokens[0])
#
# # print(train_data)
# # print(train_labels)
# test_data = []
# test_labels = []
#
# #【【term1,term2,……】【term1,term2,……】【】【】】
# #【label1,label2,……】
#
# with open("r8-test-stemmed.txt") as ifile:
#     for line in ifile:
#         line = line.strip()
#         tokens = regex.split(line)
#         test_data.append(tokens[1])
#         test_labels.append(tokens[0])
#
# knn = KNeighborsClassifier()
# #定义一个knn分类器对象
# knn.fit(train_data, train_labels)
#
# test_predict = knn.predict(test_data)
#  #调用该对象的测试方法，主要接收一个参数：测试数据集
# probility=knn.predict_proba(test_data)
#  #计算各测试样本基于概率的预测
# neighborpoint=knn.kneighbors(test_data[-1],20,False)
# #计算与最后一个测试样本距离在最近的5个点，返回的是这些样本的序号组成的数组
# score=knn.score(test_data,test_labels,sample_weight=None)
# print ('Accuracy:'+str(score))