# Part 1: Olympics data
# %%
import pandas as pd
import numpy as np
path='G:\\My Drive\\Education\\Coursera\\Introduction to Data Science with Python\\DSIntro\\Assignment 3\\'
df = (pd.read_excel(path + 'Energy Indicators.xls',
    skiprows=18,
    skipfooter=38,
    usecols = [2,3,4,5],
    names = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'],
    na_values = ['...']))

# Convert Energy Supply to Gigajoules
df['Energy Supply'] = df['Energy Supply']*1000000

# Remove numbers from country name
df['Country'] = df['Country'].str.replace('\d+', '')

# Renaming Countris
df['Country'] = df['Country'].replace({
    "Republic of Korea" : "South Korea",
    "United States of America" : "United States",
    "United Kingdom of Great Britain and Northern Ireland" : "United Kingdom",
    "China, Hong Kong Special Administrative Region" : "Hong Kong",
    "Bolivia (Plurinational State of)" : "Bolivia",
    "Venezuela (Bolivarian Republic of)" : "Venezuela"
})

print(df)
