# swagger2excel.py

"""将剪贴板中的swagger接口导出到excel"""

import xlwt, requests, json, pyperclip

# 从剪贴板中获取swagger-ui地址，处理为api-doc接口
url = str(pyperclip.paste())
url = url.replace('swagger-ui.html', 'v2/api-docs')

r = requests.get(url)
# 获取访问的host和basePath
basePath = str(json.loads(r.text)['host'] + json.loads(r.text)['basePath'])[0, -1]

# 获取所有的uri
paths = json.loads(r.text)['paths']

# 新建excel
xls = xlwt.Workbook()

# 添加sheet并设置sheet名
sht1 = xls.add_sheet("API")

# 设置标题行内容
sht1.write(0, 0, 'url')
sht1.write(0, 1, 'uri')
sht1.write(0, 2, 'method')
sht1.write(0, 3, 'tags')
sht1.write(0, 4, 'summary')
sht1.write(0, 5, 'parameters')

# excel行数
i = 1

# 遍历需要的key和value，写入excel
for key in paths.keys():
    sht1.write(i, 0, basePath + str(key))
    sht1.write(i, 1, key)
    for key1 in paths[key].keys():
        sht1.write(i, 2, key1)
        for key2, value in paths[key][key1].items():
            if key2 == 'tags':
                sht1.write(i, 3, str(value)[2:-2])
            if key2 == 'summary':
                sht1.write(i, 4, str(value))
            if key2 == 'parameters':
                sht1.write(i, 5, str(value))
        i += 1

# 保存excel
xls.save('../resource/output/api.xls')

print("swagger ui export to excel done")
