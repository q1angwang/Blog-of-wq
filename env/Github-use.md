# 连接github

1. git环境

2. 生成秘钥key
    `$ ssh-keygen -t rsa `
    连续三个回车，key就生成，默认存放路径：`/Users/wangqiang/.ssh`

3. 打开自己的Github主页，在settings里面设置`SSH and GPG keys`

4. 打开生成的`id_ras.pub`文件，将公钥公布给github，注意文件中的所有文本都要po上去。

5. 测试连接 
    `$ ssh -T git@github.com`
    第一次测试时会弹出警告，填yes后回车

6. 设置username和email
    $ git config --global user.name "q1angwang"
    $ git config --global user.email "565603068@qq.com"
    在把本项目上传到github之前设置username和email，每次commit都会记录下username和email。








## 更新仓库

1. 选择一个仓库的`clone with ssh`，eg：
    $ git clone git@github.com:q1angwang/Notes.git


2. 操作本地仓库：
    $ git add .
    //$ git add --all #(-A) #将删除文件操作也加到stages中
    //`git add .`只能stages新文件和被修改文件，没有被删除文件
    $ git commit -m'first commit'

[建议]：每次add后，再使用`git status`确认新操作stage了



3. 把本地仓库推送到远程仓库 ：
    $ git push origin master















# 设置全局大小写敏感
默认不敏感

    $ git config --global core.ignorecase false

完事后`.gitconfig`文件内容显示：

    [core]
        quotepath = false
        ignorecase = false
    [user]
        name = q1angwang
        email = qiangwanghhh@gmail.com















# 删除文件操作(git仓库中)

$ rm test.txt
$ git rm test.txt
$ git commit -m "remove test.txt"
$ git add all #可提交未跟踪、修改和删除文件。
$ git add .可以提交未跟踪和修改文件，但是不处理删除文件。








# Issue pushing new code in Github


## Q1：
➜  Notes git:(master) git push origin master
To github.com:q1angwang/Notes.git
 ! [rejected]        master -> master (fetch first)
error: failed to push some refs to 'git@github.com:q1angwang/Notes.git'
hint: Updates were rejected because the remote contains work that you do
hint: not have locally. This is usually caused by another repository pushing
hint: to the same ref. You may want to first integrate the remote changes
hint: (e.g., 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.

A：
Previously, your have a push not from this terminal, and your local repository doesn't know about this commit yet. Hence: `Updates were rejected because the remote contains work that you do not have locally.`

    git pull && git push origin master
    //or
    git push -f origin master
BEWARE: Using force can change the history for other folks on the same project. Basically, if you don't care about a file being deleted for everyone, just go ahead. Especially if you're the only dev on the project.



## Q2:
➜  Notes git:(master) git push origin master
To github.com:q1angwang/Notes.git
! [rejected]     master -> master (non-fast-forward) 
error: failed to push some refs to 'git@github.com:q1angwang/Notes.git' 
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. Integrate the remote changes (e.g.
hint: 'git pull ...') before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.


当前分支代码上传到master分支上时出错，github中的部分文件不在本地代码目录，可以通过如下命令进行代码合并

    $ git pull --rebase origin master

//pull=fetch+merge

此时再执行语句 `git push -u origin master`即可完成代码上传到github












# branch have diverged
## Q：

    $ git status
    On branch master
    Your branch and 'origin/master' have diverged,
    and have 22 and 23 different commits each, respectively.
      (use "git pull" to merge the remote branch into yours)

    nothing to commit, working tree clean

    WQ@DESKTOP-3BGM28T MINGW64 ~/Documents/CloudFile/Work/Notes/2019Course (master)
    $ git merge origin/master
    fatal: refusing to merge

## 解决1：

    git merge master --allow-unrelated-histories

## 解决2：

    $ git rebase origin/master 
    $ git pull --rebase 
    $ git push origin master 



















# 为什么Github没有记录你的Contributions

解决方法来源：
http://xunli.xyz/2016/01/09/github-not-count/


因为git初始化设定时没有设定正确的用户名和邮箱（主要是邮箱），具体可以参考Github官方写的help文档

https://help.github.com/en/articles/why-are-my-contributions-not-showing-up-on-my-profile


条件：
1. commits使用的email地址是与你的Github账号相关联的
2. 这些commits是在在默认分支上（通常是master）


排查：
本地repo里用git log，查看commit记录上的个人邮箱是否正确


强制恢复之前不是自己名字的commit记录：
见作者原文方法

## 完成后需设置本地git配置
git config --global user.email "565603068@qq.com"
git config --global user.name "q1angwang"
