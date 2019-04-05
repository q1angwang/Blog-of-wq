# SSL配置说明 (apache服务器)







## 前置知识

    ssl openssl https 证书 pem文件与crt文件 dns


### 如何查看apache配置文件httpd.conf路径

    $ httpd -V
    $ apache2 -V
输出中的`HTTPD_ROOT`和`SERVER_CONFIG_FILE`可确定httpd.conf路径


Apache的主配置文件：
Apache在启动时会自动读取这个文件的配置信息。其他的一些配置文件，如 httpd.conf等，则是通过`Include`指令包含进来(在apache2.conf中可以找到这些Include行)。

    /etc/httpd/conf/httpd.conf
    /etc/apache2/httpd.conf
    /etc/apache2/apache2.conf //Ubuntu的Apache

    $ wc -l /etc/httpd/conf/httpd.conf 
    1009 /etc/httpd/conf/httpd.conf 
    //内容较多，wc命令统计一共有1009行，其中大部分是以#开头的注释行。

默认站点主目录：

    /var/www/html/




### 虚拟目录典型配置

    <VirtualHost *:443>
     ServerName servername443
     ServerAlias servername443

     SSLEngine on
     SSLProtocol all -SSLv2 -SSLv3
     SSLCipherSuite HIGH:!RC4:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!EXP:+MEDIUM
     SSLHonorCipherOrder on

     SSLCertificateFile /etc/apache2/cert/1899820_waf.qiangwang.site_public.crt
     SSLCertificateKeyFile /etc/apache2/cert/1899820_waf.qiangwang.site.key
     SSLCertificateChainFile /etc/apache2/cert/1899820_waf.qiangwang.site_chain.crt

     DocumentRoot /var/www/html/

     <Directory />
     Options FollowSymLinks
     AllowOverride None
     </Directory>
    </VirtualHost>





### 数字证书格式转换：.key和.crt转换成.pem格式

.key 转换成 .pem：

    openssl rsa -in temp.key -out temp.pem


.crt 转换成 .pem：

    openssl x509 -in tmp.crt -out tmp.pem




### apache安装目录下文件夹意义
/sites-available：该目录存放的是可用的虚拟主机；

/sites-enabled：该目录存放的是已经启用的虚拟主机。




<!------------------------------------------------------------>







## 购买
在阿里云CA证书中心购买Symantec的SSL服务











<!------------------------------------------------------------>













## 获取阿里云提供的密钥

