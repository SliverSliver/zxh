if __name__ == "__main__":
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
