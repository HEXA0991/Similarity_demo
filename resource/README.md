datadet 里是数据集
model 是词向量模型，这个程序直接用的词向量模型没有用词向量
src 是源码，shorttext_lstm.py本来该是用来预测的程序，但是lstm中可以直接预测
所以shorttext_lstm.py相当于废弃了
lstm.py 是主程序，运行后就会在dump目录下生成结果
word2vec.py 是生成词向量模型的程序