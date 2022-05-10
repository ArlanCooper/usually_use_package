# -*- coding:utf-8 -*-
'''
功能：各类时间函数处理

'''
import time
from datetime import datetime,timedelta

class TimeProcess():
    def time2datetime(self, timestamp):
        '''
        将时间戳数字转换成datetime
        :param timestamp: 时间戳，数字
        :return: datetime格式的时间
        '''
        if isinstance(timestamp,float):
            timestamp = int(timestamp)
        if isinstance(timestamp,int):
            return datetime.fromtimestamp(timestamp)
        else:
            raise ValueError('时间戳数字不是int，请修改后重新处理')
    def time2str(self,timestamp,str_format = '%Y-%m-%d %H:%M:%S'):
        '''
        将时间戳数字转换成str
        :param timestamp: 时间戳，数字
        :param str_format 返回的str格式，默认%Y-%m-%d %H:%M:%S
        :return: str格式的时间
        '''
        if isinstance(timestamp,float):
            timestamp = int(timestamp)
        if isinstance(timestamp,int):
            return time.strftime(str_format, time.localtime(timestamp))
        else:
            raise ValueError('时间戳数字不是int，请修改后重新处理')
    def str2time(self,time_str,str_format = '%Y-%m-%d %H:%M:%S'):
        '''
        str转成timestamp数字类型
        :param time_str:
        :param str_format:
        :return:
        '''
        if isinstance(time_str,str):
            return time.mktime(time.strptime(time_str, str_format))
        else:
            raise ValueError('不是str，或者请修改后重新处理')
    def str2datetime(self,time_str,str_format = '%Y-%m-%d %H:%M:%S'):
        '''
        str转换成datetime
        :param time_str:
        :param str_format:
        :return:
        '''
        if isinstance(time_str,str):
            return datetime.strptime(time_str, str_format)
        else:
            raise ValueError('不是str，或者请修改后重新处理')
    def datetime2time(self,date_type):
        '''
        datetime 转变成 timestamp 数字类型
        :param date_type:
        :return:
        '''
        if isinstance(date_type,datetime):
            return time.mktime(date_type.timetuple())
        else:
            raise ValueError('不是datetime，或者请修改后重新处理')

    def datetime2str(self,date_type,  str_format = '%Y-%m-%d %H:%M:%S'):
        '''
        datetime 转换成str
        :param date_type:
        :param str_format:
        :return:
        '''
        if isinstance(date_type,datetime):
            return date_type.strftime(str_format)
        else:
            raise ValueError('不是datetime，或者请修改后重新处理')

    def get_special_time(self,date_type,hour=0,minute=0,second=0,microsecond=0):
        '''
        获取某日期特定的时间
        :param date_type: 某日期的时间
        :param hour: 当日小时设定值，默认0点
        :param minute:当日分钟设定值，默认0分
        :param second:当日秒设定值，默认0秒
        :param microsecond:当日微秒设定值，默认0毫秒
        :return:date_type当天特定的时间
        '''
        if isinstance(date_type, datetime):
            return date_type.replace(hour=0, minute=0, second=0, microsecond=0)
        else:
            raise ValueError('不是datetime，或者请修改后重新处理')
    def compute_days_diff(self,date1,date2):
        '''
        计算两个时间的相差的天数
        :param date1:第一个时间
        :param date2:第二个时间
        :return:
        '''
        if isinstance(date1,str):
            date1 = self.str2datetime(date1)
        if isinstance(date2,str):
            date2 = self.str2datetime(date2)
        if not isinstance(date1,datetime) or not isinstance(date2,datetime):
            raise ValueError('两个日期中至少一个不是datetime，或者请修改后重新处理')

        return (date1 - date2).days

    def compute_seconds_diff(self,date1,date2):
        '''
        计算两个时间的相差的秒数
        :param date1:第一个时间
        :param date2:第二个时间
        :return: 相差的秒数
        '''
        if isinstance(date1,str):
            date1 = self.str2datetime(date1)
        if isinstance(date2,str):
            date2 = self.str2datetime(date2)
        if not isinstance(date1,datetime) or not isinstance(date2,datetime):
            raise ValueError('两个日期中至少一个不是datetime或者str，或者请修改后重新处理')

        return (date1 - date2).total_seconds()


if __name__ == '__main__':
    test = TimeProcess()
    test_int = time.time()
    test_str = '2022-05-09 02:00:00'
    date_today = datetime.today()
    last = datetime.strptime('2022-04-12 20:11:22', '%Y-%m-%d %H:%M:%S')
    print(test.str2time(test_str))
    print(test.time2str(test_int))
    print(test.time2datetime(test_int))
    print(test.str2datetime(test_str))
    print(test.datetime2time(date_today))
    print(test.datetime2str(date_today))
    print(test.get_special_time(date_today))
    print(test.compute_days_diff(date_today,last))
    print(test.compute_seconds_diff(test_str, last))