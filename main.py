import pandas as pd
df = pd.read_csv('employee.csv')
print(df)

import pandas as pd
df = pd.read_excel('Sales.xlsx')

df = pd.read_csv('./data/TCB_2018_2020.csv')
print(df)

df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
print(df.head())

df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
# Export data with the condition that the closing price is greater than 98
print(df[df['Close']>98])
print(df[["High", "Low"]].tail())
df = pd.read_csv('./data/TCB_2018_2020.csv', header=None)
print(df[[0, 2, 3]].tail())

df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
print(df.loc['2020-06-15'])

df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
print(df.loc[['2019-06-10', '2020-06-10']])

df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
print(df.iloc[0]) # Get the first row

df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
print(df.iloc[[0, 2]]) # Get multiple records

df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
print(df.iloc[35:41]) # Get multiple consecutive records

df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
# Retrieve closing price on 20-08-2019
print(df.loc['2019-08-20', 'Close'])
print(df.loc['2020-12-25':, 'Open'])

df = pd.read_csv('./data/TCB_2018_2020.csv', index_col=0)
# Retrieve the 5th row and first column
print(df.iloc[4, 0])

# Retrieve rows from row 648 with all columns
print(df.iloc[648:, :])



