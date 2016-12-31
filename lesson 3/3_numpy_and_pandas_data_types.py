import numpy as np
import pandas as pd

print np.array([1, 2, 3, 4, 5]).dtype

enrollments = np.array([
    ['account_key', 'status', 'join_date', 'days_to_cancel', 'is_udacity'],
    [448, 'canceled', '2014-11-10', 65, True],
    [448, 'canceled', '2014-11-05', 5, True],
    [448, 'canceled', '2015-01-27', 0, True],
    [448, 'canceled', '2014-11-10', 0, True],
    [448, 'current', '2015-03-10', np.nan, True]
])

print enrollments

print enrollments[:, 3]

# print enrollments[:, 3].mean() doesn't work

enrollments_df = pd.DataFrame({
    'account_key': [448, 448, 448, 448, 448],
    'status': ['canceled', 'canceled', 'canceled', 'canceled', 'current'],
    'join_date': ['2014-11-10', '2014-11-05', '2015-01-27', '2014-11-10', '2015-03-10'],
    'days_to_cancel': [65, 5, 0, 0, np.nan],
    'is_udacity': [True, True, True, True, True]
})

print enrollments_df

print enrollments_df.mean()

print enrollments_df.mean(axis=1)
