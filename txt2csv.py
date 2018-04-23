def txt2csv(input_file_name):
    output_file_name = input_file_name.replace("localhost_access_", "").replace(".txt", ".csv")
    with open(output_file_name, 'wb') as csvfile:
        with open(input_file_name, 'rb') as filein:
            for line in filein:
                line = bytes.decode(line)
                line = line.replace("  [ ", " ").replace(' ] - [ INFO ]  ', ' ').replace(', ', ';') \
                    .replace('  :  ', ':').replace(': ', ':').replace('  ', ' ').replace(' ', ',')
                line = str.encode(line)
                csvfile.write(line)
    return output_file_name
