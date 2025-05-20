import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读取 CSV 文件
df = pd.read_csv('mm_change_summary.csv')

df['deletions'] = df['deletions'].abs()

# 创建一个新列 'total'，表示代码变更的总数
df['total'] = df['commits'] + df['insertions'] + df['deletions']

# 绘制趋势图
fig, ax = plt.subplots(figsize=(12, 8))

# 绘制单独数据趋势
ax.plot(df['range'], df['commits'], label='Commits', color='blue', marker='o')
ax.plot(df['range'], df['insertions'], label='Insertions', color='green', marker='o')
ax.plot(df['range'], df['deletions'], label='Deletions', color='red', marker='o')

# 绘制总趋势
ax.plot(df['range'], df['total'], label='Total', color='black', linestyle='--', linewidth=2, marker='x')

# 设置图表标题和标签
plt.title('Code Change Trends', fontsize=16)
ax.set_xlabel('Range', fontsize=12)
ax.set_ylabel('Number of Changes', fontsize=12)

# 添加图例
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# 旋转x轴标签以提高可读性
plt.xticks(rotation=45)

# 添加网格线以提高可读性
ax.grid(True, linestyle='--', alpha=0.7)

# 确保图表布局整洁
plt.tight_layout()

# 保存并显示图表
plt.savefig('Code Change Trends.png', dpi=300)
plt.show()