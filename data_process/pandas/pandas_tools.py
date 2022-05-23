# -*- coding:utf-8 -*-

"""
pandas数据处理的一些组件
"""
import pandas as pd
import datetime
import numpy as np


null_list = [np.nan, np.NaN, " ", "", None, "nan", "NaN", "None", "null", []]


def is_null(tgt):
    """
    查看输入的是不是null

    :param tgt: 输入的string或者unicode
    :return: boolean
    """
    if tgt not in null_list and not pd.isnull(tgt):
        isnull_res = False
    else:
        isnull_res = True

    return isnull_res


def rm_space(tgt, rm_all=True):
    """
    删除字符的

    :param tgt: 输入的string或者unicode
    :param rm_all: 是否删除所有的空格
    :return: string or unicode
    """
    rm_tgt = ""
    if tgt:
        if rm_all:
            rm_tgt = tgt.strip().replace(" ", "")
        else:
            rm_tgt = tgt.strip()
    return rm_tgt


def null_to_nan_df(df):
    """
    把df的空值情况转成np.NaN

    :param df: DataFrame
    :return: DataFrame
    """
    if df.empty is False:
        df = df.applymap(lambda x: bool(x in null_list) and np.NaN or x)
    return df


def list_rm_null(list_param):
    """
    去除list里面的空值

    :param list_param:
    :return:
    """
    no_null_list = []
    if list_param:
        no_null_list = [i for i in list_param if i not in null_list and not pd.isnull(i)]

    return no_null_list


def series_rm_null(series_param):
    """
    去除series里的空值
    :param series_param:
    :return:
    """
    no_null_series = series_param.dropna()
    for each_index in no_null_series.index:
        if no_null_series.ix[each_index] in null_list:
            no_null_series.drop(each_index, inplace=True)
    return no_null_series


def df_to_dict(df):
    """
    把dataframe转换成dict

    :param df: dataframe
    :return: list of dict
    """
    src_list = []
    if df.empty is False:
        for row_idx, row_data in df.iterrows():
            src_list.append(row_data.to_dict())

    return src_list


def df_time_transfer(df, ipt_tvar, opt_tvar, transfer_type="mth"):
    """
    df时间转换工具

    :param df: 输入的df
    :param ipt_tvar: 需要转换参数
    :param opt_tvar: 需要输出参数
    :param transfer_type: 根据转换需求
    :return: 输出df
    """
    if df.empty is False:
        df[ipt_tvar] = df[ipt_tvar].map(
            lambda x: datetime.datetime.strptime(x, '%Y-%m-%d %H:%M:%S') if not is_null(x) and type(x) == str else x)
        if transfer_type == "mth":
            fmt_time = '%Y-%m'
        elif transfer_type == "day":
            fmt_time = '%Y-%m-%d'
        df[opt_tvar] = df[ipt_tvar].map(lambda x: (not is_null(x)) and x.strftime(fmt_time) or "")

    return df


def df_map_rm_space(df, column_name):
    """
    对于某series去除空格等

    :param df: 输入的df
    :param column_name: 列名
    :return: 输出df
    """
    if df.empty is False:
        df[column_name] = df[column_name].map(lambda x: rm_space(x) if not is_null(x) else x)
    return df


def df_apply_rm_space(df, exclude_columns=None):
    """
    对于全部列去除空格等
    :param df: 输入的df
    :param exclude_columns: 不执行apply的列表
    :return: 输出df
    """
    _opt_df = pd.DataFrame()
    if df.empty is False:
        if exclude_columns:
            df_columns = df.columns
            include_columns = [col for col in df_columns if col not in exclude_columns]
            _opt_df = pd.DataFrame(df, columns=include_columns)
            _opt_df = _opt_df.applymap(lambda x: rm_space(x) if not is_null(x) and type(x) is str else x)
            for exl_col in exclude_columns:
                if exl_col in df_columns:
                    _opt_df[exl_col] = df[exl_col]
        else:
            _opt_df = df.applymap(lambda x: rm_space(x) if not is_null(x) else x)

    return _opt_df


def df_apply_convert_nan_none(df, exclude_columns=None):
    """
    对全部列中存在的nan值替换成None

    :param df:
    :param exclude_columns: 排除的列, 某些列无法的类型不能做转换, 例如 list
    :return:
    """
    _opt_df = pd.DataFrame()

    if df.empty is False:
        if exclude_columns:
            df_columns = df.columns
            include_columns = [col for col in df_columns if col not in exclude_columns]
            _opt_df = pd.DataFrame(df, columns=include_columns)
            _opt_df = _opt_df.applymap(lambda x: x if not is_null(x) else None)
            for exl_col in exclude_columns:
                if exl_col in df_columns:
                    _opt_df[exl_col] = df[exl_col]
        else:
            _opt_df = df.applymap(lambda x: x if not is_null(x) else None)

    return _opt_df
