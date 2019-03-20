# 网络编程-conn.Read问题



## Q：golang，写socket client

被conn.Read折磨疯了。server端连续conn.Write五条消息，而client这边的的一句conn.Read有时能接收3条有时能接受4条，有时能接受5条...

golang里socket的io有没有类似readline或者readuntil之类的函数？

搜了好久，没人讨论




## 解决思路

1. 先看看到底是谁没发(收)


2. 自行合包解析

    c++里面Windows和Linux和Arduino系统都是会读出任意个数的字符，需要自行合包解析。

    如果是少收到的话，要记得设定某个参数才能在缓冲区清空之后才断开tcp，或者自己写个延时。TCP本来就是个流嘛。。。没有包的概念

    如果一定要按包分的话，可以考虑用UDP，一次一个不会多不会少



## 原因

这是TCP的延迟发送机制——？？算法决定的啥时发送，可以设置nodelay禁用这算法，然后就会定时flush了
参考：  
https://gitlab.com/fromddy/ddy_work/blob/master/river_tcp2.md  
错了，是这个  
https://gitlab.com/fromddy/ddy_work/blob/master/river_tcp1.md  




但是nodelay也不能阻止接收方粘包——只要接收方速度比发送方慢。就能粘

一个解决方法是：选择固定数据包大小。这样好分





## 其他

//最好别说啥粘包的名词，TCP是流协议，没有数据包的概念
//所以说现在有做无缓冲TCP实现的系统？
//不要这样说也行，毕竟数据包是应用层的实现，所以说和tcp没关系，但是操作系统的优化（好吧可以关掉）以及缓冲区（这个可以设置成0么）会导致收到的数据和某些人想象中的不一样。

//也许是flush在作怪
//建议rtfm //Read The Fucking(Friendly) Manua