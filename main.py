from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder
from pathlib import Path
import numpy as np
import polars as pl
import sys

FILE_PATH = ""
file_name = ""


# read datasets -- assuming they are all execel files
def read_file_into_memory(file: str | list):
    if type(file) is list:
        n = 0
        for i in file:
            if Path(f"{i}").exists():
                try:
                    globals()[f"file_{n}"] = pl.read_excel(i)
                    n += 1
                except Exception as e:
                    raise e
            else:
                raise FileNotFoundError
    else:
        if not Path(f"{file}").exists():
            raise FileNotFoundError
        else:
            try:
                globals()[file_name] = pl.read_excel(file)
            except Exception as e:
                raise e


# perform data processing


# def main():
#     pass


if __name__ == "__main__":
    read_file_into_memory(sys.argv[1])
