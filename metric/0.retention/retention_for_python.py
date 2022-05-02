import pandas as pd
import numpy as np
import matplotlib as plt


"""
0. 데이터 확인
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
(data.groupby(['datetime_to_date'])['product_id']\
    .nunique().reset_index().plot(x='datetime_to_date', y='product_id'))

"""
1. 리텐션 계산
"""




