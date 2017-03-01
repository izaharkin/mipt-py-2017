

def input_file(file_name):
    with open(file_name, "r") as log_file:
        return [line for line in log_file]


def parse_logs(text_to_parse):
    wincnt = ubcnt = maccnt = allcnt = 0
    for line in text_to_parse:
        allcnt += 1
        wincnt += "Windows" in line[line.find("HTTP"):]
        ubcnt += "Ubuntu" in line[line.find("HTTP"):]
        maccnt += "Macintosh" in line[line.find("HTTP"):]
    other = allcnt - (wincnt + ubcnt + maccnt)
    d = {"Windows": wincnt, "Ubuntu": ubcnt,
         "OS X": maccnt, "Unknown": other}
    d = sorted(d.items(), key=lambda x: x[1])
    return d


def output(result):
    for pair in result:
        print(str(pair[0]) + ": " + str(pair[1]))


def main():
    file_name = "input.txt"
    logs_to_parse = input_file(file_name)
    result = parse_logs(logs_to_parse)
    output(result)


main()
