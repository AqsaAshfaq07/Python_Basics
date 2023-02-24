import pandas as pd
data = pd.read_csv('iris.csv')
df = pd.DataFrame(data)

print(df)
print(data.size)
print(data.describe())
print(data.info())

# Class Task
print(data.dtypes)
print(data.tail())
print(data.head())
print(pd.set_option('display.max_rows', None)) #multiple parameters can be passes...find more in pandas documentation
print(data.shape) #returns no. of columns, no. of rows
print(data.index) #returns indices range ,, start, stop, step
df_reName = data.rename(columns={'5.1': 'Title'})
print(df)
print(df_reName)
rePlace = data.replace({'3.5': {3.0: 10.0}}, inplace=False) #replaces values of a column ,, inplace=True --> changes value in the original dataframe object
print(rePlace)
