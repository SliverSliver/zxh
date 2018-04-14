#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 19:40
# @Author  : Soloist
# @File    : GetFileName.py
# @Software: PyCharm
import os


class GetFileName:

    @staticmethod
    def get_all(suffix):
        dir_list = os.listdir(os.getcwd())
        txt_list = []
        for file_name in dir_list:
            if file_name.find("." + suffix) != -1:
                txt_list.append(file_name)
        return txt_list
