from datetime import datetime as dt

# Function creates a new txt file to contain the data
def create_txt(file_name: str):
    file_handle = open(file_name, "w", encoding="utf-16")
    return file_handle

def is_time_between(
    check_time: dt,
) -> bool:
    """
    Checks if a time between in a margin
    """
    return variables.begin_time < check_time.date() < variables.end_time


def is_not_tmp(path: str):
    """
    Check if the file temporary
    """
    if "~$" in path:
        return False
    return True