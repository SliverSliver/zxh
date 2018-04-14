def txt2csv(inputFileName, outputFileName):
    with open(outputFileName, 'wb') as csvfile:
        with open(inputFileName, 'rb') as filein:
            for line in filein:
                line = bytes.decode(line)
                line = line.replace("- - ", "").replace(' +0800', '').replace('"', '') \
                    .replace(' HTTP/1.0', '').replace(' ', ',')
                line = str.encode(line)
                csvfile.write(line)
