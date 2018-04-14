#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 20:17
# @Author  : Soloist
# @File    : getTeachers.py
# @Software: PyCharm
import os
import MakeDir


class GetTeachers:
    dir_name = ""

    @staticmethod
    def init(file_name):
        global dir_name
        dir_name = MakeDir.makedir(file_name.replace(".csv", ".getTeachers"))
        os.chdir(dir_name)
        right = open(file_name.replace(".csv", ".getTeachers.right.csv"), "w")
        error = open(file_name.replace(".csv", ".getTeachers.error.csv"), "w")
        os.chdir("../")
        return right, error

    @staticmethod
    def deal(line, *stream):
        stream = stream[0]
        os.chdir(dir_name)
        line_list = line.split(",")
        if line_list[4] == "200" and line_list[5] == "43\n":
            stream[1].write(line)
        elif line_list[4] == "200":
            stream[0].write(line)
        os.chdir("../")
