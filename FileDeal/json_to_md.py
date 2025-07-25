import json

# 读取 JSON 文件
with open('./word_card.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

md_lines = []

# 遍历每个分类，生成 Markdown 内容
for category_obj in data:
    for category, units in category_obj.items():
        md_lines.append(f"\n## {category}")
        for unit, unit_content in units.items():
            md_lines.append(f"\n### {unit}")
            md_lines.append("\n| 单词 | 音标 | 中文释义 |")
            md_lines.append("|------|------|----------|")
            for word in unit_content['words']:
                md_lines.append(f"| {word['word']} | {word['phonetic']} | {word['meaning']} |")

# 写入 Markdown 文件
with open('../_includes/word_card.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))
