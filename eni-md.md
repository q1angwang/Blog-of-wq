# Markdown 参考

<i style="color:grey">Last Updated: 2017-8-1</i>  
<script async src="//dn-lbstatics.qbox.me/busuanzi/2.3/busuanzi.pure.mini.js"></script>
<span id="busuanzi_container_page_pv" style="float:right;">
  Page views: <span id="busuanzi_value_page_pv"></span>
</span><br>


## markdown简介
Markdown 是一种轻量级标记语言，它允许人们使用易读易写的纯文本格式编写文档，然后转换成有效的 HTML 文件。
>markdown 是什么？  
>同样是标记语言，但它相比HTML更加简单！一是体现在标记符的数量上，二是体现在标记符的书写上。HTML标记符号非常多，并且需要标记内容的开始和结束位置，而markdown只有四个基本的标记符号，只要在开始位置标记即可。  
>markdown 解决什么问题？  
>当我们需要让文档看起来层次分明，但又不依赖于word这样的编辑工具来书写、排版和读取时，markdown的易写易读优势就非常突出了。并且在我使用一段时间以后，发现使用markdown非常有助于帮助作者在写作时整理自己的逻辑思路和段落层次。
——from [Scien](http://www.jianshu.com/p/de9c98bba332)


## md语法


### 1. 段落与换行

\# 1         一阶标题  
\#\# 0x00     二阶标题

- 起新段落：  
空出一行即可。

- 段落的前后必须是空行：  
空行：行内什么都没有，或只有空格/ 制表符  

- 在当前行尾加 2 个或更多空格    
下一行就会新起一行  
相邻的两行文本，如果 中间没有空行/上一行行尾缺少2 个空格 ，就会显示在一行中（换行处被转为空格）

- 如果需要在段落内换行，加标签：< br>

- **Markdown 中的多数区块都需要在两个空行之间。**


### 2. 字体格式

\*xx\*		 *斜体*

\*\*xxx\*\*  **加粗**

 \*\*\*xxx\*\*\*  ***粗斜体*** 

\_xxx\_           _下划线_

\`xxx\`           `变成块强调 / 一般の代码块`

\~~aaa\~~	~~删除线~~

\>		          
>   引用


\`\`\`python  
from PIL import Image   
\`\`\`
代码块高亮显示：\`\`\` / 直接空Tab

```C
#include<stdio.h>
```


### 3. 链接与图片
文字链接：  
[链接名称]\(http://链接网址)：[xx](http://xxx.com)  

网址链接：  
\<http://xxx.com\>： <http://xxx.com>

图片：  
\![xxx]\(url)：![xxx](xxx.jpg/png/gif) 


### 4. 列表 表格
\-/\* xxx 
- 无序列表

\1.xxx:     
1. 有序列表 	

- [Tab]可以创造二级序列

\-\-\-  
三个以上的短线，即可作出分割线



#### 表格：
|Table|'s    |demo|
| --- |-----| --- |
| 1     | test1| $16 |
| 2     | c1       | $12 |
| 3     | d1       |   $1 |


#### LaTeX 公式：  
md可以创建行内公式 或 块级公式:  
\$\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$  

$\Gamma(n) = (n-1)!\quad\forall n\in\mathbb N$

$$ x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$

\$$ x = \dfrac{-b \pm \sqrt{b^2 - 4ac}}{2a} $$  


#### Task List：

- [x] HTML
- [x] CSS
- [  ] JavaScript

### 5. Tips

#### 转换为PDF

Chrome/Firefox:  
Markdown 转换为 HTML  之后，可以通过浏览器 打开它。选择 '打印'（Ctrl+P），然后更改 '目标打印机' 为 '另存为 PDF'，~~再进行一些设置后~~，即可保存为 PDF 文档。

####  输出空格
& emsp; 来输入两个空格(段首)  
& nbsp; 来输入单个空格
>「Markdown 语言」不负责实现段首缩进 (`->`)  
段首缩进这件事，应该是 CSS 或其他排版工具的事情，Markdown 奉行的是样式和内容分开的哲学。我们需要一个干净些的排版。

#### 限制图片大小并居中
```<div align=center><img src="image/1.jpg" width="200" height="200"/></div>```    
<div align=center><img src="image/1.jpg" width="400" /></div>

#### 目录
用 [TOC] 来生成目录

#### HTML标签可用  
Markdown 只控制文档的结构，不控制文档的样式，md内容转换后的样式完全由 转换器/样式 决定。  
如果要修改样式，在需要渲染的地方（比如你的blog上）覆盖默认样式即可。

#### 注释：
\[^\_^\]  
测试 (b被吃掉)：
a
[^_^]:b 
c



---


| 标题：Markdown 参考  
| 作者：强王  
| 发布：2017-8-1  
| 来源：http://qiangwang.site/blog/eni-md.html  
| 版权声明： 本文由 强王 原创，采用[保留署名-非商业性使用-禁止演绎 4.0-国际许可协议](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh)  
| 转载请保留以上声明信息