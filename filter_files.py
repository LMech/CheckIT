import os
import time as tm
from datetime import datetime as dt
from glob import glob
from tqdm import tqdm

import variables
import utils
import check





def list_files(path):
    """
    List all the corrupted files in the path
    """
    print(
        "The filtering process started\nThe specified path is {0}\nThe specified file extensions are {1} modified between {2} and {3}".format(
            path,
            variables.supported_extensions,
            variables.begin_time,
            variables.end_time,
        )
    )

    file_handle = utils.create_txt(variables.filtered_txt_name)
    file_count = sum(len(files) for _, _, files in os.walk(path))

    with tqdm(total=file_count) as pbar:
        for path, _, _ in os.walk(path):
            subdir = glob(os.path.join(path, "*.*"))
            for file in subdir:
                pbar.update(1)
                if (
                    os.path.isfile(file)
                    and file.endswith(variables.supported_extensions)
                    and utils.is_time_between(dt.strptime(
                        tm.ctime(os.path.getmtime(file)), "%a %b %d %H:%M:%S %Y"
                    ))
                    and utils.is_not_tmp(file)
                    and check.is_corrupted(file)
                ):
                    file_handle.write(file + "\n")
