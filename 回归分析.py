import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.api as sm

# 读取数据
df = pd.read_excel("C:/Users/Administrator/Desktop/总1.xlsx")

# 数据预处理
# 将Gender列转换为数值类型
df['Gender'] = df['Gender'].replace({'M': 1, 'F': 0})

# 计算各项之间的相关系数
correlation_matrix = df[['MVPA', 'high', 'TIRBH', 'MEAN']].corr()

# 绘制相关性热力图
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f", square=True)
plt.title('Correlation Matrix')
plt.show()

# 输出各项之间的相关系数
print("Correlation Matrix:")
print(correlation_matrix)

# 线性回归分析
# 准备数据
X = df[['high',  'TIRBH', 'MEAN']]
y = df['MVPA']

# 添加常数项
X = sm.add_constant(X)

# 建立线性回归模型
model = sm.OLS(y, X).fit()

# 输出系数、R^2分数和p值
print("\nResults:")
print("\nCoefficients:")
coefficients_df = pd.DataFrame({'Variable': X.columns, 'Coefficient': model.params.values})
print(coefficients_df)

print(f"\nR^2 Score: {model.rsquared}")

print("\nResult Table:")
result_table = pd.DataFrame({'Variable': X.columns, 
                             'Coefficient': model.params.values, 
                             'p-value': model.pvalues})
result_table['p-value'] = result_table['p-value'].apply(lambda x: '%.3f' % x)
print(result_table)
