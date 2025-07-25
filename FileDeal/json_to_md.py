import json

# 读取 JSON 文件
with open('character.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

md_lines = []

# 遍历每个分类，生成 Markdown 内容
for category_obj in data:
    for category, content in category_obj.items():
        md_lines.append(f"\n## {category}")
        words = content.get('words', [])
        if words:
            md_lines.append("\n| 单词 | 音标 | 中文释义 |")
            md_lines.append("|------|------|----------|")
            for word in words:
                md_lines.append(f"| {word.get('word','')} | {word.get('phonetic','')} | {word.get('meaning','')} |")

# 写入 Markdown 文件
with open('../_includes/character_card.md', 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))
