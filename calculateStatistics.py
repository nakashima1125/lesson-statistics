"""
基本統計量を求める。以下の数値を算出する式を書く。
- 平均
- 代表値
- 分散
- 標準偏差
"""
import numpy as np

np.random.seed(0)
x = np.random.rand(50) # 0.0 ~ 1.0

# 平均
cal_mean = np.sum(x) / x.shape[0] # スカラーで取り出す。
fact_mean = np.mean(x)

print(np.allclose(cal_mean ,fact_mean))



