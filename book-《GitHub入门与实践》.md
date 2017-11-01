# 《GitHub入门与实践》

高效开发，代码审查，交流，简单。  
避免本人看懂、打错字、理解错误的 Bug


## 1. 欢迎

### 1.1 github简介  

### 1.2 带来的变化
协作形式   
Pull Request   ——开发者间的化学反应  
`watch`，添加感兴趣的repository

 
#### tip1：
可用描述方法：
1. @user  @organization   //通知单人/多人  
2. \#编号 //自动链接到仓库对应的Issue编号

     user / repository # 编号


### 1.3 + 1.4 社会化编程
IT的人才流动性  
不闭目塞听，接触不同的文化   
踏踏实实编写出代码的职业程序员   
面向人  

### 1.5 GitHub提供主要功能
* repository  
* issue    
追踪管理任务/问题。bug管理系统，一个功能更改或修正对应一个Issue，谈论和修正以Issue为中心。   
在 Git 的提交信息中写上issue的ID(`#7`),github自动生成从Issue到对应提交的链接。特定格式的提交，还可关闭Issue。


* wiki
开发文档/手册

* Pull Request
申请对方合并自己的修改。










## 2. Git

版本管理系统，git安装，环境变量，git-bush，初始设置


1. 设置使用 Git 时的姓名和邮箱地址，所设置会用在 Git 的提交日志中。在 GitHub 上公开仓库时，会随着提交日志一同被`公开`。

    $ git config --global user.name "Firstname Lastname"
    $ git config --global user.email "your_email@example.com"

将在`~/.gitconfig`中以如下形式输出设置文件。

    [user]
    name = Firstname Lastname
    email = your_email@example.com

2.  提高命令输出的可读性

    $ git config --global color.ui auto
`~/.gitconfig`中会增加下面一行。

    [color]
    ui = auto











## 3. GitHub准备
注册，头像，ssh-key


### 添加密钥
    $ ssh-keygen -t rsa -C "your_email@example.com"
按照英文提示输入[存放地址]和[认证密码]

在web界面中添加密钥：
Account Settings  ->   SSH Keys   -> Add SSH Key  
Title 中输入适当的密钥名称。Key 赋值 id_rsa.pub 内容。添加后会有邮件提示。

    $ cat ~/.ssh/id_rsa.pub

完成以上设置后，即可用私钥与 GitHub 进行认证和
通信。

    $ ssh -T git@github.com

出现以下提示说明连接成功。

    Hi xxx! You've successfully authenticated, but GitHub does not provide shell access.



### 社区功能
Follow user  
Watch repository



### New repository

右上角[用户]左边的[+]号，新建仓库。点击后跟从页面操作。

Initialize this repository with a README
GitHub 会自动初始化仓库并设置 README 文件，让用户可以立刻clone 这个仓库。
如果想向 GitHub 添加已有的 Git 仓库，不必勾选，直接手动 push。

Add .gitignore
把不需要在Git仓库中进行版本管理的文件记录在 .gitignore 文件中

Add a license
生成包含许可协议内容的 LICENSE 文件，用来表明该仓库内容的许可
协议。



### clone 已有仓库

Clone with HTTPS ;Use Git or checkout with SVN using the web URL.

    $ git clone [url]
    Cloning into 'Hello-World'...
    remote: Counting objects: 3, done.
    remote: Total 3 (delta 0), reused 0 (delta 0)
    Receiving objects: 100% (3/3), done.

    $ cd Hello-World


### git status
创建示例test文本后，查看仓库状态

    $ git status

### 提交
先添加至暂存区(Index 数据结构中记录文件提交前状态)，再commit 到本地仓库中。添加后，查看提交日志。

    $ git add test.test
    $ git commit -m "add hello world"
    $ git log

push执行后，GitHub上的仓库才更新。

    $ git push













## 4.git操作

使用 Git 版本管理，须先初始化仓库：
    
    $ mkdir test
    $ cd test
    $ git init

初始化成功后，执行`git init`命令的目录下就会生成 .git 文件夹，存储管理当前目录所需的仓库数据。  
该目录的内容称为“附属于该仓库的工作树”。文件的编辑等操作在工作树中进行，然后记录到仓库中，以此管理文件的历史快照。

状态：`git status`

若只是在工作树中创建文件的话，不会记录进Git 的版本管理对象中。 此时 `git status`命令查看新建文件时，会显示在 Untracked files 。    
要想让文件成为 Git 仓库的管理对象，就需要用 `git add`命令将其加入暂存区（提交之前的一个临时区域，称 Stage/Index）中。  add后，文件显示在 Changes to be committed 中了。

