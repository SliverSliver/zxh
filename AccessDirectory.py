import os


def get_lines(filename):
    file = open(filename, "r", encoding="UTF-8")
    lines = file.readlines()
    lines_count = len(lines)
    return lines_count


def get_directory(file):
    dir_list = os.listdir(os.getcwd())
    if len(dir_list):
        for i in range(0, len(dir_list)):
            path = os.path.join(os.getcwd(), dir_list[i])
            if os.path.isfile(path):
                if path.find(".csv") != -1:
                    line = dir_list[i] + "," + str(get_lines(path)) + "\n"
                    file.write(line)
            elif os.path.isdir(path):
                os.chdir(path)
                get_directory(file)
                os.chdir("../")


if __name__ == "__main__":
    file_list = open("file_list.csv", "w", encoding="UTF-8")
    get_directory(file_list)
    file_list.close()
