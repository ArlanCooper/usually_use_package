# -*- coding:utf-8 -*-

import jieba


########## 切词
#读入自定义词典
jieba.load_userdict('./dict/custom_dict.txt')


with open('./dict/stop_words.txt', 'r', encoding='utf8') as f:
    stop_words = [word.strip() for word in f.readlines()]


def get_split_words(sentence):
    '''
    功能:切分语句，并返回最终的结果
    :param sentence:
    :return:
    '''
    words = jieba.cut(sentence) #切词
    filter_words = [word for word in words if word not in stop_words and len(word) >0 ]
    return filter_words
