#!/usr/bin/env python3
import sys
import re


def error_search(logging_file):
    error = input("What is the error? ")
    returneds_errors = []
    with open(logging_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in error_patterns):
                returneds_errors.append(log)
        file.close()
    return returneds_errors


def file_output(returned_errors):
    # with open(os.path.expanduser('~') + '/data/errors_found.log', 'w') as file:
    with open("errors_found.log", 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()


if __name__ == "__main__":
    log_file = "fishy.log"
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)


# Test input : "CRON ERROR Failed to start"