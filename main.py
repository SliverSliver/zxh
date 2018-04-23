from GetFileName import GetFileName
import txt2csv
from Client import Client
import os


def split_by_time_and_request(suffix="txt"):
    # 获取所有txt文件
    txt_list = GetFileName.get_all(suffix)
    for txt in txt_list:
        # 转换csv文件名
        out_file_name = txt2csv.txt2csv(txt, suffix)
        # 按分钟分割csv, 返回目录名
        dir_name, dir_list = Client.split_by_minutes(out_file_name, 15)
        # 进入分割后目录
        os.chdir(dir_name)
        for dir_name in dir_list:
            os.chdir(dir_name)
            # 获取所有csv文件
            csv_list = GetFileName.get_all("csv")
            for csv in csv_list:
                # 按请求分割csv
                Client.assign_by_request(csv)
            os.chdir("../")
        # 返回上级目录
        os.chdir("../")


if __name__ == "__main__":
    split_by_time_and_request("log")
