import pandas as pd

engagement_df = pd.DataFrame({
    'account_key': ['1200', '1200', '1200', '1200', '1200',
                    '1200', '1200', '1175', '1175', '1175',
                    '1175', '1175', '1175', '1175'],
    'utc_date':['2015-03-04', '2015-03-05', '2015-03-06', '2015-03-07',
                '2015-03-08', '2015-03-09', '2015-03-10', '2015-04-02',
                '2015-04-03', '2015-04-04', '2015-04-05', '2015-04-06',
                '2015-04-07', '2015-04-08'],
    'total_minutes_visited': [114.9, 43.4, 187.8, 150.1, 191.6, 0, 8.8,
                              2.7, 0, 0, 0, 0, 0, 0]
})

print engagement_df.groupby('account_key').sum()['total_minutes_visited'].mean()
    
print engagement_df.groupby('account_key').groups

print engagement_df.groupby('account_key').sum()['total_minutes_visited'].describe()

