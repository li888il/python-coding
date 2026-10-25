import json  # 导入标准库 json，用来处理 JSON 格式的数据

# 1. 准备数据：列表里套字典，每个字典代表一个学生
students = [
    {"name": "张三", "score": 88},
    {"name": "李四", "score": 92},
    {"name": "王五", "score": 75},
]

# 2. 写入文件
# open 打开文件，"w" 表示写入模式（文件不存在就新建，存在就覆盖）
# encoding="utf-8" 保证中文不乱码
# with ... as f 是固定写法，代码块结束后自动关闭文件，不用手动 close()
with open("grades.json", "w", encoding="utf-8") as f:
    # json.dump 把 Python 数据（students）写进文件对象 f
    # ensure_ascii=False 让中文正常显示，而不是变成 \u5f20\u4e09 这种转义码
    # indent=2 让文件内容缩进 2 个空格，方便阅读
    json.dump(students, f, ensure_ascii=False, indent=2)

# 3. 读回文件
# "r" 表示读取模式，打开刚才写好的 grades.json
with open("grades.json", "r", encoding="utf-8") as f:
    # json.load 把文件里的 JSON 文本转回 Python 列表，赋值给 loaded
    loaded = json.load(f)

# 4. 打印结果，确认读回来的数据和原数据一致
print(loaded)          # 应该是一个列表
print(type(loaded))    # 应该显示 <class 'list'>