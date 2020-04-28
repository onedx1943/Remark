【python】通过关键字对列表进行分组聚类



## 一、问题背景

在Dolphin数据收集功能中，按维度查看功能使用情况时，在后台需要对数据库查询出的数据进行分组聚类。比如功能维度，需要对功能和模块进行分组并计算对应总次数，版本维度则需要对版本分组计算。



## 二、解决方案

1. 多值字典分组

   创建一个字典将需要分组的关键字作为键，对应的数据实例添加到该键映射的列表中。可以使用 `collections` 模块中的 `defaultdict` 来构造这样的字典。然后再遍历字典计算分组后的内容。

   ```python
   from collections import defaultdict
   data_list = Models.objects.filter()
   data_dict = defaultdict(list)
   for data in data_list:
       data_dict[data['version']].append(data)
   ```
   
可以看出，此处根据关键值内容
   
   
   
2. groupby分组

   `groupby()` 把迭代器中相邻的重复元素分为一组。

   分组的规则是通过函数完成的，只要作用于函数的两个元素返回的值相等，这两个元素就被分为同一组，而分组的key则是函数的返回值。

   同时因为 `groupby()` 是检查相邻元素进行分组，所以在分组前需要对其进行排序。

   ```python
   from operator import itemgetter
   from itertools import groupby
   # itemgetter效果等同于使用lambda函数，但是性能较优一点。
   rows.sort(key=itemgetter('display_name', 'function_name'))
   for key, items in groupby(rows, key=itemgetter('display_name', 'function_name')):
       # key itemgetter传入多个索引参数时返回一个包含所有元素值的元组
       # items 包含该分组下所有元素的一个迭代器对象
       for i in items:
           print(i)
   ```

   hahah



## 三、结论

对比这两种分组方式，第一种方式没有进行排序，而是直接进行关键值比较，并存入相应的数据结构中，其运行速度会比 `groupby()` 的方式更快一些。但是如果根据多个关键值分组，或是需要对分组后的内容进行迭代访问， `groupby()` 分组的方法则更为灵活实用。

`groupby()`也可以自定义规则分组

```python
from itertools import groupby
lst=[2, 8, 11, 25, 43, 6, 9, 29, 51, 66]

def com(num):
    if num <= 10:
        return '低频'
    elif num >=30:
        return '高频'
    else:
        return '常规'

print [(k, list(g)) for k, g in groupby(sorted(lst), key=com)]
# 返回：
[('低频', [2, 6, 8, 9]), ('常规', [11, 25, 29]), ('高频', [43, 51, 66])]
```

