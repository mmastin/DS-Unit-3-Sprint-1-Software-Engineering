import numpy as np

def outlier_removal(data):
    quartile_1, quartile_3 = np.percentile(data, [25, 75])
    iqr = quartile_3 - quartile_1
    lower_bound = quartile_1 - (iqr * 1.5)
    upper_bound = quartile_3 + (iqr * 1.5)
    return np.where((data <  upper_bound | (data > lower_bound))

def split_dates(datetime):
    import pandas as pd
    df['year] = pd.datetime.year
    df['month'] = pd.datetime.month
    df['day'] = pd.datetime.day
    return df

