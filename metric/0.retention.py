import pandas as pd
import numpy as np

"""
리텐션 계산 방법을 다뤄봅니다.
"""

"""
0. 우선 데이터를 불러봅시다.
"""

data = pd.read_excel("metric/data/KPMG_VI_New_raw_data_update_final.xlsx", sheet_name='Transactions', skiprows=[0])
data.head()