保存：`git commit`  

将当前暂存区中的文件实际保存到仓库的历史记录中。

    $ git commit -m "First commit"
    [master (root-commit) 9f129ba] First commit
    1 file changed, 0 insertions(+), 0 deletions(-)
    create mode 100644 README.md


\-m 参数：

后的 "First commit"称作提交信息，是对这个提交的
概述。  


直接执行`git commit`：

执行后编辑器就会启动，在编辑器中记述提交信息的格式如下。  
● 第一行：用一行文字简述提交的更改内容  
● 第二行：空行  
● 第三行以后：记述更改的原因和详细内容  


中止提交：

若在编辑器启动后想中止提交，直接关闭编辑器，随后提交就会被中止。


查看提交后的状态:  
执行完 `git commit`后再来`git status`查看当前状态。

查看提交日志：  `$ git log`
包括：who when 提交或合并 操作前后区别   
commit 栏旁边显示的“9f129b……”是指向这个提交的哈希值。Git 的其他命令中，在指向提交时会用到这个哈希值。    

查看一行简述信息：git log命令后加上 `--pretty=short`

只显示指定目录、文件的日志：`$ git log [dir/filename]`

显示文件的改动：`$ git log -p`

    $ git log -p README.md

多种参数帮助开发者把握以往提交的内容。每当有想查看的日志就
积极去查，慢慢就能得心应手了。


git diff——查看更改前后的差别


未提交前，`git diff`查看工作树和暂存区的差别
+ 增加
- 被删除行
`git add` 后 git diff 工作树与暂存区状态无差别，不显示
`git diff HEAD` 查看与最新提交的差别

在执行 git commit命令之前先执行git diff HEAD命令，查看本次提交与上次提交之间有什么差别，等确认完毕后再进行提交。这里的 HEAD 指向当前分支中最新一次提交的指针。

保险起见，提交后看下提交日志，确认提交是否成功
$ git log



### 4.2 分支操作
并行作业，往往同时存在多个最新代码状态，从 master 分支创建 feature-A 分支和 fix-B 分支后，每个分支中都拥有自己的最新代码。

master 分支是 Git 默认创建的分支，因此基本上所有开发都是以这个分
支为中心进行的。可以同时进行完全不同的作业。等该分支的作业完成
之后再与 master 分支合并。

通过灵活运用分支，可以让多人同时高效地进行并行开发。


`git branch`
显示分支一览表,显示分支名列表，确认当前所在分支。


创建 test 分支：

    $ git branch test
并将当前分支切换为 test 分支。

    $ git checkout test



`git checkout  - b [name]`
创建并切换进入新分支

正常开发，修改代码，`git add`后提交，会提交到test分支。修改后的文件在master 中保持原样。

切换回上一个分支 - 连字符，代替分支名
$ git checkout -








特性分支：
集中实现单一特性（主题），除此之外不进行任何作业的分支。即便在开发过程中发现了 BUG，也需要再创建新的分支，在新分支中进行修正。

日常开发中，往往会创建数个特性分支，同时在此之外再保留一个随时可以发布软件的稳定分支。稳定分支的角色通常由 master 分支担当。

主干分支：master 
主干分支中并没有开发到一半的代码，可以随时供他人查看。

基于特定主题的作业在特性分支中进行，主题完成后再与 master 分支合并。只要保持这样一个开发流程，就能保证 master 分支可以随时供人查看。


//不要被限制了，同时管理多个版本发布 / 有时又需要用标签 Tag 等创建版本信息。主干分支也有多个。










合并分支：`git merge`
$ git checkout master
Switched to branch 'master'
$ git merge --no-ff feature-A       
//创建合并提交, --no-ff 参数
随后编辑器会启动，用于录入合并提交的信息。

默认信息中已经包含了从 feature-A 分支合并过来的相关内容，所
以可不必做任何更改。将编辑器中显示的内容保存，关闭编辑器。完成后即合并。

以图表形式查看分支:

    $ git log  -- graph








### 4.3 更改提交的操作

 ● git reset——回溯历史版本

实现功能后进行提交，累积提交日志作为历史记录，借此不断培育一款软件。


Git 的另一特征便是可以灵活操作历史版本。借助分散仓库的优势，可以在不影响其他仓库的前提下对历史版本进行操作。

