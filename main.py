from GetFileName import GetFileName
import txt2csv
from Client import Client
import os

if __name__ == "__main__":
    # 获取所有txt文件
    txt_list = GetFileName.get_all("txt")
    for txt in txt_list:
        # 转换csv文件名
        out_file_name = txt2csv.txt2csv(txt)
        # 按分钟分割csv, 返回目录名
        dir_name = Client.split_by_minutes(out_file_name, 15)
        print(dir_name) # log.2018-04-14.hour=1
        # 按小时分割csv, 返回目录名
        # dir_name = Client.split_by_hour(out_file_name, 2)
        # 进入分割后目录
        # os.chdir(dir_name)
        # 获取所有csv文件
        # csv_list = GetFileName.get_all("csv")
        # for csv in csv_list:
            # Client.split_by_minutes(csv, 15)
        # 按请求分割csv
        # Client.assign_by_request(csv)
        # 返回上级目录
        # os.chdir("../")
