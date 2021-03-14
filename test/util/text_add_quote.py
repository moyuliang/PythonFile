# text_add_quote.py

import pyperclip
import numpy as np

"""将剪贴板中每行内容收尾加上单引号，并用逗号拼接，拷贝到剪贴板"""


def text_add_quote_to_clipboard():
    # 从剪贴板获取文本，以行分隔放入列表
    list = str(pyperclip.paste()).splitlines()

    # 拼接字符串，给每行加上引号并用逗号拼接
    ids = ""
    for i in range(len(list)):
        ids += "'" + list[i] + "'"
        if i != len(list) - 1:
            ids += ","

    # 将拼接好的字符串放入剪贴板
    pyperclip.copy(ids)

    print("text_add_quote_to_clipboard done！")


"""将剪贴板中每行内容用逗号拼接，拷贝到剪贴板"""


def number_add_comma_to_clipboard():
    # 从剪贴板获取文本，以行分隔放入列表
    list = str(pyperclip.paste()).splitlines()

    # 用逗号拼接文本
    ids = ",".join(list)

    # 将拼接好的字符串放入剪贴板
    pyperclip.copy(ids)

    print("number_add_comma_to_clipboard done！")


"""将id.txt文件中每行首尾加单引号，并用逗号拼接为一行，输出到id_add_quote.txt文件中"""


def text_add_quote_to_file(file_name):
    with open(file_name) as txt:
        # 读取文本文件时去掉换行符\n
        content = txt.read().splitlines()
        txt.close()

    # 转成数组
    lines = np.array(content)

    # 拼接成字符串
    ids = ""
    for i in range(lines.size):
        ids += "'" + lines[i] + "'"
        if i != lines.size - 1:
            ids += ","

    # 写入文件
    with open("../resource/output/id_add_quote.txt", "w") as write:
        write.write(ids)

    print("text_add_quote_to_file done！")


if __name__ == '__main__':
    number_add_comma_to_clipboard()
    # int_add_comma_to_clipboard()
    # text_add_quote_to_file("./resource/id.txt")

