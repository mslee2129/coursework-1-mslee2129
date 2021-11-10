# Write code that prepares your data
import pandas as pd


# function to explore the datasets
def explore_df(df):
    print(df.shape)
    print(df.head(5))
    print(df.columns)
    print(df.info(verbose=True))


# function to keep only the countries listed in DBCountry.csv
def country_filter(df1, df2):
    country_codes = df2['Country Code']
    country_list = list(country_codes)
    df = df1[df1['Country Code'].isin(country_list)]
    return df


# function to filter out unnecessary indicators
def indicator_filter(df1):
    # filtering the indicators to keep out of the 205 indicators
    indicators_list = ['Rank: Ease of doing business index (1=most business-friendly regulations)',
                       'Rank: Paying taxes (1=most business-friendly regulations)',
                       'Paying taxes: Profit tax (% of profits)',
                       'Global: Ease of doing business score (DB17-20 methodology)',
                       'Paying taxes (DB17-20 methodology) - Score']
    df = df1[df1['Indicator Name'].isin(indicators_list)]
    return df


if __name__ == '__main__':
    df_data = pd.read_csv("DBData.csv")
    df_country = pd.read_csv("DBCountry.csv")

    # uncomment below to explore uncleaned datasets
    explore_df(df_data)
    explore_df(df_country)

    df_data = country_filter(df_data, df_country)
    df_data = indicator_filter(df_data)

    # only keeping recent data due to inconsistencies in older data
    df_data.drop(df_data.columns.difference(['Country Name', 'Country Code', 'Indicator Name', 'Indicator Code',
                                             '2016', '2017', '2018', '2019', '2020']), axis=1, inplace=True)

    print(df_data.shape)
    print(df_data.head(10))

    # df_data.to_csv("DBData_clean.csv")
