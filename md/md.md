# Markdown

## 1. markdown简介
Markdown 是一种轻量级标记语言，它允许人们“使用易读易写的纯文本格式编写文档，然后转换成有效的XHTML(或者HTML)文档
>markdown 是什么？  

>同样是标记语言，但它相比HTML更加简单！一是体现在标记符的数量上，二是体现在标记符的书写上。HTML标记符号非常多，并且需要标记内容的开始和结束位置，而markdown只有四个基本的标记符号，只要在开始位置标记即可。

>markdown 解决什么问题？  

>当我们需要让文档看起来层次分明，但又不依赖于word这样的编辑工具来书写、排版和读取时，markdown的易写易读优势就非常突出了。并且在我使用一段时间以后，发现使用markdown非常有助于帮助作者在写作时整理自己的逻辑思路和段落层次。

--from [Scien](http://www.jianshu.com/p/de9c98bba332)

## 2. 段落与换行
\# 1         总标题  
\#\# 0x00     二阶标题

1.段落的前后必须是空行：

空行指的是行内什么都没有，或者只有空白符（空格或制表符）  
_>相邻两行文本，如果中间没有空行 会显示在一行中（换行符被转换为空格）  

2.如果需要在段落内加入换行<br/><br>


在当前行的结尾加 2 个或更多空格    
这行就会新起一行  
如果是要起一个新段落，只需要空出一行即可。

3.Markdown 中的多数区块都需要在两个空行之间。

\*xx\*		      *斜体*

\*\*xxx\*\*   	  **加粗**

\`xxx\`     	  `变成红色的块强调`

\~~aaa\~~	      删除线

\>		          >引用

文字链接： [链接名称](http://链接网址) 	链接			//<http://www.izhangbo.cn> 

网址链接： <http://链接网址>

![xx](url)  图片   		//<img src="1.png"/> HTML标签可用

* xxx		无序列表		//Space

1.xxx:     有序列表 	//Space
    >nihao

<br/>		换行


```python
from PIL import Image			代码块 高亮显示 //直接空Tab也可以
```

`#include<stdio.h>`				 一般代码块

三个以上的短线 即可作出分割线
------

表格：

| Tables        | Are           | Cool  |
| ------------- |---------------| ------|
| col 3 is      | right-aligned | $1600 |
| col 2 is      | centered      |   $12 |
| zebra stripes | are neat      |    $1 |

### LaTeX 公式
可以创建行内公式，例如:
$\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$。
或者块级公式：
$$	x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$

###Task List
- [x] Code
- [x] HTML
  - [x] CSS
  - [x] JavaScript

## 转换为PDF

Chrome

在将 Markdown 转换为 HTML 文档 之后，可以通过 Chrome 浏览器 打开它。选择 '打印'（Ctrl+P），然后更改 '目标打印机' 为 '另存为 PDF'，再进行一些设置后，即可保存为 PDF 文档。

###  输出空格
&emsp;来输入两个空格&emsp;来输入两个空格

### 限制图片大小并居中
<div align=center><img src="123.jpg" width="200" height="200"/></div>
![图片名称](http://图片网址)
链接前加“!”





「Markdown 语言」不负责实现段首缩进 (ˊ_>ˋ)段首缩进这件事，应该是 CSS 或者其他排版工具的事情，Markdown 奉行的是样式和内容分开的哲学。即使手动输入空格，&nbsp; 也是很不推荐的方法。我推荐全角空格，切换到全角模式下（一般的中文输入法都是按 shift + space）输入两个空格就行了。这个相对 &nbsp; 来说稍微干净一点，而且宽度是整整两个汉字，很整齐。


注释：
[^_^]:
[^_^]:
    commentted-out contents
    should be shift to right by four spaces (`>>`).

测试：
a

[^_^]:
    b

c

d