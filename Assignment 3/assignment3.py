# Part 1: Olympics data
# %%
import pandas as pd
import numpy as np
path='G:\\My Drive\\Education\\Coursera\\Introduction to Data Science with Python\\DSIntro\\Assignment 3\\'
df = (pd.read_excel(path + 'Energy Indicators.xls',
    skiprows=18,
    skipfooter=38,
    usecols = [2,3,4,5],
    names = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']))

# Convert Energy Supply to Gigajoules
df['Energy Supply'] = df['Energy Supply']*1000000
df.replace('...', np.NaN)

# for col in df.columns:
#     if col[:2]=='01':
#         df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
#     if col[:2]=='02':
#         df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
#     if col[:2]=='03':
#         df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
#     if col[:1]=='№':
#         df.rename(columns={col:'#'+col[1:]}, inplace=True)
#
# names_ids = df.index.str.split('\s\(') # split the index by '('
#
# df.index = names_ids.str[0] # the [0] element is the country name (new index)
# df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)
#
# df = df.drop('Totals')
df.head()
