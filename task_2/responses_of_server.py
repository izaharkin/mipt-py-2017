import re


def input_file(file_name):
    with open(file_name, "r") as log_file:
        return [line for line in log_file]


def pattern_all():
    ipv4 = "([0-9]|[1-9]\d|[1-9]\d\d)\.([0-9]|[1-9]\d|[1-9]\d\d)\." \
           "([0-9]|[1-9]\d|[1-9]\d\d)\.([0-9]|[1-9]\d|[1-9]\d\d)"
    skipped = "-" + " " + "-"
    time = "\[\d+/\w+/\d+:\d\d:\d\d:\d\d \+\d\d\d\d\]"
    query = "\"GET (/\S*)+ HTTP/\d\.\d\""
    code = "\d+"
    size = "\d+"
    referer = "\"\S*\""
    browser = "\"*\""

    pattern = ipv4 + " " + skipped + " " + time + " " + query + \
        " " + code + " " + size + " " + referer + " " + browser
    return pattern


def pattern_code_200():
    ipv4 = "([0-9]|[1-9]\d|[1-9]\d\d)\.([0-9]|[1-9]\d|[1-9]\d\d)\." \
           "([0-9]|[1-9]\d|[1-9]\d\d)\.([0-9]|[1-9]\d|[1-9]\d\d)"
    skipped = "-" + " " + "-"
    time = "\[\d+/\w+/\d+:\d\d:\d\d:\d\d \+\d\d\d\d\]"
    query = "\"GET (/\S*)+ HTTP/\d\.\d\""
    code = "200"
    size = "\d+"
    referer = "\"\S*\""
    browser = "\"*\""

    pattern = ipv4 + " " + skipped + " " + time + " " + query + \
        " " + code + " " + size + " " + referer + " " + browser
    return pattern


def pattern_code_300309():
    ipv4 = "([0-9]|[1-9]\d|[1-9]\d\d)\.([0-9]|[1-9]\d|[1-9]\d\d)\." \
           "([0-9]|[1-9]\d|[1-9]\d\d)\.([0-9]|[1-9]\d|[1-9]\d\d)"
    skipped = "-" + " " + "-"
    time = "\[\d+/\w+/\d+:\d\d:\d\d:\d\d \+\d\d\d\d\]"
    query = "\"GET (/\S*)+ HTTP/\d\.\d\""
    code = "30\d"
    size = "\d+"
    referer = "\"\S*\""
    browser = "\"*\""

    pattern = ipv4 + " " + skipped + " " + time + " " + query + \
        " " + code + " " + size + " " + referer + " " + browser
    return pattern


def parse_logs(string_to_parse):
    pattern_funcs = [pattern_code_200,
                     pattern_code_300309,
                     pattern_all]
    stats = []
    for gen_func in pattern_funcs:
        pattern = gen_func()
        cur_stat = len(re.findall(pattern, string_to_parse))
        stats.append(cur_stat)
    stats.insert(2, stats[2] - (stats[0] + stats[1]))
    return stats


def output(result):
    print("\n".join(str(x) for x in result))


def main():
    file_name = "input.txt"
    logs_to_parse = input_file(file_name)
    string_to_parse = ''.join(logs_to_parse)
    result = parse_logs(string_to_parse)
    output(result)


main()
