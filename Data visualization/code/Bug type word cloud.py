import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# 读取 CSV 文件
df = pd.read_csv('bug_type_stats.csv')

# 创建词频字典
word_freq = dict(zip(df['Bug Type'], df['Count']))

# 创建词云对象
wordcloud = WordCloud(width=400, height=300, background_color='black', max_font_size=150, colormap='plasma')

# 生成词云
wordcloud.generate_from_frequencies(word_freq)

# 显示词云
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Bug fix type word cloud', fontsize=16)
plt.tight_layout()
plt.show()

# 保存词云
wordcloud.to_file('bug_type_wordcloud.png')