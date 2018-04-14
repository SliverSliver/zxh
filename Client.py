#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/14 19:59
# @Author  : Soloist
# @File    : Client.py
# @Software: PyCharm
from GetTeachers import GetTeachers
from GetTeacher import GetTeacher
from Vote import Vote
import os
import MakeDir


class Client:

    @staticmethod
    def assign_by_request(file_name):
        with open(file_name, "r") as filein:
            os.chdir(MakeDir.makedir(file_name.replace(".csv", "")))
            get_teacher = GetTeacher.init(file_name)
            vote = Vote.init(file_name)
            get_teachers = GetTeachers.init(file_name)

            for line in filein:
                line_list = line.split(",")
                if line_list[3].find("getTeachers") != -1:
                    GetTeachers.deal(line, get_teachers)
                elif line_list[3].find("getTeacher") != -1:
                    GetTeacher.deal(line, get_teacher)
                elif line_list[3].find("vote") != -1:
                    Vote.deal(line, vote)
            os.chdir("../")

    # 默认按1分钟分割
    @staticmethod
    def split_by_minutes(file_name, minutes=1):
        file_name = file_name
        dir_name = file_name.replace(".csv", ".minutes=" + str(minutes))

        # 创建目录
        MakeDir.makedir(dir_name)
        # 打开文件
        with open(file_name, 'r') as filein:
            # 进入目录
            os.chdir(dir_name)
            # 第一行
            first_line = filein.readline()
            csvlist = first_line.split(",")
            time = Client.__get_time(csvlist[1]) + minutes

            i = 0
            fileout = open(file_name.replace(".csv", "." + str(i) + ".csv"), "w")
            fileout.write(first_line)

            for line in filein:
                csvlist = line.split(",")
                nowtime = Client.__get_time(csvlist[1])

                # 由于时间大于60时会归0，判断当前列时间是否为下一小时
                if time >= 60 and nowtime <= time % 60:
                    nowtime += 60

                if nowtime < time:
                    fileout.write(line)
                else:
                    time = (time + minutes) if time < 60 else (time + minutes) % 60
                    i += 1
                    fileout.close()
                    fileout = open(file_name.replace(".csv", "." + str(i) + ".csv"), "w")
                    fileout.write(line)
            fileout.close()
        # 返回上级目录
        os.chdir("../")
        return dir_name

    @staticmethod
    def split_by_method(file_name):
        dir_name = file_name.replace(".csv", ".method")
        MakeDir.makedir(dir_name)

        with open(file_name, "r") as filein:
            os.chdir(dir_name)
            fileout_get = open(file_name.replace(".csv", ".method=GET.csv"), "w")
            fileout_post = open(file_name.replace(".csv", ".method=POST.csv"), "w")
            for line in filein:
                row = line.split(",")
                if row[2] == "GET":
                    fileout_get.write(line)
                elif row[2] == "POST":
                    fileout_post.write(line)
        os.chdir("../")
        return dir_name

    @staticmethod
    def __get_time(date):
        date = date.replace("[", "").replace("]", "")
        date = date.split("/")[2]
        time = date.split(":")[2]
        return int(time)
