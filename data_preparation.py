# Write code that prepares your data
import pandas as pd

# exploring DBData.csv file
df_data = pd.read_csv("DBData.csv")
print(df_data.head(5))
print(df_data.columns)

# exploring DBCountry.csv file
df_country = pd.read_csv("DBCountry.csv")
print(df_country.head(5))
print(df_country.columns)

