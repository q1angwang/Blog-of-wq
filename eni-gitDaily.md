# GitHub使用日常

Github 上操作虽多，但是都是围绕一个个的项目展开的。



## 0. 创建项目

绿色的 [+ New repository]

可选 `Initialize this repository with a README`，然后创建这个项目。

Create Repository 按钮的上方还有两个选择框：
`.gitignore`&`LICENSE` 
选择这两项后会多两个文本文件，一个是 .gitignore 文件，另一个是 LICENSE 文件。若暂不选，可后期自己用编辑器新建。

创建后的页面：

`commit  `  
    --last commit  保存版本/版本
    -- commit message 可用版本留言来定位特定的某次修改
    项目首页的[N] commits 是个链接，点进为项目历史的页面。进入可关注why who when what commitID

`branch`





## 1. GitHub添加许可证

Q: 当我创建一个GitHub项目时，默认选择了None。如何添加许可证到已经创建的项目?

A: 去项目下，添加新文件，以`License.txt`或 `License.md`命名。 
输入文件名称后，许可选择器就会出现，选择许可类型即可。




## 2. 删除Repository

1. 进入仓库(Repository)，选择·`settings`    
2. 进入 settings 页后，下拉到最下面，有`Danger Zone`区域，点击即可。
若操作了一个 fork 后的项目，即等于 unfork 操作。




## 3. 本地直接删除文件后，git到远程仓库，为什么不会同步删除对应文件

应使用`git add -A`它能stages所有文件，而之前用的`git add .`只能stages新文件和被修改文件，没有被删除文件

需要把改动commit进版本库再push，在项目根目录使用命令

    git add -A   
    git commit -m "del   
    git push
推送到远程服务器

//建议每次add后，使用`git status`来查看是否已经stage了









## 4. 为每个项目设置主页(创建分支时不继承master的内容)

各个项目的主页是放在 gh-pages 分支的。放到 gh-pages 分支上的内容会被公开成网页。

在项目版本库中创建一个名为gh-pages的分支，并向其中添加静态网页即可。也就是说如果项目的Git版本库中包含了名为gh-pages分支的话，则表明该项目提供静态网页构成的主页，可以通过网址<http://<user-id>.github.io/<project-name>>访问。

作为项目网页demo的gh-pages分支中的内容和master不同，不希望gh-pages分支继承master分支的历史和文件，需要一个干净的gh-pages分支：


    $ git symbolic-ref HEAD refs/heads/gh-pages
    $ rm .git/index
    $ printf "hello world.\n" > index.html
    $ git add index.html
    $ git commit -m "branch gh-pages init."
    $ git push -u origin gh-pages

用到Git底层命令：git symbolic-ref；上述命令对应每一行的注释：

1. 用git symbolic-ref命令将当前工作分支由master切换到一个尚不存在的分支gh-pages。  
2. 删除暂存区文件，即相当于清空暂存区。  
3. 创建项目首页index.html。  
4. 添加文件index.html到暂存区。  
5. 执行提交。提交完毕分支gh-pages完成创建。  
6. 执行推送命令，在GitHub远程版本库创建分支gh-pages(已经建立过`push`操作)。  


* 若是在web中建立git-pages，可以从版本库里，获取并切去gh-pages分支进行静态网页编辑。

    $ git fetch
    $ git checkout gh-pages