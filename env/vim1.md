# vim LookUp

<i style="color:grey">Last Updated: 2018-4-28</i>
<script async src="//dn-lbstatics.qbox.me/busuanzi/2.3/busuanzi.pure.mini.js"></script>
<span id="busuanzi_container_page_pv" style="float:right;">
  Page views: <span id="busuanzi_value_page_pv"></span>
</span><br>










**Better, Stronger, Faster.**





## *Normal* 模式
* 按下[Esc]进入 *Normal*



### 0. 光标

             ^
             k
       < h      l >
             j
             v

* 行内：  
0 → 数字零，到行首  
^ → 到本行第一个不是blank字符的位置（blank字符：空格，tab，换行，回车等）  
$ → 到本行行尾  
g → 到本行最后一个不是blank字符的位置

* 行间：  
N+gg → 跳转到N行  
N+G → 跳转到N行  
gg → 第一行  
G → 最后一行 

* 单词：  
w → 到下一个单词的开头  
e → 到下一个单词的结尾  一个单词由字母数字下划线组成，由程序变量规定  
E/W → 下一个空隔


 


### 1. 进入*Insert*

    i → 在当前光标处插入
    a → 在光标后插入
    o → 在当前行后插入一个新行
    O → 在当前行前插入一个新行






### 2. 退出+保存

    :q!                     #退出vim编辑器并放弃所有修改∶
    :wq                     #保存所有修改∶
    :w                      #存盘，:w 后可以跟文件名）  
    :q                      #退出  
    :wq  =  :x(仅需要时保存) = ZZ  
    :saveas [path/file]     #另存为





### 3. 修改
删去光标处字符

    x
    dw     #删除掉该单词
    d$     #从当前光标删除到行末
    dd     #可以删除整一个当前行


粘贴

    p      #paste

    dd 将某行删除后 ，光标移动到准备置入的位置的上方，`p` 将该行粘贴置入

    yy = ddP

    p  = paste After  
    P  = paste Before


撤销

    u           #undo
    CTRL-R      #redo, 撤消掉撤消命令








## 编辑模式








## Tips

* 所有文本都修正完毕，请按下 ```<ESC>``` 键返回正常模式。



* 帮助菜单

    ```:help <command>```






* 显示数字行号

    ```:set nu```    注意:复制同时复制行号





* 寻找字符串xxx

    ```/xxx```       找到后输n, 跳转至下一个xxx






* 匹配括号  
    ```%```          光标移到某个`{`后按下`%`，对应到`}`

* 匹配光标当前所在的单词  
    ```*```          nextOne  
    ```#```          beforeOne
 
* 重复命令  
    ```N.```          重复上一个命令，N = 重复次数

* 自动补齐   
    ```<C-n> 和 <C-p>```












<!-- 

### 宏录制
### 分屏: :split 和 vsplit
### 可视化
 -->


### Refer： [简明 VIM 练级攻略](https://coolshell.cn/articles/5426.html)
