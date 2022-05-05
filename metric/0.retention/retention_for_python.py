import pandas as pd
import numpy as np
import matplotlib as plt


"""
0. Rolling_retention
상품 구매와 같이, 주기성이 떨어지는 경우
DayN_Retention보다는 Rolling Retention이 적합함
"""


# 데이터 호출
data = pd.read_excel("metric/0.retention/KPMG_VI_New_raw_data_update_final.xlsx", sheet_name='Transactions', skiprows=[0])
print(data.head())

# 데이터 타입 확인
data.info()

# 집계 시작일 집계 종료일
print(f'First date is {data.transaction_date.min()} and Last date is {data.transaction_date.max()}')

# datetime을 date로 변경
data['datetime_to_date'] = pd.to_datetime(data['transaction_date']).dt.date
print(f'First date is {data.datetime_to_date.min()} and Last date is {data.datetime_to_date.max()}')

# 일자별 고객수 확인
data.groupby(['datetime_to_date'])['customer_id'].nunique().reset_index().plot(x='datetime_to_date', y='customer_id')
(data.groupby(['datetime_to_date'])['product_id']
    .nunique().reset_index().plot(x='datetime_to_date', y='product_id'))

# distinct customer_id and datetime_to_date
dayN_retention = (data[['customer_id', 'datetime_to_date']].drop_duplicates()
                            .sort_values(['customer_id', 'datetime_to_date'], ascending=[True, True]))
dayN_retention['shift_date'] = dayN_retention.groupby(['customer_id'])['datetime_to_date'].shift(1)
dayN_retention.head(20)

dayN_retention.loc[:, ['datetime_to_date', 'shift_date']] = (dayN_retention.loc[:, ['datetime_to_date', 'shift_date']].
                                                              apply(pd.to_datetime, errors='coerce'))

# type 확인 dtypes
dayN_retention.dtypes

# datediff between original_date and shift_date
dayN_retention['diff_day'] = (((dayN_retention['datetime_to_date'] - dayN_retention['shift_date'])\
                             / np.timedelta64(1, 'D')).fillna(0))

dayN_retention.head()
