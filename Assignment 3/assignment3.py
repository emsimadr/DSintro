# Part 1: Olympics data
# %%
import pandas as pd
import numpy as np
path='G:\\My Drive\\Education\\Coursera\\Introduction to Data Science with Python\\DSIntro\\Assignment 3\\'

# Load energy indicators from excel
df_energy = (pd.read_excel(path + 'Energy Indicators.xls',
    skiprows=18,
    skipfooter=38,
    usecols = [2,3,4,5],
    names = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'],
    na_values = ['...']))

# Convert Energy Supply to Gigajoules
df_energy['Energy Supply'] = df_energy['Energy Supply']*1000000

# Remove numbers from country name
df_energy['Country'] = df_energy['Country'].str.replace('\d+', '')

# Renaming Countris
df_energy['Country'] = df_energy['Country'].replace({
    'Republic of Korea' : 'South Korea',
    'United States of America' : 'United States',
    'United Kingdom of Great Britain and Northern Ireland' : 'United Kingdom',
    'China, Hong Kong Special Administrative Region' : 'Hong Kong',
    'Bolivia (Plurinational State of)' : 'Bolivia',
    'Venezuela (Bolivarian Republic of)' : 'Venezuela'
})

# %%
# Load gdp data from world_bank.csv
df_gdp = pd.read_csv(path + 'world_bank.csv',
    skiprows = 5,
    names = ['Country','Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
    )

# Rename countries
df_gdp['Country'] = df_gdp['Country'].replace( {
    'Korea, Rep.': 'South Korea',
    'Iran, Islamic Rep.': 'Iran',
    'Hong Kong SAR, China': 'Hong Kong'
})
