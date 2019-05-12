# Mac_拷贝硬盘中文件

移动硬盘的文件在mac系统中呈现灰色的解决方法


## 存在问题
复制/修改时提示文件正在被其他程序使用；后来移动硬盘的文件有的也灰色，有拷贝过程，但是不能成功拷贝到电脑中。比如下图，移动硬盘中，系统镜像文件全部灰色，执行如图步骤。

"one or more items can’t be changed because they are in use"

![](Mac_拷贝硬盘中文件.png)

点击继续按钮需要管理员密码，并且表现为该文件似乎被复制/移动，但复制到最后，目标文件会"忽然"消失。


## 解决命令

    xattr -d com.apple.FinderInfo [filePath]
路径信息可以把灰色文件拽进终端窗口





## 真正原因

是扩展文件属性问题，在Terminal中可以`ls -l@`看到文件多了个@属性。需要用xattr删掉@属性。

    > ls
    -rwxr-xr-x @ 1 zzz staff 42164199 Dec 19 18:58 MAH07541.MP4
    > ls -l@
    -rwxr-xr-x@ 1 zzz  staff  42164199 Dec 19 18:58 MAH07541.MP4
        com.apple.FinderInfo          32

因此`com.apple.FinderInfo`是导致问题的属性。只要我删除了扩展属性`xattr -d com.apple.FinderInfo MAH07541.MP4`，一切都恢复正常，文件可以被复制/移动/删除。



当摆弄扩展属性时要小心，因为它们也可以存储资源或基本文件元数据。



## REFER
<https://discussions.apple.com/thread/3917858>