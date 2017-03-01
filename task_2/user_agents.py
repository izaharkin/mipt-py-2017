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
    browser = "\".*\""

    pattern = ipv4 + " " + skipped + " " + time + " " + query + \
        " " + code + " " + size + " " + referer + " " + browser
    return pattern


def pattern_ua_windows():
    ipv4 = "([0-9]|[1-9]\d|[1-9]\d\d)\.([0-9]|[1-9]\d|[1-9]\d\d)\." \
           "([0-9]|[1-9]\d|[1-9]\d\d)\.([0-9]|[1-9]\d|[1-9]\d\d)"
    skipped = "-" + " " + "-"
    time = "\[\d+/\w+/\d+:\d\d:\d\d:\d\d \+\d\d\d\d\]"
    query = "\"GET (/\S*)+ HTTP/\d\.\d\""
    code = "\d+"
    size = "\d+"
    referer = "\"\S*\""
    browser = "\".*Windows.*\""

    pattern = ipv4 + " " + skipped + " " + time + " " + query + \
        " " + code + " " + size + " " + referer + " " + browser
    return pattern


def pattern_ua_ubuntu():
    ipv4 = "([0-9]|[1-9]\d|[1-9]\d\d)\.([0-9]|[1-9]\d|[1-9]\d\d)\." \
           "([0-9]|[1-9]\d|[1-9]\d\d)\.([0-9]|[1-9]\d|[1-9]\d\d)"
    skipped = "-" + " " + "-"
    time = "\[\d+/\w+/\d+:\d\d:\d\d:\d\d \+\d\d\d\d\]"
    query = "\"GET (/\S*)+ HTTP/\d\.\d\""
    code = "\d+"
    size = "\d+"
    referer = "\"\S*\""
    browser = "\".*Ubuntu.*\""

    pattern = ipv4 + " " + skipped + " " + time + " " + query + \
        " " + code + " " + size + " " + referer + " " + browser
    return pattern


def pattern_ua_mac():
    ipv4 = "([0-9]|[1-9]\d|[1-9]\d\d)\.([0-9]|[1-9]\d|[1-9]\d\d)\." \
           "([0-9]|[1-9]\d|[1-9]\d\d)\.([0-9]|[1-9]\d|[1-9]\d\d)"
    skipped = "-" + " " + "-"
    time = "\[\d+/\w+/\d+:\d\d:\d\d:\d\d \+\d\d\d\d\]"
    query = "\"GET (/\S*)+ HTTP/\d\.\d\""
    code = "\d+"
    size = "\d+"
    referer = "\"\S*\""
    browser = "\".*Macintosh.*\""

    pattern = ipv4 + " " + skipped + " " + time + " " + query + \
        " " + code + " " + size + " " + referer + " " + browser
    return pattern


def parse_logs(string_to_parse):
    pattern_funcs = [pattern_ua_windows,
                     pattern_ua_ubuntu,
                     pattern_ua_mac,
                     pattern_all]
    stats = []
    for gen_func in pattern_funcs:
        pattern = gen_func()
        cur_stat = len(re.findall(pattern, string_to_parse))
        stats.append(cur_stat)
    stats[3] = stats[3] - (stats[0] + stats[1] + stats[2])
    d = {"Windows": stats[0], "Ubuntu": stats[1],
         "OS X": stats[2], "Unknown": stats[3]}
    d = sorted(d.items(), key=lambda x: x[1])
    return d


def output(result):
    for pair in result:
        print(str(pair[0]) + ": " + str(pair[1]))


def main():
    file_name = "input.txt"
    logs_to_parse = input_file(file_name)
    string_to_parse = ''.join(logs_to_parse)
    result = parse_logs(string_to_parse)
    output(result)


main()
