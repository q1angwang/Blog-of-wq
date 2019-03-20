# npm

npm 是 Node.js 的包管理工具，随同NodeJS一起安装(新版的nodejs已经集成了npm)，能解决NodeJS代码部署上的很多问题

开发时，轮子很多，程序员开发的模块可以打包后放到npm官网上。这时就需要一个集中管理的工具，npm应运而生，可用于安装其他人发布的JavaScript代码、包。

使用场景有以下几种：

    允许用户从NPM服务器下载别人编写的第三方包到本地使用。
    允许用户从NPM服务器下载并安装别人编写的命令行程序到本地使用。
    允许用户将自己编写的包或命令行程序上传到NPM服务器供别人使用。












## 淘宝npm镜像
$ npm install -g cnpm --registry=https://registry.npm.taobao.org


可以使用 cnpm 命令来安装模块了

    $ cnpm install [name]
















# 日常使用

## 安装


npm search xxx

npm update xxx



0. npm install xxx

会将安装包放在 ./node_modules 下，如没该目录，会自动生成。

nodejs中通过 require('xxxxx')引入本地包


1. npm install 
装在./node_modules 里

安装某项目npm依赖，该命令会自动根据`package.json`中的dependencies配置(模块的依赖)安装所需依赖包



2. 全局安装
`/usr/local/lib/node_modules/$ npm install xxx`

`$ npm install xxxx -g`

该目录是全局目录，所安装包可直接在命令行中使用

同时在项目/全局安装包，可以两个地方都install，或是`npm link`





## 卸载

npm uninstall xxx
aliases: remove, rm, r, un, unlink

卸载开发版本的模块：
npm uninstall gulp --save-dev







## 更新
$ sudo npm install npm -g
//更新npm版本

$ npm update <package>
把当前目录下node_modules子目录里边的对应模块更新至最新版本。

$ npm update <package> -g
把全局安装的对应命令行程序更新至最新版。








## 列出
$ npm ls 
aliases: list, la, ll

查看全局安装的模块：
$ npm list -g

查看某个模块的版本号
$ npm list xxx





## 初始化项目

npm init 
该命令在项目中引导创建一个package.json文件

安装包的信息可保持到项目的package.json文件中

方便后续的项目开发者或用户使用

npm init [-f|--force|-y|--yes]




## 注册发布

在package.json所在目录下使用npm install . -g可先在本地安装当前命令行程序，可用于发布前的本地测试。


在项目init之后 可以
$ npm adduser
$ npm publish

npm unpublish <package>@<version>
可以撤销发布自己发布过的某个版本代码。








## Package.json 属性说明

name - 包名。

version - 包的版本号。

description - 包的描述。

homepage - 包的官网 url 。

author - 包的作者姓名。

contributors - 包的其他贡献者姓名。

dependencies - 依赖包列表。如果依赖包没有安装，npm 会自动将依赖包安装在 node_module 目录下。

repository - 包代码存放的地方的类型，可以是 git 或 svn，git 可在 Github 上。

main - main 字段指定了程序的主入口文件，require('moduleName') 就会加载这个文件。这个字段的默认值是模块根目录下面的 index.js。

keywords - 关键字