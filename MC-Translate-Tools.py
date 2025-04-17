import json

print("请输入英文json文件名：")
en="en_us.json"
with open(en, 'r', encoding='UTF-8') as f:
    data_en = json.load(f)
keys_en = data_en.keys()
#print(keys_en)

print("请输入中文json文件名：")
zh="zh_cn.json"
with open(zh, 'r', encoding='UTF-8') as f:
    data_zh = json.load(f)
keys_zh = data_zh.keys()
#print(keys_zh)
for key in keys_en:
    if key in keys_zh:
        data_en[key] = data_zh[key]
        print(key + " 已合并")

# 保存修改后的JSON文件
with open(zh, 'w', encoding='UTF-8') as f:
    json.dump(data_en, f, indent=2,ensure_ascii=False)  # 确保把数据重新写入文件
