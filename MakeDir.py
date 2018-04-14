#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 22:07
# @Author  : Soloist
# @File    : MakeDir.py
# @Software: PyCharm
import os


def makedir(dir_name):
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    return dir_name
