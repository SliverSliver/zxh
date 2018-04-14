def txt2csv(input_file_name):
    output_file_name = input_file_name.replace("localhost_access_", "").replace(".txt", ".csv")
    with open(output_file_name, 'w') as csvfile:
        with open(input_file_name, 'r') as filein:
            for line in filein:
                line = line.replace("- - ", "").replace(' +0800', '').replace('"', '') \
                    .replace(' HTTP/1.0', '').replace(' ', ',')
                csvfile.write(line)
    return output_file_name
