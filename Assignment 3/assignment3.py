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
answer_one()
# %%
# Answer Two
def answer_two():
    max_row_count = np.max([Energy.shape[0], GDP.shape[0], ScimEn.shape[0]])
    join_row_count = pd.merge(pd.merge(Energy, GDP), ScimEn, on='Country', how='inner').shape[0]
    return int(max_row_count - join_row_count)
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
def answer_seven():
    Top15 = answer_one()
    Top15['Citation Ratio'] = Top15['Self-citations'] / Top15['Citations']
    top_citation_ratio = Top15[Top15['Citation Ratio'] == Top15['Citation Ratio'].max()]
    return (top_citation_ratio.index[0], top_citation_ratio['Citation Ratio'])
answer_seven()

# %%
# Answer Eight
def answer_eight():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    return Top15.sort_values('Population', ascending = False).index[2]

answer_eight()

# %%
# Answer Nine
def answer_nine():
    Top15 = answer_one()
    Top15['Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15['Citable Documents per Capita'] = Top15['Citable documents'] / Top15['Population']
    return Top15[['Citable Documents per Capita','Energy Supply per Capita']].corr(method='pearson').iloc[0,1]

answer_nine()

# %%
# Answer Ten
def answer_ten():
    Top15 = answer_one()
    median = Top15['% Renewable'].median()
    Top15['Above Mean'] = [1 if x >= median else 0 for x in Top15['% Renewable']]
    return Top15['Above Mean']
answer_ten()

# %%
# Answer Eleven
def answer_eleven():
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}

    Top15['Continent'] = [ContinentDict[country] for country in Top15.index]
    Top15['Population'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']

    df = Top15.set_index('Continent').groupby(level=0)['Population'].agg({
        'size' : np.size,
        'sum' : np.sum,
        'mean' : np.mean,
        'std' : np.std
    })
    return df
answer_eleven()

# %%
# Answer Twelve
def answer_twelve():
    Top15 = answer_one()
    ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}

    Top15['Continent'] = [ContinentDict[country] for country in Top15.index]
    Top15['Bin'] = pd.cut(Top15['% Renewable'], 5)

    return Top15.groupby(['Continent', 'Bin']).size()
answer_twelve()

# %%
# Answer Thirteen
def answer_thirteen():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    return Top15['PopEst'].map('{:20,.2f}'.format)

answer_thirteen()

# %%
def plot_optional():
    import matplotlib as plt
    %matplotlib inline
    Top15 = answer_one()
    ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter',
                    c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
                       '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'],
                    xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);

    for i, txt in enumerate(Top15.index):
        ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')

    print("This is an example of a visualization that can be created to help understand the data. \
This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' \
2014 GDP, and the color corresponds to the continent.")
