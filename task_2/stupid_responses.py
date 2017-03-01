

def input_file(file_name):
    with open(file_name, "r") as log_file:
        return [line for line in log_file]


def parse_logs(text_to_parse):
    cnt200 = cnt300 = allcnt = 0
    for line in text_to_parse:
        allcnt += 1
        new_line = line[line.find("HTTP")+10:]
        cnt200 += (new_line.find("200") == 0)
        cnt300 += (new_line.find("30") == 0)
    other = allcnt - (cnt200 + cnt300)
    res = [cnt200, cnt300, other, allcnt]
    return res


def output(result):
    print("\n".join(str(x) for x in result))


def main():
    file_name = "input.txt"
    logs_to_parse = input_file(file_name)
    result = parse_logs(logs_to_parse)
    output(result)


main()
