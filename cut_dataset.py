# 打开你的原始数据文件
with open('dataset0.txt', 'r', encoding='utf-8') as f:
    paragraphs = f.read().split('\t')  # 这里我们直接读取全部内容，并按制表符分割成段落

# 初始化一个空列表来保存满足条件的段落
filtered_paragraphs = []

# 设置最多保留的段落数量
max_paragraphs = 650000

# 遍历原始数据文件中的每一个段落
for paragraph in paragraphs:
    # 如果段落的长度不超过500个字符，那么保留
    if len(paragraph) <= 500:
        filtered_paragraphs.append(paragraph)
        # 如果已经达到最多保留的段落数量，则停止遍历
        if len(filtered_paragraphs) >= max_paragraphs:
            break

# 将过滤后的段落合并为一个字符串，段落之间用制表符隔开
filtered_text = '\t'.join(filtered_paragraphs)

# 写入新的文本文件
with open('dataset.txt', 'w', encoding='utf-8') as f:
    f.write(filtered_text)
