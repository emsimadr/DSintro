# Part 1: Olympics data
# %%
import pandas as pd
path='G:\\My Drive\\Education\\Coursera\\Introduction to Data Science with Python\\DSintro\\Assignment 2\\'
df = pd.read_csv(path + 'olympics.csv', index_col=0, skiprows=1)

for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:'Gold'+col[4:]}, inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:'Silver'+col[4:]}, inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:'Bronze'+col[4:]}, inplace=True)
    if col[:1]=='№':
        df.rename(columns={col:'#'+col[1:]}, inplace=True)

names_ids = df.index.str.split('\s\(') # split the index by '('

df.index = names_ids.str[0] # the [0] element is the country name (new index)
df['ID'] = names_ids.str[1].str[:3] # the [1] element is the abbreviation or ID (take first 3 characters from that)

df = df.drop('Totals')
df.head()

# %%
# You should write your whole answer within the function provided. The autograder will call
# this function and compare the return value against the correct solution value
def answer_zero():
    # This function returns the row for Afghanistan, which is a Series object. The assignment
    # question description will tell you the general format the autograder is expecting
    return df.iloc[0]

# You can examine what your function returns by calling it in the cell. If you have questions
# about the assignment formats, check out the discussion forums for any FAQs
answer_zero()

# %%
df[df['# Summer'] == df['# Summer'].max()]

# %%
import numpy as np
tmp['diff'] = np.abs(df['# Summer'] - df['# Winter'])
tmp

# %%
def answer_three():
    df['relative diff'] = abs(df['# Summer'] - df['# Winter'])/df['Combined total']
    return df[df['relative diff'] == df['relative diff'].max()].index[0]

answer_three()

# %%
def answer_four():
    res = pd.Series(data=df.apply(lambda x: x['Gold.2']*3 + x['Silver.2']*3 + x['Bronze.2'], axis=1))
    return res
answer_four()

# Part 2: Census Data
# %%
census_df = pd.read_csv(path + 'census.csv')


# %%
def answer_five():
    county_cnt = census_df[census_df.SUMLEV ==50][['STNAME','SUMLEV']].copy()
    return county_cnt.groupby('STNAME').count()[['SUMLEV']].idxmax()
answer_five()

# %%
def answer_six():
    largest_counties = census_df[census_df.SUMLEV ==50][['STNAME','SUMLEV','CENSUS2010POP']].copy()
    return largest_counties.groupby('STNAME')['CENSUS2010POP'].apply(lambda x: x.nlargest(3).sum()).sort_values(ascending=False).head(3)
answer_six()

# %%
def answer_seven():
    pop_change = census_df[census_df.SUMLEV ==50][['CTYNAME','POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']].copy()
    pop_change.set_index('CTYNAME', inplace=True)
    pop_change['diff'] = pop_change.max(axis=1) - pop_change.min(axis=1)
    return pop_change['diff'].idxmax()
answer_seven()

# %%
def answer_eight():
    tmpdf = pd.DataFrame(index=census_df.index)
    tmpdf = census_df[(census_df['REGION'].isin([1,2])) & (census_df['POPESTIMATE2015'] > census_df['POPESTIMATE2014'])]
    return tmpdf[['STNAME','CTYNAME']][tmpdf['CTYNAME'].str.startswith('Washington')]
answer_eight()
