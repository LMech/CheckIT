import variables
from datetime import datetime
import logging

import os
import filter_files


def get_time(initial_message: str) -> datetime:
    print(initial_message)
    date = input("The date should be formated as dd-mm-yyyy: ")
    return datetime.strptime(date, '%d-%m-%Y').date()


def get_path() -> str:
    while True:
        path = os.path.abspath(input("Enter the folder path\n"))
        if os.path.isdir(path):
            return path
        else:
            print("This path in invalid\n")


def initiate_variables():
    variables.path = get_path()
    variables.begin_time = get_time("Enter the begin time for filtering\n")
    variables.end_time = get_time("Enter the end time for filtering\n")


if __name__ == "__main__":
    logger = logging.getLogger("PyPDF2")
    logger.setLevel(logging.NOTSET)
    initiate_variables()
    filter_files.list_files(variables.path)
