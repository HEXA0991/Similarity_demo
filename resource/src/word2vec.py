# -*- encoding=UTF-8 -*-

import jieba
from gensim.models import Word2Vec

file_path = r'E:\dump\dataset\train.txt'
texts = [] #存放文件中所有字符
corpuses = [] #存放所有句子
segged = [] #存放分词完成的所有句子
with open(file_path, 'r') as file: #读入所有语料
    texts = file.readlines()

for text in texts: #将语料前两句话分开，存入corpuses中，别的不要
    temp = text.strip('\n')
    temp = temp.split('\t')
    corpuses.append(temp[0])
    corpuses.append(temp[1])

for corpus in corpuses: #对每个句子进行分词
    seg = list(jieba.cut(corpus))
    segged.append(seg)

model = Word2Vec(segged) #训练词向量
model.save(r'E:\dump\model\w2v.mod')
model.wv.save_word2vec_format(r'E:\dump\model\word_vector.vec', binary = False) #保存词向量文件
pass
