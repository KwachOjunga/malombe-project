from sklearn.preprocessing import OneHotEncoder, LabelEncoder, OrdinalEncoder
import numpy as np
import polars as pl

FILE_PATH = ""

# read datasets -- assuming they are all execel files
def read_file_into_memory(file: str|list):
    if type(file) == list:
        n = 0 
        for i in file:
            if os.path.exists(i):
                try:
                   file_[n] =  pl.read_excel(i)
                   n += 1 
                except Exception as e:
                   raise e
    else:
        try:
            file_name = pl.read_excel(file)
        except:
            raise Exception

# perform data processing



def main():
    


if __name__ == "__main__":
    main()
