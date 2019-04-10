# python-assert

开发一个程序时候，与其让它运行时崩溃，不如在它出现错误条件时就崩溃（返回错误）。

这时候可以利用好断言assert

    如果你断言的语句正确 则什么反应都没有 
    但如出错,就会报出 AssertionError,并且错误可以自己填写



## 使用

格式 ： 

    assert+空格+要判断语句+双引号“报错语句”

例子：

    >>> assert 1>5, "chucuo"
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    AssertionError: chucuo
    >>> assert 5>1, "chucuo"
    >>> 
