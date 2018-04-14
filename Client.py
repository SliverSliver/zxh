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
from GetFileName import GetFileName


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

    # 默认按15分钟分割
    @staticmethod
    def split_by_minutes(file_name, minutes=15):
        dir_name = Client.split_by_hour(file_name)
        os.chdir(dir_name)
        file_list = GetFileName.get_all("csv")
        for name in file_list:
            with open(name, "r") as filein:
                os.chdir(MakeDir.makedir(name.replace(".csv", "")))
                stream_list = []
                for i in range(0, 60, minutes):
                    stream_list.append(open(name.replace(".csv", "minutes=" + str(i) + ".csv"), "w"))
                for line in filein:
                    nowminutes = Client.__get_time(line)
                    stream_list[int(nowminutes / minutes)].write(line)
                for stream in stream_list:
                    stream.close()
            os.chdir("../")
        # 返回上级目录
        os.chdir("../")
        return dir_name

    @staticmethod
    def split_by_hour(file_name, hour=1):
        file_name = file_name
        dir_name = file_name.replace(".csv", ".hour=" + str(hour))

        # 创建目录
        MakeDir.makedir(dir_name)
        # 打开文件
        with open(file_name, 'r') as filein:
            # 进入目录
            os.chdir(dir_name)
            # 创建文件
            stream_list = []
            for i in range(0, 24, hour):
                stream_list.append(open(file_name.replace(".csv", "." + "hour=" + str(i) + ".csv"), "w"))

            for line in filein:
                nowhour = Client.__get_time(line, "hour")
                stream_list[int(nowhour / hour)].write(line)
            for stream in stream_list:
                stream.close()

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
    def __get_time(date, time_type="minutes"):
        time = ""
        if time_type == "minutes":
            time = date.split(":")[2]
        elif time_type == "hour":
            time = date.split(":")[1]
        return int(time)
