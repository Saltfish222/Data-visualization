import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取 CSV 文件
df = pd.read_csv('mm_change_summary.csv')

# 将 deletions 列取绝对值
df['deletions'] = df['deletions'].abs()

# 计算每行的总和，用于计算百分比
df['total'] = df['commits'] + df['insertions'] + df['deletions']

# 计算每个分类的百分比
df['commit_percent'] = (df['commits'] / df['total'] * 100).round(2)
df['insert_percent'] = (df['insertions'] / df['total'] * 100).round(2)
df['delete_percent'] = (df['deletions'] / df['total'] * 100).round(2)

# 绘制堆叠柱状图
fig, ax1 = plt.subplots(figsize=(12, 8))

# 设置柱状图的位置和宽度
x = np.arange(len(df['range']))
bar_width = 0.5

# 绘制堆叠柱状图，使用百分比
bars1 = ax1.bar(x, df['commit_percent'], bar_width, label='Commits', color='b')
bars2 = ax1.bar(x, df['insert_percent'], bar_width, bottom=df['commit_percent'], label='Insertions', color='g')
bars3 = ax1.bar(x, df['delete_percent'], bar_width, bottom=df['commit_percent'] + df['insert_percent'], label='Deletions', color='r')

# 设置图表标题和标签
plt.title('Code change percentage', fontsize=16)
ax1.set_xlabel('range', fontsize=12)
ax1.set_ylabel('Percentage (%)', fontsize=12)
ax1.set_xticks(x)
ax1.set_xticklabels(df['range'])

# 添加图例
ax1.legend([bars1, bars2, bars3], ['Commits', 'Insertions', 'Deletions'], bbox_to_anchor=(1.05, 1), loc='upper left')

# 显示图表
plt.tight_layout()
plt.savefig('Code change percentage.png', dpi=300)
plt.show()