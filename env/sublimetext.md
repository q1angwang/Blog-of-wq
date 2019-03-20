# Sublimetext配置

<i style="color:grey">Last Updated: 2018-3-1</i>  
<script async src="//dn-lbstatics.qbox.me/busuanzi/2.3/busuanzi.pure.mini.js"></script>
<span id="busuanzi_container_page_pv" style="float:right;">
  Page views: <span id="busuanzi_value_page_pv"></span>
</span><br>



# 基础配置：
Preferences -> Setting (可选user)

    "trim_trailing_white_space_on_save":	true,
    "ensure_newline_at_eof_on_save":		true,
    "save_on_focus_lost":					true,
    "highlight_line":						true,
    "word_wrap":							true,
    "fade_fold_buttons":					alse,
    "bold_folder_labels":					true,
    "highlight_modified_tabs":				true,
    "default_line_ending":					"unix",
    "tab_size":								4,
    "font_face":							"Microsoft YaHei Mono",
    "translate_tabs_to_spaces":				true,//indent use space
    "spell_check":							true,//英文创作 启用拼写检查



## Font
Microsoft YaHei Mono——中文为微软雅黑，英文为Consolas，自带粗体斜体。  
Consolas作为英文字体来说，它是一个等宽字体，并且设计得十分适合写代码。  
```"font_face": "Microsoft YaHei Mono",```










# 插件

## IMESupport
光标跟随在win10上的问题。  
问题版本：win10 31xx版本 2018年01月16日

1. 下载：https://github.com/zcodes/IMESupport
2. Preferences->Browse Packages打开插件安装的目录
3. 将解压后的文件夹复制到上一步打开的目录中
4. 重启sublime text 3即可

## ConvertToUTF8

1. 安装Package Contro:
	ctrl+Shift+P打开package，输入Install Package关键字，点击Package Control: Install Package。
2. 左下角有个=号来回动，稍等一会，会再次在命令行下弹出一个下拉菜单。输入"ConvertToUTF8"
	//GBK Encoding Support”
3. 重启sublime text 3，中文字符就可以正常显示了。











<!--

## Boxy theme(集成多个主题)
1. Package Control: Install Package——>Boxy Theme——>[Enter]
2. 激活theme： Command Palette选择Boxy Theme: Activation





## python support——sublime REPL
1. 打开Sublime text 3 安装package control
2. Ctrl+shift+p 键入 install packages稍等片刻后 键入 SublimeREPL 安装
    激活：通过选项Tools->SublimeREPL->Python就可以看到效果了
3. 键位绑定：
    每次通过Tools->SublimeREPL->Python这样的方式比较繁琐，将这样的操作和一个按键如F1绑定，Preferences->Key Bindings-User:

    {"keys":["f1"],
    "caption": "SublimeREPL: Python",
    "command": "run_existing_window_command", "args":
    {"id": "repl_python",
    "file": "config/Python/Main.sublime-menu"}}
    ,
    {"keys":["f5"],
    "caption": "SublimeREPL: Python - RUN current file",
    "command": "run_existing_window_command", "args":
    {"id": "repl_python_run",
    "file": "config/Python/Main.sublime-menu"}}
4. 注意：
**REPL需要python环境支持**

	while (True):
		print hi
死循环的程序用StF5去跑会崩溃, 并且跑不了





## 拓展包管理
Show the same open file in multiple：
	File -> New View into File

delete:在软件菜单里preferences->browse packages，打开的那个目录，把Sublime Text 3那层目录全删了就可以了。这里存着用户数据，卸载或者升级时是不会动这里的数据的

https://www.sublimetext.com/docs/3/revert.html
 -->








# 快捷键




## 编辑

Ctrl+Z 				撤销  
Ctrl+Y 				恢复撤销  
  
cmd  + d          	选择同样的单词  
cmd  + 单击       	同时选择多处文本  
Shift+ 右键/中键		竖向多行选择  
  
Ctrl + /         	注释整行  
ctrl + shift+k 		删除当前行  
Ctrl + ←/→ 		逐词移动  
Ctrl + Shift+←/→	逐词选择。  
  
Ctrl + ↑/↓  			移动当前显示区域  
Ctrl + Shift+↑/↓		移动当前行。  
  
F6 					检测语法错误, 英文写作时好用  





## 搜索

Alt + C         切换大小写敏感（Case-sensitive）模式  
Alt + W         切换整字匹配（Whole matching）模式  
Ctrl+ H 			正则的支持  
  
选中范围内搜索：  
（Search in selection）,通过配置项在选中文本的状态下范围内搜索就会自动开启。  
	```“auto_find_in_selection”: true,```  
配合这个功能，局部重命名（Local Renaming）变的非常方便  






## 查看代码

Ctrl+F2 	设置/取消书签  
Shift+F2 	上一个书签  
  
ctrl+g 		跳转指定行  
ctrl+r 		跳转到标志————			显示函数(类)列表，输入关键字来查找所需要的函数/类  
  
Alt+Shift+2	左右分屏(1恢复)  
Alt+Shift+8 上下分屏  
Alt+Shift+5 分为四屏  
  





## 标签页与文件
Ctrl+k+b 		文件列表  

Ctrl+Shift+T 	打开刚关闭的tab页 //chrome同  

右键+滚轮		切换标签  
  
ctrl+p 快速查找和打开文件。  

	在当前打开文件所在目录下的文件都可以检索到  
	在工程中文件的一部分路径/文件名你就可以很容易的打开这个文件  
	这在一个大型的 Django 工程中显得非常方便。比如你想打开login/func/funtion.php，你只要在输入框中输入login/func/funtion.php即可，也可以用模糊匹配，如login/function等  
  
	在Ctrl+P 匹配到文件后，我们可以进行后续输入以跳转到更精确的位置：  
  
	@ 符号跳转：输入@symbol跳转到symbol符号所在的位置  
	# 关键字跳转：输入#keyword跳转到keyword所在的位置  
	: 行号跳转：输入:12跳转到文件的第12行。  
