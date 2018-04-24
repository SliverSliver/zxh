import os
import numpy as np


def replace_csv():
    input_file_name = "temp.csv"
    # output_file_name = input_file_name.replace("localhost_access_", "").replace(".txt", ".csv")
    output_file_name = input_file_name.replace("temp", "temp2")
    with open(output_file_name, 'w', encoding="utf-8") as csv_file:
        with open(input_file_name, 'r', encoding="utf-8") as filein:
            for line in filein:
                line = line.replace('.', ' ').replace('hour=', '').replace(':00:00-14:59', ':00:00') \
                    .replace(':15:00-29:59', ':15:00').replace(':30:00-44:59', ':30:00') \
                    .replace(':45:00-59:59', ':45:00').replace("-", "/").replace("\n", ",1\n")
                # line = line.replace("access.", "access_2018-04-23.").replace('access_', '').replace('hour=', '')\
                #     .replace('minutes=00.csv', ':00:00-14:59').replace('minutes=15.csv', ':15:00-29:59')\
                #     .replace('minutes=30.csv', ':30:00-44:59').replace('minutes=45.csv', ':45:00-59:59')
                csv_file.write(line)


def np_add_csv():
    for i in range(19, 23):
        os.chdir("log")
        csv_1 = np.loadtxt(open("1.info.log.2018-04-" + str(i) + ".count.csv", "rb"), delimiter=",", skiprows=0)
        csv_2 = np.loadtxt(open("2.info.log.2018-04-" + str(i) + ".count.csv", "rb"), delimiter=",", skiprows=0)
        csv_3 = np.loadtxt(open("3.info.log.2018-04-" + str(i) + ".count.csv", "rb"), delimiter=",", skiprows=0)
        csv_4 = csv_1 + csv_2 + csv_3
        os.chdir("../")
        np.savetxt("info.log.2018-04-" + str(i + 18) + ".count.csv", csv_4, fmt="%d", delimiter=',')


def csv_file_add():
    csv_1 = np.loadtxt(open("info.log.2018-04-19.count.csv", "rb"), delimiter=",", skiprows=0)
    csv_2 = np.loadtxt(open("info.log.2018-04-20.count.csv", "rb"), delimiter=",", skiprows=0)
    csv_3 = np.loadtxt(open("info.log.2018-04-21.count.csv", "rb"), delimiter=",", skiprows=0)
    csv_4 = np.loadtxt(open("info.log.2018-04-22.count.csv", "rb"), delimiter=",", skiprows=0)
    csv_5 = np.concatenate((csv_1, csv_2, csv_3, csv_4))
    np.savetxt("info.log.2018-04-19 - 4-22.count.csv", csv_5, fmt="%d", delimiter=',')


def csv_row_add():
    csv = np.loadtxt(open("info.log.2018-04-19 - 4-22.count.csv", "rb"), delimiter=",", skiprows=0)
    for i in range(1, len(csv)):
        csv[i] += csv[i - 1]
    np.savetxt("info.log.count.csv", csv, fmt="%d", delimiter=',')


def csv_add_time():
    with open("info.log.count.csv", 'r', encoding="utf-8") as csv_file:
        with open("info.log.csv", 'w', encoding="utf-8") as fileout:
            time = []
            for d in range(19, 23):
                for Hour in range(0, 24):
                    for Minutes in range(0, 60, 15):
                        time.append("2018-04-" + str(d).zfill(2) + " " + str(Hour).zfill(2) + ":"
                                    + str(Minutes).zfill(2) + ":00,")

            i = 0
            for line in csv_file:
                line = time[i] + line
                fileout.write(line)
                i += 1


if __name__ == "__main__":
    csv_row_add()
    csv_add_time()
