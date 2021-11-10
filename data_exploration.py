# Write code that explores your data set
import pandas as pd
import matplotlib.pyplot as plt
from data_preparation import explore_df


def create_dataframe(df, indicator):
    return df.loc[df['Indicator Name'] == indicator]


def create_bar(x, y, title, xlabel, ylabel, fname):
    plt.figure(figsize=(50,10))
    plt.bar(x, y)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.show()
    plt.savefig(fname)


if __name__ == '__main__':
    # reading file
    df = pd.read_csv("DBData_clean.csv")
    # explore_df(df)
    # countries = list(df['Country Name'].unique())
    indicators = ['Rank: Ease of doing business index (1=most business-friendly regulations)',
                  'Rank: Paying taxes (1=most business-friendly regulations)',
                  'Paying taxes: Profit tax (% of profits)',
                  'Global: Ease of doing business score (DB17-20 methodology)',
                  'Paying taxes (DB17-20 methodology) - Score']
    file_names = ['rank_ease_of_doing_business.png',
                  'rank_paying_taxes.png',
                  'paying_taxes.png',
                  'ease_of_doing_business_score.png',
                  'paying_taxes_score.png']

    df_business_ease_rank = create_dataframe(df, indicators[0])
    df_taxes_rank = create_dataframe(df, indicators[1])
    df_taxes = create_dataframe(df, indicators[2])
    df_business_ease = create_dataframe(df, indicators[3])
    df_taxes_score = create_dataframe(df, indicators[4])

    # uncomment below to explore dataframes
    # explore_df(df_business_ease_rank)
    # explore_df(df_taxes_rank)
    # explore_df(df_taxes)
    # explore_df(df_business_ease)
    # explore_df(df_taxes_score)

    countries = df_business_ease_rank['Country Code']
    create_bar(countries, df_business_ease_rank['2020'], 'Rank: Ease of Doing Business in 2020 by Country','Country',
               'Rank: Ease of Doing Business 2020', file_names[0])
    create_bar(countries, df_taxes_rank['2020'], 'Rank: Paying taxes (1=most business-friendly regulations)', 'Country',
               'Rank: Paying taxes', file_names[1])
