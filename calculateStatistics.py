"""
基本統計量を求める。以下の数値を算出する式を書く。
行列演算ではなくfor文章を用いること。
- 平均
- 分散
- 標準偏差
"""
import numpy as np

np.random.seed(0)
x = np.random.rand(50) # 0.0 ~ 1.0

# 平均
cal_mean = np.sum(x) / x.shape[0] # スカラーで取り出す。
fact_mean = np.mean(x)
print("平均 : ", np.allclose(cal_mean ,fact_mean))


# 分散
tmp = 0
for i in range(x.shape[0]):
    tmp += (np.mean(x) - x[i]) **2
cal_variance = tmp / x.shape[0]
fact_variance = np.var(x)
print("分散 : ", np.allclose(cal_variance ,fact_variance))


# 標準偏差
tmp = 0
for i in range(x.shape[0]):
    tmp += (np.mean(x) - x[i]) **2
cal_stdev = np.sqrt(tmp / x.shape[0])
fact_stdev = np.std(x)
print("標準偏差 : ", np.allclose(cal_stdev ,fact_stdev))


