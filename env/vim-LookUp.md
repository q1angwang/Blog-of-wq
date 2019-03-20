 # vim LookUp  

<i style="color:grey">Last Updated: 2017-10-20</i>  
<script async src="//dn-lbstatics.qbox.me/busuanzi/2.3/busuanzi.pure.mini.js"></script>
<span id="busuanzi_container_page_pv" style="float:right;">
  Page views: <span id="busuanzi_value_page_pv"></span>
</span><br>





** Better, Stronger, Faster. **







## 1. *Normal* 模式
* 按下[Esc]进入 *Normal*

* number-command-object


### 0. 光标

                 ^
                 k                    
       < h          l >                  
                 j                           
                 v

#### 行内：

0 → 数字零，到行首   
^ → 到本行第一个不是blank字符的位置（blank字符：空格，tab，换行，回车等）  
$ → 到本行行尾  
g_ → 到本行最后一个不是blank字符的位置  


#### 单词：

w → 到下一个单词的开头
e → 到下一个单词的结尾  
//一个单词由字母数字下划线组成，由程序变量规定  
大写的E和W → 下一个空隔

#### 行间：

N+gg → 跳转到N行  
N+G → 跳转到N行  
gg → 第一行  
G → 最后一行  





### 1. 退出+保存

退出vim编辑器并放弃所有修改∶

    :q!         <回车>
保存所有修改∶

    :wq         <回车>
 :wq → :w 存盘; :q 退出   （:w 后可以跟文件名）  
:wq  =  :x  = ZZ            //:x 仅需要时保存

另存为：

    :saveas [path/file]

### 2. 进入*Insert*

    i → 在当前光标处插入       
    a → 在光标后插入
    o → 在当前行后插入一个新行
    O → 在当前行前插入一个新行





### 3. 修改  

删去光标处字符
    
    x


删除掉该单词
从当前光标删除到行末
可以删除整一个当前行

    dw       
    d$      
    dd     


粘贴 paste  

    p
dd 将某行删除后 ，光标移动到准备置入的位置的上方，`p` 将该行粘贴置入    
yy=ddP  
p = paste After  
P = paste Before  


撤销  undo    

    u   
撤消掉撤消命令

    CTRL-R      //redo









## 2. Tips

* 所有文本都修正完毕，请按下 <ESC> 键返回正常模式。


* 帮助菜单

    :help <command>


* 设置数字行号(注意:复制同时复制行号)

    :set nu     


* 寻找字符串xxx；n——下一个

    /xxx       


* {} 光标移到某个`{`后按下`%`，对应到`}`，即匹配括号

    % 

* 匹配光标当前所在的单词，移动光标到下一个

    \*    //nextOne
    #       //beforeOne

* 重复命令

    N.  //重复上一个命令
    N<command>  

N = 重复次数



* 自动补齐：

     <C-n> 和 <C-p>



### 宏录制
### 分屏: :split 和 vsplit
### 可视化



## Refer： [简明 VIM 练级攻略](https://coolshell.cn/articles/5426.html)



| 标题：Vim查询  
| 作者：强王  
| 发布：2017-10-20
| 来源：http://qiangwang.site/blog/eni-vim1 
| 版权声明： 本文由 强王 原创，采用[保留署名-非商业性使用-禁止演绎 4.0-国际许可协议](https://creativecommons.org/licenses/by-nc-nd/4.0/deed.zh)  
| 转载请保留以上声明信息