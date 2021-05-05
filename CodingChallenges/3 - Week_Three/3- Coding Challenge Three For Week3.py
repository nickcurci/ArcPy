import pandas as pd 
  
# creating a data frame 
df = pd.read_csv("hawaii.csv") 
print(df)

df['year'] = pd.DatetimeIndex(df['date']).year
df['month'] = pd.DatetimeIndex(df['date']).month
print(df)



dfy = df.groupby(['year'])['value'].mean()
print(dfy)



ind = df['value'].idxmin()
df.iloc[ind,:]




ind = df['value'].idxmax()
df.iloc[ind,:]



meanval = df['value'].mean()
print('the mean value is: ', meanval)
print(df)



df.loc[df['month'] == 1, 'month'] = 'winter'
df.loc[df['month'] == 2, 'month'] = 'winter'
df.loc[df['month'] == 3, 'month'] = 'spring'
df.loc[df['month'] == 4, 'month'] = 'spring'
df.loc[df['month'] == 5, 'month'] = 'spring'
df.loc[df['month'] == 6, 'month'] = 'summer'
df.loc[df['month'] == 7, 'month'] = 'summer'
df.loc[df['month'] == 8, 'month'] = 'summer'
df.loc[df['month'] == 9, 'month'] = 'fall'
df.loc[df['month'] == 10, 'month'] = 'fall'
df.loc[df['month'] == 11, 'month'] = 'fall'
df.loc[df['month'] == 12, 'month'] = 'winter'
print(df)


dfm = df.groupby(['month'])['value'].mean()
print(dfm)
