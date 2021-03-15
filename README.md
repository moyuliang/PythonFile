# PythonFile
主要是记录一些以python写的工作中用的小工具。

- **text_add_quote.py**：

  `text_add_quote_to_clipboard()`：将剪贴板中文本每行加上单引号并用逗号拼接，输出到剪贴板中。

  操作方法：

  1. 在Navicat拷贝了多行字符串
  2. 运行该方法
  3. 粘贴到Navicat查询语句

  `number_add_comma_to_clipboard()`：将剪贴板中每行内容用逗号拼接，输出到剪贴板。

  操作方法：

  1. 在Navicat拷贝了多行数字
  2. 运行该方法
  3. 粘贴到Navicat查询语句

  `text_add_quote_to_file(filename)`：将传入的文件中每行文本内容加单引号并以逗号拼接，输出到文件中。

  操作方法：

  1. 在input/id.txt中录入多行字符串并保存
  2. 运行该方法
  3. 查看生成的output/id_add_quote.txt文件

- **stitch_sql.py**：

  `stitch_sql(preparing, parameters)`：拼接debug日志中的sql并输出到剪贴板，入参1为参数化sql，入参2为参数

  操作方法：

  1. 运行该方法
  2. 在debug日志中复制Preparing后的参数化sql，例如：
     `select * from t_bus_user where id in (?,?) and create_time= ? and money = ? order by id limit ?`
  3. 粘贴到运行窗口，按下回车
  4. 在debug日志中复制Parameters后的参数，例如：
     `1(String), 2(String), 2021-03-01 00:00:00.0(Timestamp), 8569874(BigDecimal), 10(Integer)`
  5. 粘贴到运行窗口，按下回车
  6. 提示拼接完毕并放入剪贴板后，即可直接在Navicat中Ctrl+V粘贴使用

- **swagger2excel.py**：一个将剪贴板中swagger接口导出到Excel中的工具，生成文件output/api.xls

  操作方法：

  1. 浏览器地址栏拷贝swagger地址，如：https://xxx/swagger-ui.html
  2. 运行该程序
  3. 查看生成的output/api.xls文件
