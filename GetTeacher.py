#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 20:48
# @Author  : Soloist
# @File    : GetTeacher.py
# @Software: PyCharm
import os
import MakeDir


class GetTeacher:
    dir_name = ""

    @staticmethod
    def init(file_name):
        global dir_name
        dir_name = MakeDir.makedir(file_name.replace(".csv", ".getTeacher"))
        os.chdir(dir_name)
        right = open(file_name.replace(".csv", ".getTeacher.right.csv"), "w")
        error = open(file_name.replace(".csv", ".getTeacher.error.csv"), "w")
        os.chdir("../")
        return right, error

    @staticmethod
    def deal(line, *stream):
        stream = stream[0]
        os.chdir(dir_name)
        line_list = line.split(",")
        if line_list[4] == "200" and line_list[5].find("43") != -1:
            stream[1].write(line)
        elif line_list[4] == "200":
            stream[0].write(line)
        os.chdir("../")
