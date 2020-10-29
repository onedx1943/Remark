CSV，它是一种以逗号分隔数值的文件类型。以纯文本形式存储表格数据（数字和文本）。在项目中我们经常需要读取CSV文件中数据。Python 标准库提供了读写 CSV 文件的库，名为 `csv`，使用 `csv` 可以轻松应对各种 CSV 格式。**本文将介绍使用 Python 的内置库解析 CSV 文件的方法。**



假设file.csv的文件中包含如下数据：

```csv
name,gender,age
'张三',男,33
'李四',男,34
'王二',男,27
'麻子',女,56
```

### 使用reader方法读取

```python
import csv

with open('file.csv', 'r', encoding='utf-8') as f:
    # 默认解析逗号分隔符
    reader = csv.reader(f, delimiter=',')
    print(type(reader))
    # 读取一行，单独获取标题行，下面的reader中已经没有该行了
    head = next(reader)
    print(head)

    for row in reader:
        print(row)

'''输出：
<class '_csv.reader'>
['name', 'gender', 'age']
["'张三'", '男', '33']
["'李四'", '男', '34']
["'王二'", '男', '27']
["'麻子'", '女', '56']
'''
```

每个row 是一个list数据类型。这样我们就可以对row使用list的诸多方法，如：切片、列表倒序、查找制定成员的索引等。

如果要访问特定的字段就需要使用对应的索引，如row[0]表示第一列的name。

但是这样使用索引非常容易混淆，所以我们可以使用另一种方式将数据读取为字典序列。

### 使用DictReader()方法读取

```python
import csv

with open('file.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    print(type(reader))

    for row in reader:
        print(row)

'''输出：
<class 'csv.DictReader'>
OrderedDict([('name', "'张三'"), ('gender', '男'), ('age', '33')])
OrderedDict([('name', "'李四'"), ('gender', '男'), ('age', '34')])
OrderedDict([('name', "'王二'"), ('gender', '男'), ('age', '27')])
OrderedDict([('name', "'麻子'"), ('gender', '女'), ('age', '56')])
'''
```

以字典的方式处理csv文件，实质上是以OrderedDict方式进行处理，默认情况下是将CSV文件的第一行作为字段名。这样就可以使用表头来轻松访问每行中的数据，如：row['name']。

如果 CSV 文件中没有指定字段名，则应通过将 fieldsnames 可选参数设置字典的键。

```python
import csv

with open('file.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f, fieldnames=['first', 'second', 'third'])
    print(type(reader))

    for row in reader:
        print(row)

'''输出：
<class 'csv.DictReader'>
OrderedDict([('first', 'name'), ('second', 'gender'), ('third', 'age')])
OrderedDict([('first', "'张三'"), ('second', '男'), ('third', '33')])
OrderedDict([('first', "'李四'"), ('second', '男'), ('third', '34')])
OrderedDict([('first', "'王二'"), ('second', '男'), ('third', '27')])
OrderedDict([('first', "'麻子'"), ('second', '女'), ('third', '56')])
'''
```



当然，要读写 CSV 文件，Python 的 csv 标准库并不是唯一的选择，也可以用 pandas 来读写 CSV 文件，**如果要分析大量数据，那么强烈建议使用 pandas**。

