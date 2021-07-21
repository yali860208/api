import pandas as pd

pd.set_option('display.max_columns', None)
pd.options.mode.chained_assignment = None
df = pd.read_csv('output.csv')
d = df.iloc[:, lambda df: [5, 19, 18, 7, 15, 9, 10, 21]]

d.to_csv('data.csv', index=True)