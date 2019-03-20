# node.js


## 简介

简单的说 Node.js 就是运行在服务端的 JavaScript。
Node.js 是一个基于Chrome JavaScript 运行时建立的一个平台。
Node.js 是一个事件驱动I/O服务端JavaScript环境，基于Google的V8引擎，V8引擎执行Javascript的速度非常快，性能非常好。


## 使用场景

前端程序员想创建自己的服务，使用Node.js

需要部署一些高性能的服务

如使用PHP来编写后端的代码时，需要Apache 或者 Nginx 的HTTP 服务器，并配上 mod_php5 模块和php-cgi。此时"接收 HTTP 请求并提供 Web 页面"的需求使用 PHP 来处理是非必要的。

对 Node.js 来说，概念不一样。使用 Node.js 时，我们不仅仅在实现一个应用，同时还实现了整个 HTTP 服务器。


















## Helloworld

### 交互模式
Node.js REPL(Read Eval Print Loop:交互式解释器) 


    $ nodejs
    >
ctrl-d 退出

使用变量：    
- 变量声明需要使用 var 关键字，如果没有使用 var 关键字变量会直接打印出来。
-  var 关键字的变量可以使用 console.log() 来输出变量。



#### REPL 命令

ctrl + c - 退出当前终端。

ctrl + c 按下两次 - 退出 Node REPL。

ctrl + d - 退出 Node REPL.

向上/向下 键 - 查看输入的历史命令

tab 键 - 列出当前命令

.help - 列出使用命令

.break - 退出多行表达式

.clear - 退出多行表达式

.save filename - 保存当前的 Node REPL 会话到指定文件

.load filename - 载入当前 Node REPL 会话的文件内容。








### 脚本模式

    $ node helloworld.js
    console.log("Hello World");





















## 典型的nodesjs应用——HTTP服务

1. 引入 required 模块

2. 创建服务器，用于监听客户端的请求

3. 接收请求与响应请求


具体：

用`require`指令载入 Node.js 的`HTTP`模块，并将实例化的 HTTP 赋值给变量 http。

使用 http.createServer() 方法创建服务器，并使用 listen 方法绑定 8888 端口。 函数通过 request, response 参数来接收和响应数据。

http 模块提供的函数： createServer 。这个函数会返回 一个对象，这个对象有一个叫做 listen 的方法，这个方法有一个数值参数， 指定这个 HTTP 服务器监听的端口号。

```JS
var http = require('http');

http.createServer(function (request, response) { 
    response.writeHead(200, {'Content-Type': 'text/plain'});// 发送 HTTP 头部 ；HTTP 状态值: 200 : OK ；内容类型: text/plain
    response.end('Hello World\n');// 发送响应数据 "Hello World"
}).listen(8888);

console.log('Server running at http://127.0.0.1:8888/');
// 终端打印：
````

```SH
node server.js
Server running at http://127.0.0.1:8888/
```
