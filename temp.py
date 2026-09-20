#导入数据集预处理、特征工程和模型训练所需的库
from sklearn import model_selection
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import decomposition, ensemble
from sklearn.model_selection import KFold
from sklearn.naive_bayes import MultinomialNB
import re
import pandas
import numpy, textblob, string
import os


def train_model(classifier, feature_vector_train, label, feature_vector_valid, is_neural_net=False):
    # fit the training dataset on the classifier
    classifier.fit(feature_vector_train, label)
 
    # predict the labels on validation dataset
    predictions = classifier.predict(feature_vector_valid)
 
    if is_neural_net:
        predictions = predictions.argmax(axis=-1)
 
    return metrics.accuracy_score(predictions, valid_y)

def TfIdf(trainDF,train_x,test_x):
    tfidf_vect = TfidfVectorizer(analyzer='word', token_pattern=r'\w{1,}', max_features=5000)
    tfidf_vect.fit(trainDF['text'])
    xtrain_tfidf =  tfidf_vect.transform(train_x)
    xtest_tfidf =  tfidf_vect.transform(test_x)
    return xtrain_tfidf,xtest_tfidf
 
def classymodel(xtrain_tfidf, train_y, xtest_tfidf):
    #特征为词语级别TF-IDF向量的朴素贝叶斯
    accuracy = train_model(naive_bayes.MultinomialNB(), xtrain_tfidf, train_y, xtest_tfidf)
    print("NB, WordLevel TF-IDF: ", accuracy)


path = r"E:\download\nlp_text_classify\text" #文件夹目录
files= os.listdir(path) #得到文件夹下的所有文件名称
kf = KFold(n_splits=5,shuffle=True)
labels, texts = [], []

for file in files: #遍历文件夹
    position = path+'\\'+ file
    #print (position)           
    with open(position, "r",encoding='ISO-8859-1') as f:    #打开文件        
        lines = f.readlines()   #读取文件中的一行
        for line in lines:
            content = line.split()
            texts.append("".join(content[0:]))
            print(file)
            labels.append()
f.close()



#创建一个dataframe，列名为text和label
trainDF = pandas.DataFrame()
trainDF['text'] = texts
trainDF['label'] = labels

for train_index_x, test_index_x , train_index_y, test_index_y in kf.split(trainDF['text'], trainDF['label']):
    xtrain_tfidf, xtest_tfidf = TfIdf(trainDF,train_index_x,test_index_x)
    classymodel(xtrain_tfidf, train_index_y , xtest_tfidf)
    #print('train_index:%s , test_index: %s ' %(train_index,test_index))

#将数据集分为训练集和验证集
#train_x, valid_x, train_y, valid_y = model_selection.train_test_split(trainDF['text'], trainDF['label'])
 




