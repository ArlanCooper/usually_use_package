# -*- coding:utf-8 -*-

import pymongo
from loguru import logger

#####################################  mongo连接

class MyMongo():
    def __init__(self,url,db_name):
        self.connect_mongo(url)
        self.connect_db(db_name)

    def connect_mongo(self,url):
        '''
        连接mongo数据库
        :param url:
        :return:
        '''
        try:
            self.ali_mongo = pymongo.MongoClient(url)
            logger.info('连接mongo成功')
        except Exception as e:
            logger.error('连接mongo失败，请查看具体原因',e)
            self.ali_mongo = None

    def connect_db(self, db_name):
        '''
        连接对应的数据库
        :param db_name:
        :return:
        '''
        try:
            self.db = self.ali_mongo[db_name]
            logger.info('连接数据库成功')
        except Exception as e:
            logger.error('没有该名称的数据库，请查看具体原因', e)
            self.db = None
    def get_colection(self,collection_name):
        '''
        获取collection
        :param collection_name:
        :return:
        '''
        try:
            collection = self.db.get_collection(collection_name)
            logger.info('读取collection成功')
        except Exception as e:
            collection = None
            logger.error('读取collection 失败，具体查看报错原因',e)
        return collection
    def generate_data(self,table_name, col_dics={"_id":0}):
        '''
        获取需要的数据
        :param col_dics:{"id":0} 不需要哪个字段显示，则将该字段设置为零，默认全部显示
        :return:
        '''
        try:
            collection = self.db.get_collection(table_name)
            data = collection.find({}, col_dics)
            logger.info('获取数据成功')
        except Exception as e:
            data = None
            logger.error('获取数据失败，具体查看原因:',e)
        return data

    def find_one(self, table_name, dic):
        '''
        :param table: str 数据库中的集合
        :param dic: dict 查询条件
        :return: dict 返回单条记录的字典
        '''
        try:
            collection = self.db[table_name]
            rep = collection.find_one(dic)
        except Exception as e:
            logger.error('查找数据报错')
            rep = None

        return rep

    def find(self, table_name, dic,columns={"_id":0}):
        '''
        获取需要的数据
        :param col_dics:{"id":0} 不需要哪个字段显示，则将该字段设置为零，默认全部显示
        :return:
        '''
        try:
            collection = self.db.get_collection(table_name)
            data = collection.find(dic, columns)
            #logger.info('获取数据成功')
        except Exception as e:
            data = None
            logger.error('获取数据失败，具体查看原因:',e)
        return data

    def insert_one(self,table_name,data):
        '''
        插入一条数据
        :param table_name:
        :param data:
        :return:
        '''
        # try:
        #     collection = self.db.get_collection(table_name)
        #     collection.insert_one(data)
        #     return True
        # except Exception as e:
        #     logger.error('插入数据错误，请查看原因：',e)
        #     return False
        collection = self.db.get_collection(table_name)
        collection.insert_one(data)
        return True

    def insert_many(self,table_name, data):
        '''

        :param table_name:
        :param data:
        :return:
        '''
        try:
            collection = self.db.get_collection(table_name)
            print('collection:',type(collection))
            len_data = len(data)
            print('len_data:',len_data)
            #分块插入
            while len_data > 500:
                tmp = data[:500]
                collection.insert_many(tmp)
                data = data[500:]
                len_data = len(data)
            collection.insert_many(data)
            print('----------')
            logger.info('插入数据成功')
            return True
        except Exception as e:
            logger.error('插入数据错误，请查看原因：', e)
            return False

    def update_one(self,table_name,condition,dic):
        '''
                :param table_name: str 数据库中的集合
                :param condition: dict 查询条件
                :param dic: dict 更新的数据
                :return: 返回UpdateResult对象
        '''
        try:
            collection = self.db[table_name]
            # $set 表示只更新dic字典内存在的字段
            rep = collection.update_one(condition, {'$set': dic})
            logger.info('更新数据成功')
            # 会把之前的数据全部用dic字典替换，如果原本存在其他字段，则会被删除
            # rep = collection.update_one(condition, dic)
            return True
        except Exception as e:
            logger.error('更新单条数据失败,具体原因请查看:', e)
            return False

    def update_many(self,table_name, condition, dic):
        '''
                :param table_name: str 数据库中的集合
                :param condition: dict 查询条件
                :param dic: dict 更新的数据
                :return:返回UpdateResult对象
        '''
        try:
            collection = self.db[table_name]
            # $set 表示只更新dic字典内存在的字段
            rep = collection.update_many(condition, {'$set': dic})
            # 会把之前的数据全部用dic字典替换，如果原本存在其他字段，则会被删除
            # rep = collection.update_many(condition, dic)
        except Exception as e:
            logger.error('更新数据失败，具体原因请查看:', e)

    def update_insert_one(self,table_name,condition,dic):
        '''
        更新插入操作
                :param table_name: str 数据库中的集合
                :param condition: dict 查询条件
                :param dic: dict 更新的数据
                :return: 返回UpdateResult对象
        '''
        try:
            collection = self.db[table_name]
            # $set 表示只更新dic字典内存在的字段，upsert存在则更新，不存在则插入
            rep = collection.update_one(condition, {'$set': dic}, upsert=True)
            logger.info('更新数据成功')
            # 会把之前的数据全部用dic字典替换，如果原本存在其他字段，则会被删除
            # rep = collection.update_one(condition, dic)
            return True
        except Exception as e:
            logger.error('更新单条数据失败,具体原因请查看:', e)
            return False

