from GetFileName import GetFileName
import txt2csv
from Client import Client
import os
import re


def split_and_count_info():
    txt_list = GetFileName.get_all("txt")
    for txt in txt_list:
        out_file_name = txt2csv.txt2csv(txt)
        dir_name, dir_list = Client.split_by_minutes(out_file_name, 15)
        with open(out_file_name.replace(".csv", ".count.csv"), "w") as fileout:
            os.chdir(dir_name)
            for dir_ in dir_list:
                os.chdir(dir_)
                file_list = GetFileName.get_all("csv")
                for file_name in file_list:
                    print(file_name)
                    teacher_id = [0 for i in range(52)]
                    with open(file_name, "r", encoding="UTF-8") as filein:
                        for line in filein:
                            line_list = line.split(",")
                            if line_list[3].find("投票") != -1:
                                key = re.findall(r'[^\[\]]+', line_list[3])
                                if len(key) == 3:
                                    votes = key[1].split(";")
                                    if len(votes) == 5:
                                        for vote in votes:
                                            if int(vote) < 53:
                                                teacher_id[int(vote) - 1] += 1
                    index = file_name.find("hour=")
                    index1 = file_name.find("minutes=")
                    line_result = file_name[index + 5: index + 7] + "," + file_name[index1 + 8: index1 + 10] + ","
                    count = 0
                    for i in teacher_id:
                        count += i
                        line_result += str(i) + ","
                    fileout.write(line_result + str(count) + "\n")
                os.chdir("../")
            os.chdir("../")


if __name__ == "__main__":
    split_and_count_info()
