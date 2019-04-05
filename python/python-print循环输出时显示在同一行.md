# python print 循环输出在同一行

仔细看看print的参数：
    
    print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
value是要打印的字符串

sep则是value之间的间隔
(可以print("Hello","Python")看到中间确实有一个空格间隔开了)

end为print默认在结束的时候打印一个\n
要print不换行，只要把end参数换成''即可

file是具体打印到哪里，sys.stdout是系统的控制台，即标准输出设备

flush=False说明print不开启缓冲区
要开启缓冲区只需把flush设置成True即可。


## 在python终端中显示在同一行 实例

    #python3
    for i in range(1000):
        print('%d'%(i) , end='\r')

    #python2
    for i in xrange(1000):
        print '%d\r'%(i) 




## 来源(原理)
\r 和 \n 都是以前的那种打字机传承来的。

\r 回车，即打印头归位，回到某一行的开头。
\n 换行，就是走纸，下一行。

linux只用\n换行。
windows用\r\n表示换行。

测试： 

    print(u'前面的内容\r只显示后面的内容')

cmd控制台中显示：“只显示后面的内容”
\r真正实现了其回车的功能——回到某行开头，把前面的输出覆盖

自带的IDLE运行显示：“前面的内容只显示后面的内容”
更接近于写文件，所以都写出来了(转义字符没显示)。



## 倒计时模块

    #-*- coding:utf-8 -*-
    import time
    print("倒计时程序")
    for x in range(5,-1,-1):
        mystr = "倒计时" + str(x) + "秒"
        print(mystr, end = "")
        print("\b" * (len(mystr)*2), end = "", flush=True)   #\b：退格，用于清理一行内的所有字符 2：字符串是中文时占位符长度为2，英文为1
        time.sleep(1)

注意，在python IDLE的shell中无法按照需要在一行中运行(无法识别\b转义字符)，需要cmd环境

## 显示百分比进度的程序：

    #-*- coding:utf-8 -*-
    import time
    print("显示百分比")
    for x in range(101):
        mystr = "百分比" + str(x) + "%"
        print(mystr,end = "")
        print("\b" * (len(mystr)*2),end = "",flush=True)
        time.sleep(0.5)