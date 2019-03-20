# python-利用range高效执行


Python 3中的range()只是Python 2中被称为xrange的函数的重命名版本。

## 功能

只能在需要时一次返回一个数字。

```py
    for i in range(3):
        print(i)
```
output:

    0 
    1 
    2

range （0默认不用写
step可正可负


## 使用目的

1. 重复执行for循环的循环体指定次数
2. 创建比使用列表或元组完成的更高效的整数迭代算法




## 特性

Python中range()是一种类型

可以按索引访问range()中的项，就像列表中的那样
`range(6)[1]`

甚至可以在range()上使用切片标记
`range(6)[2:5]`

range()与列表不同，是惰性的，但不是迭代器。

range 不存数/列表在内存中，可以高效利用存储空间

range处理的数字是整数，浮点的解决方案是NumPy



## 更高效
使用迭代器 itertools系列：
https://docs.python.org/zh-cn/2.7/library/itertools.html