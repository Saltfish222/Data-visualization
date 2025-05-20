import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取 CSV 文件
df = pd.read_csv('bug_type_stats_by_year.csv')

# 创建一个新列 'total'，表示错误变更的总数
df['total'] = df['fix'] + df['bug'] + df['oops'] + df['crash'] + df['fault'] + df['leak']

# 绘制趋势图
fig, ax = plt.subplots(figsize=(12, 8))

# 绘制单独数据趋势
ax.plot(df['Year'], df['fix'], label='Fix', color='blue', marker='o')
ax.plot(df['Year'], df['bug'], label='Bug', color='green', marker='o')
ax.plot(df['Year'], df['oops'], label='Oops', color='red', marker='o')
ax.plot(df['Year'], df['crash'], label='Crash', color='cyan', marker='o')
ax.plot(df['Year'], df['fault'], label='Fault', color='magenta', marker='o')
ax.plot(df['Year'], df['leak'], label='Leak', color='yellow', marker='o')

# 绘制总趋势
ax.plot(df['Year'], df['total'], label='Total', color='black', linestyle='--', linewidth=2, marker='x')

# 设置图表标题和标签
plt.title('Bug Fix Trends', fontsize=16)
ax.set_xlabel('Year', fontsize=12)
ax.set_ylabel('Count', fontsize=12)

# 添加图例
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# 旋转x轴标签以提高可读性
plt.xticks(rotation=45)

# 添加网格线以提高可读性
ax.grid(True, linestyle='--', alpha=0.7)

# 确保图表布局整洁
plt.tight_layout()

# 保存并显示图表
plt.savefig('Bug Fix Trends.png', dpi=300)
plt.show()