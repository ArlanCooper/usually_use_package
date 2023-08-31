基本说明
===
[toc]


# 目的
主要总结常用的一些包


# 数据库操作
- [mongodb](./database_operation/mongo_operation.py)
- [sqlalchemy](./database_operation/sqlalchemy_operation.py)


# 数据预处理
- [jieba分词](./data_process/jieba_split/jieba_split.py)
- [简繁体转换](./data_process/trandition2simple/main_process.py)
- [所有常用的字典](./data_process/common_dicts/)
    - [simple_dirty_words](./data_process/common_dicts/simple_dirty_words.txt) (小部分脏话)
    - [ill_words](./data_process/common_dicts/ill_words.txt)(疾病相关字典)
    - [porn_words](./data_process/common_dicts/porn_words.txt)(色情相关字典)
    - [complete_dirty_words](./data_process/common_dicts/complete_dirty_words.txt)(丰富的敏感词汇表)
    - [pregnant_words](./data_process/common_dicts/pregnant_words.txt)(孕妇词汇表)
    - [severe_words](./data_process/common_dicts/severe_words.txt)(重病词汇表)
- [pandas操作](./data_process/pandas/)
    - [pandas_tools](./data_process/pandas/pandas_tools.py)

# 时间处理
- [timeprocess](./time_operation/util_times.py)
