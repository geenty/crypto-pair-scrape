"""
Take raw data files with pricing over time and clean them into dataframes
for consumption.

Author: Jon Geenty

"""
import pandas as pd
import ast
import os


DATA_LOC = 'data/'
OUT_LOC = 'clean_data/'
pair_names = os.listdir("data")

for i in pair_names:
    item = i
    pair = item[:-9]
    print("getting " + item)

    filename = DATA_LOC+ item
    file_data = open(filename, 'r')

    with open(filename, 'r') as myfile:
        data=myfile.read().replace('\n', '')

    data = data[3:]
    data = data[:-2]
    data_dict = ast.literal_eval(data)

    df = pd.DataFrame(list(data_dict),index=None)

    df.to_csv(OUT_LOC + pair + '.csv', index=False, encoding='utf-8')
    print("saved " + item + 'data as dataframe')
