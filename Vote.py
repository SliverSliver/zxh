#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 20:50
# @Author  : Soloist
# @File    : Vote.py
# @Software: PyCharm
import MakeDir
import os


class Vote:
    dir_name = ""

    @staticmethod
    def init(file_name):
        global dir_name
        dir_name = MakeDir.makedir(file_name.replace(".csv", ".vote"))
        os.chdir(dir_name)
        right = open(file_name.replace(".csv", ".vote.right.csv"), "w")
        already = open(file_name.replace(".csv", ".vote.already.csv"), "w")
        notVote = open(file_name.replace(".csv", ".vote.notVote.csv"), "w")
        error = open(file_name.replace(".csv", ".vote.error.csv"), "w")
        os.chdir("../")
        return right, already, notVote, error

    @staticmethod
    def deal(line, *stream):
        stream = stream[0]
        os.chdir(dir_name)
        line_list = line.split(",")
        if line_list[4] == "200":
            if line_list[5] == "45\n":
                stream[0].write(line)
            elif line_list[5] == "49\n":
                stream[1].write(line)
            elif line_list[5] == "43\n":
                stream[3].write(line)
        else:
            stream[2].write(line)
        os.chdir("../")
