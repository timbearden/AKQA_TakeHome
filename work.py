import pandas as pd
import numpy as np


def cleaning_data(df, dropna = True):
    clean_df = df.drop(['LastSaleDate', 'LOCATION', 'LONGITUDE', 'LATITUDE'], axis=1)
    clean_df['Age'] = 2014 - clean_df['YearBuilt']
    clean_df['HasGarage'] = clean_df.HasGarage.apply(lambda val: 1 if val == 'Garage' else 0)
    clean_df['SoldPrev'] = clean_df.SoldPrev.apply(lambda val: 1 if val == 'Y' else 0)
    clean_df['ShortSale'] = clean_df.ShortSale.apply(lambda val: 1 if val == 'Y' else 0)
    if dropna:
        clean_df.dropna(inplace = True)
    return clean_df





if __name__ == '__main__':
    df = pd.read_excel('AKQA_Dataset_Test.xlsx', sheetname='Twin Cities')
    zips = pd.read_excel('AKQA_Dataset_Test.xlsx', sheetname='Zips')

    df = cleaning_data(df, dropna = True)