0. 登录阿里云[SSL证书控制台](https://yundunnext.console.aliyun.com/?spm=a2c4g.11186623.2.9.301615a1S79XxQ&p=casnext#/overview/cn-hangzhou)。


1. 在SSL证书页面，点击已签发标签，并下载证书文件(压缩包)。

    ![](http://static-aliyun-doc.oss-cn-hangzhou.aliyuncs.com/assets/img/66001/155188178639177_zh-CN.jpg)

2. 在证书下载选择Apache服务器，并将Apache版证书压缩包下载到本地。

3. 解压Apache证书，并将Apache证书、证书链和秘钥文件上传到服务器的Apache安装目录中下的cert目录（没有这个目录就手动新建一个）

    $ mkdir /etc/apache2/cert




## 在apache服务器上配置密钥

0. 打开Apache/conf/httpd.conf，查看是否加载ssl模块，找到以下参数删除行首的配置语句注释符号“#”，并保存修改

    `#LoadModule ssl_module modules/mod_ssl.so `    
    `#用来加载mod_ssl.so模块以启用SSL服务；Apache默认不启用该模块。如找不到该配置，请重新编译mod_ssl模块`
    `#Include conf/extra/httpd-ssl.conf`

启用SSL模块也可以:
    $ sudo a2enmod ssl

这条命令相当于:
sudo ln -s /etc/apache2/mods-available/ssl.load /etc/apache2/mods-enabled 
sudo ln -s /etc/apache2/mods-available/ssl.conf /etc/apache2/mods-enabled

或者：
vi /etc/apache2/mods-available/ssl.load 
LoadModule ssl_module /usr/lib/apache2/modules/mod_ssl.so

SSL模块启用后可执行`ls /etc/apache2/sites-available`查看目录下生成的`default-ssl.conf`文件。

443端口是网络浏览端口，主要用于HTTPS服务。SSL模块启用后会自动放行443端口。若443端口未自动放行，可执行`vi /etc/apache2/ports.conf`并添加 `Listen 443`手动放行。






1. 打开服务器上的Apache/conf/extra/httpd-ssl.conf配置文件，找到以下参数配置后保存。

    `SSLProtocol all -SSLv2 -SSLv3    `
    `SSLCipherSuite HIGH:!RC4:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!EXP:+MEDIUM  `  
    `SSLHonorCipherOrder on`
    `SSLCertificateFile cert/domain name_public.crt  `  
    `SSLCertificateKeyFile cert/domain name.key`    
    `SSLCertificateChainFile cert/domain name_chain.crt `  
 
# 添加 SSL 协议支持协议，去掉不安全的协议
SSLProtocol all -SSLv2 -SSLv3
# 修改加密套件如下
SSLCipherSuite HIGH:!RC4:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!EXP:+MEDIUM
SSLHonorCipherOrder on
# 证书公钥配置
SSLCertificateFile cert/public.pem
# 证书私钥配置
SSLCertificateKeyFile cert/3984897660442.key
# 证书链配置
SSLCertificateChainFile cert/chain.pem



修改ssl配置文件：
vi /etc/apache2/mods-available/ssl.load 
添加一行 
SSLProtocol all -SSLv2 -SSLv3 









运行以下命令修改SSL配置文件default-ssl.conf。

    vi /etc/apache2/sites-available/default-ssl.conf

在default-ssl.conf文件中找到以下参数进行修改后保存并退出。
 
    <IfModules mod_ssl.c>
    <VirtualHost *:443>  
    ServerName 
    #修改为证书绑定的域名www.YourDomainName.com。
    SSLCertificateFile /etc/apache2/www.YourDomainName_public.crt 
    #将/etc/apache2/www.YourDomainName.com_public.crt替换为证书文件路径+证书文件名。
    SSLCertificateKeyFile /etc/apache2/www.YourDomainName.com.key  
    #将/etc/apache2/www.YourDomainName.com.key替换为证书秘钥文件路径+证书秘钥文件名。
    SSLCertificateChainFile /etc/apache2/www.YourDomainName.com_chain.crt  
    #将/etc/apache2/www.YourDomainName.com_chain.crt替换为证书链文件路径+证书链文件名。

default-ssl.conf文件可能存放在 /etc/apache2/sites-available或 /etc/apache2/sites-enabled目录中。

运行以下命令把default-ssl.conf映射至/etc/apache2/sites-enabled文件夹中建立软链接、实现二者之间的自动关联。

sudo ln -s /etc/apache2/sites-available/default-ssl.conf /etc/apache2/sites-enabled/001-ssl.conf








2. 重启Apache服务器使SSL配置生效。

    命令如下：  

    `$ /usr/local/apache2/bin/apachectl restart apache`

    `$ sudo /etc/init.d/apache2 force-reload`//重新加载Apache 2配置文件。
    `$ sudo /etc/init.d/apache2 restart`



3. 测试 https://yourdomain.com

浏览器地址栏显示绿色的小锁标识说明证书安装成功。








<!------------------------------------------------------------>







## 需要注意

0. 对应架设网站的服务器需要开启端口白名单(80和443是两个端口) 
    控制台添加安全组规则

1. 网站使用https后网页中所有引用都要使用https，不然浏览器会出现警告，且默认不加载http的文件


















<!-- 
【关于一个服务器配置多个https域名的处理】

参考资料：https://www.cnblogs.com/shaoyikai/p/4235690.html

使用通配符证书，此证书需要到专门的证书颁发机构购买。
使用普通证书，配置apache的ssl主机头（需要apache版本支持）。



第一种
通配符证书往往价格比较贵，对一些大公司很适合。而对于很多小站长来说，使用普通证书可以省下来很多费用。

配置方法较简单，和http网站虚拟主机类似，只不过这些网站公用一个证书。

证书安装方式，可以咨询证书颁发机构，或者自己配置IIS或Apache等服务器软件。






第二种
假如有2个域名aaa.com和bbb.com。

首先，购买两个域名相应的证书。

其次，配置httpd-ssl.conf文件，举例：

    Listen 443

    SSLCipherSuite HIGH:MEDIUM:!aNULL:!MD5
    SSLPassPhraseDialog  builtin
    SSLSessionCache        "shmcb:C:/wamp/bin/apache/apache2.4.9/conf/ssl/logs/ssl_scache(512000)"
    SSLSessionCacheTimeout  300

    <VirtualHost _default_:443>
        DocumentRoot "c:/wamp/www/aaa"  #网站根目录
        ServerName aaa.com:443    #主机名
        ServerAdmin admin@aaa.com  #管理员邮箱

        ErrorLog "C:/wamp/bin/apache/apache2.4.9/logs/error_aaa.log"
        TransferLog "C:/wamp/bin/apache/apache2.4.9/logs/access_aaa.log"

        SSLEngine on
        #注意以下证书文件路径！！！
        SSLCertificateFile "C:/wamp/bin/apache/apache2.4.9/conf/ssl_aaa/public.crt"
        SSLCertificateKeyFile "C:/wamp/bin/apache/apache2.4.9/conf/ssl_aaa/private.key"
        SSLCACertificateFile "C:/wamp/bin/apache/apache2.4.9/conf/ssl_aaa/ca-bundle.crt"
    </VirtualHost>  

    <VirtualHost _default_:443>
        DocumentRoot "c:/wamp/www/bbb"  #网站根目录
        ServerName bbb.com:443    #主机名
        ServerAdmin admin@aaa.com  #管理员邮箱

        ErrorLog "C:/wamp/bin/apache/apache2.4.9/logs/error_bbb.log"
        TransferLog "C:/wamp/bin/apache/apache2.4.9/logs/access_bbb.log"

        SSLEngine on

        #注意以下证书文件路径！！！
        SSLCertificateFile "C:/wamp/bin/apache/apache2.4.9/conf/ssl_bbb/public.crt"
        SSLCertificateKeyFile "C:/wamp/bin/apache/apache2.4.9/conf/ssl_bbb/private.key"
        SSLCACertificateFile "C:/wamp/bin/apache/apache2.4.9/conf/ssl_bbb/ca-bundle.crt"

        <FilesMatch "\.(cgi|shtml|phtml|php)$">
            SSLOptions +StdEnvVars
        </FilesMatch>

        <Directory "C:/wamp/bin/apache/apache2.4.9/cgi-bin">
            SSLOptions +StdEnvVars
        </Directory>

        BrowserMatch "MSIE [2-5]" \
                 nokeepalive ssl-unclean-shutdown \
                 downgrade-1.0 force-response-1.0

        CustomLog "C:/wamp/bin/apache/apache2.4.9/logs/ssl_request.log" \
                  "%t %h %{SSL_PROTOCOL}x %{SSL_CIPHER}x \"%r\" %b"
    </VirtualHost>
简单些理解，就是配置多个<VirtualHost _default_:443></VirtualHost>，跟vhosts.conf文件配置多个http域名类似。

 -->




# 参考
https://help.aliyun.com/document_detail/102450.html

[官方文档"在Apache服务器上安装SSL证书"](
https://help.aliyun.com/document_detail/98727.html?spm=a2c4g.11186623.2.27.4c122de9arbaZ9#concept-zsp-d1x-yfb)



<br>

> 本文作者： 强王  
> 本文标题： SSL配置说明  
> 发布时间： CST - 2019/3/8 - 23:58  
> 版权声明： 本文由 强王 原创，采用 保留署名-非商业性使用-禁止演绎 4.0-国际许可协议   
> 转载请保留以上声明信息！  