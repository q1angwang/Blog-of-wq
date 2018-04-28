# Github Pages

<i style="color:grey">Last Updated: 2017-12-1</i>  
<script async src="//dn-lbstatics.qbox.me/busuanzi/2.3/busuanzi.pure.mini.js"></script>
<span id="busuanzi_container_page_pv" style="float:right;">
  Page views: <span id="busuanzi_value_page_pv"></span>
</span><br>







Github Pages 是 github 公司提供的免费静态网站托管服务，方便且功能强大，无空间限制，可绑定自己的域名。



## 1.新建仓库
仓库名字为：username.github.io 。注意严格替换GitHub注册时的用户名。

然后就往仓库里面放页面内容(github为你解析静态页面，包含css js)。

可参考官方文档：[Websites for you and your projects.](https://pages.github.com/)

    ~ $ git clone https://github.com/username/username.github.io
    ~ $ cd username.github.io
    ~ $ echo "Hello World" > index.html
    ~ $ git add --all
    ~ $ git commit -m "Initial commit"
    ~ $ git push -u origin master

then: Fire up a browser and go to <https://username.github.io>



## 2. 个人域名
用户主页/项目主页，可用github的二级域名或是个人域名。要在master分支（用户主页）或gh-pages分支（项目页面）的根目录下创建`CNAME`文件，内容为所用个人域名。

根目录下添加文件CNAME，内容：
    
    yourdomain.com

在个人的域名管理服务商那给自己的域名添加`A`记录指向 git-page(github的二级域名)的页面即可。DNS扩散后，该域名就可以解析到了Github page。


## 3. 404页面

需求：找不到的访问网页的页面时，弹自定义的404错误页面后跳转至首页。  

同`.gitignore`&`LICENSE` ，在项目master下添加`404.html`。  
在404页面中设置好跳转即可：

    <meta http-equiv="refresh" content="2;url=http://qiangwang.site/">


## 4. 利用github页面解析md
可以不用官方提供的jekyll渲染，md文件也会由GitHub的css解析成可视页面。
