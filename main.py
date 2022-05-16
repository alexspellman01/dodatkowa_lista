import pandas as pd
dane = pd.read_csv("logs_converted.csv",header=None, skiprows=[0])
print(dane.head(10))





# cities.to_csv('cities.csv', index=False, sep=';')