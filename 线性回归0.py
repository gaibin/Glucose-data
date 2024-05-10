import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据
df = pd.read_excel("C:/Users/Administrator/Desktop/总.xlsx")

# 设置色盲友好的颜色方案
blue_color = (0.12156862745098039, 0.4666666666666667, 0.7058823529411765)  # 深蓝色
orange_color = (1.0, 0.4980392156862745, 0.054901960784313725)  # 橙色

# 绘制散点图和线性回归线
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df, x='MVPA', y='TIRBH', color=blue_color, label='Data Points', s=100)
sns.regplot(data=df, x='MVPA', y='TIRBH', scatter=False, color=orange_color, line_kws={"linewidth": 2}, label='Regression Line')
sns.regplot(data=df, x='MVPA', y='TIRBH', scatter=False, color=orange_color, ci=95, line_kws={"linewidth": 2}, label='95% Confidence Interval')
plt.title('Linear Regression Analysis: MVPA vs TIRBH')
plt.xlabel('MVPA')
plt.ylabel('TIRBH')
plt.legend()
plt.grid(True)
plt.show()
