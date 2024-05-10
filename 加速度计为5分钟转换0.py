import os
import pampro

# 获取桌面路径
desktop_path = os.path.expanduser("C:/Users/Administrator/Desktop/1.csv")

# 构建数据文件的完整路径
data_file = os.path.join(desktop_path, "1.csv")

# 读取数据文件
data = pampro.read_data(data_file)

# 处理数据
processed_data = pampro.process_data(data)

# 生成处理后的数据文件路径
output_file = os.path.join(desktop_path, "processed_data.csv")

# 将处理后的数据保存为CSV文件
processed_data.to_csv(output_file, index=False)

print("处理后的数据已保存在桌面上的 processed_data.csv 文件中。")