$ git reset --hard fd0cbf0d4a25f747230694d95cac1be72d33441d
HEAD is now at fd0cbf0 Add index

提供目标时间点的哈希值，完全恢复至该时间点的状态。



git log命令只能查看以当前状态为终点的历史日志。所以这里要使用 

    git reflog

查看当前仓库的操作日志。在日志中找出回溯历史之前的哈希值，通过 git reset --hard命令恢复到回溯历史前的状态。


只要不进行 Git 的 GC（Garbage Collection，垃圾回收），就可以通过日志随意调取近期的历史状态，就像给时间机器指定一个时间点，在过去未来中自由穿梭一般。便开发者错误执行了 Git 操作，基本也都可以利用 git reflog命令恢复到原先的状态

git reflog 
显示的哈希值只要输入 4 位以上就可以执行。


合并时显示有冲突
feature-A 分支更改的部分与本次想要合并的 fix-B 分支更改的部分发生了冲突

在编辑器中将其改成想要的样子。
本次修正让 feature-A 与 fix-B 的内容并存于文件之中。

冲突解决后，执行 git add命令与 git commit命令。
$ git add README.md
$ git commit -m "Fix conflict"
Recorded resolution for 'README.md'.
[master 6a97e48] Fix conflict

由于本次更改解决了冲突，所以提交信息记为 "Fix conflict"。


 git commit  -- amend——修改提交信息
 要修改上一条提交信息，执行上面的命令后，编辑器就会启动。


 $ git log --graph
 可以看到提交日志中的相应内容也已经被修改。





 提交这部分内容。这个小小的变更就没必要先执行 git add命令
再执行 git commit命令了，我们用 git commit -am命令来一次
完成这两步操作。

对已有文件的小修改，添加commit -am  //创建了新的得add

    $ git commit -am "Add feature-C"
[feature-C 7a34294] Add feature-C
1 file changed, 1 insertion(+)



错字漏字等失误称作 typo，所以我们将提交信息记为 "Fix typo"



更改历史
$ git rebase -i HEAD~2


feature-C 分支的使命告一段落，我们将它与 master 分支合并。
$ git checkout master
Switched to branch 'master'
$ git merge --no-ff feature-C












4.4　推送至远程仓库

仓库名请与本地仓库保持一致，即 git-tutorial。创建时请不要勾选 Initialize this repository with a README 选项，否则GitHub 一侧的仓库就会自动生成 README 文件，从创建之初便与本地仓库失去了整合性。



 ● git remote add——添加远程仓库

 $ git remote add origin git@github.com:github-book/git-tutorial.git

按照上述格式执行 git remote add命令之后，Git 会自动将git@github.com:github-book/git-tutorial.git远程仓库的名称设置为 origin（标识符）。


git push——推送至远程仓库
在 master 分支下：
git push -u origin master

-u参数可以在推送的同时，将origin仓库的master分支设置为本地仓库当前分支的 upstream（上游）。

。添加了这个参数，将来运行 git pull命令从远程仓库获取内容时，本地仓库的这个分支就可以直接从 origin 的 master 分支获取内容，省去了另外添加参数的麻烦。

本地仓库中创建了 feature-D 分支，现在将它 push 给远程仓
库并保持分支名称不变。
$ git checkout -b feature-D
$ git push -u origin feature-D








4.5　从远程仓库获取
 ● git clone
注意不要与之前操作的仓库在同一目录下。

执行 git clone命令后我们会默认处于 master 分支下，同时系统
会自动将 origin 设置成该远程仓库的标识符。也就是说，当前本地仓库
的 master 分支与 GitHub 端远程仓库（origin）的 master 分支在内容上是
完全相同的。


$ git branch -a 
验证，-a 参数可以同时显示本地仓库和远程仓库的分支信息。



获取远程的 feature - D 分支至本地仓库
$ git checkout -b feature-D origin/feature-D













pull Push ——> pull request
fork <——firest-pr

gh-pages-> work


git clone git@github.com:hirocastest/fires-pr.git

cd first-pr

git branch -a
git checkout -b work gp-pages
git branch -a
ls
git diff

check in browser

git add index.html
git commit -m 'from wq'
git push origin work 本地 work 分支的相应远程分支

git branch -a
查看分支，/origin/work 已被创建。


发送pull request












## 关于后面几章的内容：

几款软件

开发流程介绍

团队合作 - 多pull request 几个合作中注意的点
    积压之前，把上一次的全部处理掉，就不会挤压啦哈哈哈

gist：用url 分享代码小片段/日志文件 