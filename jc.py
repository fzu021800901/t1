import jieba
from gensim import corpora, models, similarities
import sys
import math

'''读取停用词'''
stop_words = open('stopwords.txt', 'r', encoding='utf-8').read()

'''用于删除停用词函数'''
def dec_stopwords(file_0):
        dec_l = []
        for word in file_0:
            if word not in stop_words:
                dec_l.append(word)
        if len(dec_l) == 0:
            print('文本为空')
        return dec_l

'''利用tfidf计算余弦相似度'''
def sim_value(file_o, file_t):
        '''待删标点符号数字'''
        punctuations = ['\n', '\t', '，', '。', '；', '：', "？", '、', '！', '《', '》',
                 '‘', '’', '“', '”', ' ', '1', '2', '3', '4', '5', '6', '7', '8',
                 '9', '0', '.', '*', '-', '—', ',', '——', '……', '（', '）', '…',
                 '%', '#', '@', '$', '￥', '~', '`', '~', '·']
        '''删除标点符号数字'''
        for punctuation in punctuations:
            file_o = file_o.replace(punctuation, '')
            file_t = file_t.replace(punctuation, '')

        list_o = []
        list_o.append(file_o)
        list_ori = []

        '''对论文进行分词操作，利用jieba'''
        xx = [word for word in jieba.cut(file_o)]
        list_ori.append(xx)
        list_ori.append([''])

        '''利用gensim生成论文的字典'''
        dictionary = corpora.Dictionary(list_ori)

        '''建立稀疏向量集'''
        corpus = [dictionary.doc2bow(tt) for tt in list_ori]

        '''对抄袭论文进行jieba分词'''
        file_test = [word for word in jieba.cut(file_t)]

        '''对抄袭论文建立稀疏向量'''
        file_test_vec = dictionary.doc2bow(file_test)

        '''建立tfidf'''
        tfidf = models.TfidfModel(corpus)
        index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))

        '''进行相似度计算'''
        sim_val = index[tfidf[file_test_vec]]
        '''返回计算值'''
        return sim_val[0]