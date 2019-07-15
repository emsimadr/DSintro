# %%
# Initialize dataframes
import pandas as pd
import numpy as np
path='G:\\My Drive\\Education\\Coursera\\Introduction to Data Science with Python\\DSIntro\\Assignment 3\\'

# Load Energy indicators from excel
Energy = (pd.read_excel(path + 'Energy Indicators.xls',
    skiprows=18,
    skipfooter=38,
    usecols = [2,3,4,5],
    names = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable'],
    na_values = ['...']))

# Convert Energy Supply to Gigajoules
Energy['Energy Supply'] = Energy['Energy Supply']*1000000

# Remove numbers from country name
Energy['Country'] = Energy['Country'].str.replace('\d+', '')

# Renaming Countris
Energy['Country'] = Energy['Country'].replace({
    'Republic of Korea' : 'South Korea',
    'United States of America' : 'United States',
    'United Kingdom of Great Britain and Northern Ireland' : 'United Kingdom',
    'China, Hong Kong Special Administrative Region' : 'Hong Kong',
    'Bolivia (Plurinational State of)' : 'Bolivia',
    'Venezuela (Bolivarian Republic of)' : 'Venezuela',
    'Iran (Islamic Republic of)' : 'Iran'
})

# Load gdp data from world_bank.csv
GDP = pd.read_csv(path + 'world_bank.csv',
    skiprows = 5,
    names = ['Country','Country Code','Indicator Name','Indicator Code','1960','1961','1962','1963','1964','1965','1966','1967','1968','1969','1970','1971','1972','1973','1974','1975','1976','1977','1978','1979','1980','1981','1982','1983','1984','1985','1986','1987','1988','1989','1990','1991','1992','1993','1994','1995','1996','1997','1998','1999','2000','2001','2002','2003','2004','2005','2006','2007','2008','2009','2010','2011','2012','2013','2014','2015','2016','2017','2018']
    )

# Rename countries
GDP['Country'] = GDP['Country'].replace( {
    'Korea, Rep.': 'South Korea',
    'Iran, Islamic Rep.': 'Iran',
    'Hong Kong SAR, China': 'Hong Kong'
})

# Load data from the Sciamago journal
ScimEn = pd.read_excel(path + 'scimagojr-3.xlsx')

# %%
# Answer One
def answer_one():
    # Sort by rank and return top 15 countries
    tmp_scim = ScimEn.sort_values('Rank').head(15)

    # Reduce GDP years to last 10
    tmp_GDP = GDP[['Country', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]

    # Intersections between all three data frames
    Top15 = pd.merge(pd.merge(tmp_scim, Energy, left_on='Country', right_on='Country',  how='inner'),
        tmp_GDP, left_on='Country', right_on='Country', how='inner')
    # Set index on Country
    Top15.set_index('Country',inplace=True)
    return Top15

# %%
# Answer Two
def answer_two():
    max_row_count = np.amin([Energy.shape[0], GDP.shape[0], ScimEn.shape[0]])
    return int(max_row_count - 15)
answer_two()

# %%
# Answer Three
def answer_three():
    Top15 = answer_one()
    avgGDP = Top15[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']].mean(axis=1).sort_values(ascending=False)
    return avgGDP
answer_three()

# %%
# Answer Four
def answer_four():
    AvgGDP = answer_three()
    Top15 = answer_one()
    return Top15.loc[AvgGDP.index[5]]['2015'] - Top15.loc[AvgGDP.index[5]]['2006']
answer_four()

# %%
# Answer Five
def answer_five():
    Top15 = answer_one()
    return float(Top15[['Energy Supply per Capita']].mean())
answer_five()

# %%
# Answer Six
def answer_six():
    Top15 = answer_one()
    top_renewable = Top15[Top15['% Renewable'] == Top15['% Renewable'].max()]
    return (top_renewable.index[0], top_renewable['% Renewable'])
answer_six()

# %%
# Answer Seven

# %%
# Answer Eight

# %%
# Answer Nine

# %%
# Answer Ten

# %%
# Answer Eleven

# %%
# Answer Twelve

# %%
# Answer Thirteen
