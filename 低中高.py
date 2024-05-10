import pandas as pd
import matplotlib.pyplot as plt
import scipy.stats as stats
from scipy.interpolate import UnivariateSpline

# 读取数据
data = pd.read_excel('C:/Users/Administrator/Desktop/combined_data.xlsx')

# 剔除血糖值大于12的数据
data = data[data['Glucose'] <= 18]

# 将 'Time' 列的数据类型转换为数值类型
data['Time'] = data['Time'].str.replace('min', '').astype(int)

# 按照 'Time' 和 'Intensity' 对 'Glucose' 进行分组，并计算每组的平均值和标准差
grouped_data = data.groupby(['Time', 'Intensity'])['Glucose'].agg(['mean', 'std']).reset_index()

# 按照 'Time' 和 'Intensity' 对数据进行排序
grouped_data = grouped_data.sort_values(['Time', 'Intensity'])

# 定义颜色，根据图片中的颜色进行匹配
colors = {'Low': '#FFA07A', 'Mid': '#87CEFA', 'High': '#FFD700'}  # 橙色、蓝色、黄色
light_colors = {'Low': '#FFDAB9', 'Mid': '#B0E0E6', 'High': '#FFFACD'}  # 淡橙色、淡蓝色、淡黄色

# 创建图形
plt.figure(figsize=(10, 6))

# 对每个运动强度，绘制平均血糖值的线图，并添加标准差范围
for intensity in grouped_data['Intensity'].unique():
    subset = grouped_data[grouped_data['Intensity'] == intensity]
    x = subset['Time']
    y = subset['mean']
    std = subset['std'] - 2  # 减去2
    # 使用UnivariateSpline进行平滑
    spl = UnivariateSpline(x, y, s=0.5)  # s是平滑因子
    plt.plot(x, spl(x), color=colors[intensity], label=intensity)
    plt.fill_between(x, spl(x) - std, spl(x) + std, color=light_colors[intensity], alpha=0.3)

# 设置图形的标题和标签
plt.xlabel('时间（分钟）')
plt.ylabel('血糖值')
plt.legend(title='运动强度')
plt.title('不同运动强度下的血糖曲线')

# 显示图形
plt.show()
