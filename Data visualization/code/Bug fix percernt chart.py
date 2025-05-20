import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取 CSV 文件
df = pd.read_csv('bug_type_stats_by_year.csv')

# 计算每行（每年）的总错误数，用于计算百分比
df['total'] = df['fix'] + df['bug'] + df['oops'] + df['crash'] + df['fault'] + df['leak']

# 计算每种错误类型的百分比
df['fix_percent'] = (df['fix'] / df['total'] * 100).round(2)
df['bug_percent'] = (df['bug'] / df['total'] * 100).round(2)
df['oops_percent'] = (df['oops'] / df['total'] * 100).round(2)
df['crash_percent'] = (df['crash'] / df['total'] * 100).round(2)
df['fault_percent'] = (df['fault'] / df['total'] * 100).round(2)
df['leak_percent'] = (df['leak'] / df['total'] * 100).round(2)

# 设置绘图参数
plt.style.use('seaborn-v0_8-whitegrid')
fig, ax1 = plt.subplots(figsize=(12, 8))

# 设置柱状图的位置和宽度
x = np.arange(len(df['Year']))
bar_width = 0.5  # 柱子宽度

# 绘制堆叠柱状图
bars1 = ax1.bar(x, df['fix_percent'], bar_width, label='Fix', color='b')
bars2 = ax1.bar(x, df['bug_percent'], bar_width, bottom=df['fix_percent'], label='Bug', color='g')
bars3 = ax1.bar(x, df['oops_percent'], bar_width, bottom=df['fix_percent'] + df['bug_percent'], label='Oops', color='r')
bars4 = ax1.bar(x, df['crash_percent'], bar_width, bottom=df['fix_percent'] + df['bug_percent'] + df['oops_percent'], label='Crash', color='c')
bars5 = ax1.bar(x, df['fault_percent'], bar_width, bottom=df['fix_percent'] + df['bug_percent'] + df['oops_percent'] + df['crash_percent'], label='Fault', color='m')
bars6 = ax1.bar(x, df['leak_percent'], bar_width, bottom=df['fix_percent'] + df['bug_percent'] + df['oops_percent'] + df['crash_percent'] + df['fault_percent'], label='Leak', color='y')

# 设置图表标题和标签
plt.title('Bug Type Percentage by Year', fontsize=16)
ax1.set_xlabel('Year', fontsize=12)
ax1.set_ylabel('Percentage (%)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(df['Year'])

# 添加图例
ax1.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# 旋转x轴标签以提高可读性
plt.xticks(rotation=45)

# 添加网格线
ax1.grid(True, linestyle='--', alpha=0.7)

# 确保图表布局整洁
plt.tight_layout()

# 保存并显示图表
plt.savefig('Bug Type Percentage by Year.png', dpi=300)
plt.show()