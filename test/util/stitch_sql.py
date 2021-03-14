# stitch_sql.py

import re, pyperclip

"""拼接debug日志中的sql并输出到剪贴板,入参1为参数化sql,入参2为参数"""


def stitch_sql(preparing, parameters):

    # 数字类型列表，存放不需要加单引号的Java类型
    typelist = ["BigDecimal", "Integer", "Byte", "Short", "Long", "Float", "Double"]

    # 将参数用逗号空格分隔
    lists = parameters.split(", ")

    # 处理参数
    for i in range(len(lists)):
        # 如果参数末尾的数据类型不在数字类型列表中，则去掉类型并加上单引号
        try:
            if str(lists[i]).lower() == "null":
                continue;
            elif str(re.search(r'''\((\w*)\)$''', lists[i]).group(1)).lower() not in [type1.lower() for type1 in
                                                                                      typelist]:
                lists[i] = "'" + re.sub(r'''\((\w*)\)$''', "", lists[i]) + "'"
            else:
                # 否则仅去掉数据类型
                lists[i] = re.sub(r'''\((\w*)\)$''', "", lists[i])
        except AttributeError as e:
            print(e)
            i += 1

    # 将参数化sql用问号分隔
    lists1 = preparing.split("?")

    # 声明sql用于存放拼接后的sql
    sql = ""

    # 拼接sql
    for i in range(len(lists)):
        if i == len(lists) - 1:
            sql += lists1[i] + lists[i] + lists1[i + 1]
            break
        sql += lists1[i] + lists[i]

    print("拼接结果：\n" + sql)

    # 将拼接后的sql放入剪贴板
    pyperclip.copy(sql)

    print("sql拼接完毕并放入剪贴板，请直接粘贴使用")


if __name__ == '__main__':
    # preparing = "select * from t_bus_user where id in (?,?) and create_time= ? and money = ? order by id limit ?"
    # parameters = "1(String), 2(String), 2021-03-01 00:00:00.0(Timestamp), 8569874(BigDecimal), 10(Integer)"

    print(
        "1. 请输入debug日志中的Preparing:后的参数化sql，例如：select * from t_bus_user where id in (?,?) and create_time= ? and money "
        "= ? order by id limit ?   按回车结束")
    preparing = input()

    print("2. 请输入debug日志中的Parameters:后的参数，例如：1(String), 2(String), 2021-03-01 00:00:00.0(Timestamp), "
          "8569874(BigDecimal), 10(Integer)    按回车结束")
    parameters = input()

    stitch_sql(preparing, parameters)
