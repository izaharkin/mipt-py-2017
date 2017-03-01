import re


def input_file(file_name):
    with open(file_name, "r") as log_file:
        return [line for line in log_file]


def parse_logs(string_to_parse):
    ipv4 = "([0-9]|[1-9]\d|[1-9]\d\d)\.([0-9]|[1-9]\d|[1-9]\d\d)\." \
           "([0-9]|[1-9]\d|[1-9]\d\d)\.([0-9]|[1-9]\d|[1-9]\d\d)"
    skipped = "-" + " " + "-"
    time = "\[\d+/\w+/\d+:\d\d:\d\d:\d\d \+\d\d\d\d\]"
    query = "\"GET (/\S*)+ HTTP/\d\.\d\""
    code = "\d+"
    size = "\d+"
    referer = "\"\S*\""
    browser = "\"Go-http-client/1.1\""  # !

    pattern = ipv4 + " " + skipped + " " + time + " " + query + \
        " " + code + " " + size + " " + referer + " " + browser
    pattern = re.compile(pattern)
    matches = re.findall(pattern, string_to_parse)
    return len(matches)


def main():
    file_name = "input.txt"
    logs_to_parse = input_file(file_name)
    string_to_parse = ''.join(logs_to_parse)
    number_of_queries = parse_logs(string_to_parse)
    print(number_of_queries)


main()
