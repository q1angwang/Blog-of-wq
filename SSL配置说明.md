# SSL配置说明 (apache服务器)

## 前置知识

    ssl openssl https 证书 pem文件与crt文件 dns



## 购买
在阿里云CA证书中心购买Symantec的SSL服务


## 获取阿里云提供的密钥

0. 登录阿里云[SSL证书控制台](https://yundunnext.console.aliyun.com/?spm=a2c4g.11186623.2.9.301615a1S79XxQ&p=casnext#/overview/cn-hangzhou)。


1. 在SSL证书页面，点击已签发标签，并下载证书文件(压缩包)。

    ![](http://static-aliyun-doc.oss-cn-hangzhou.aliyuncs.com/assets/img/66001/155188178639177_zh-CN.jpg)





2. 在证书下载选择Apache服务器，并将Apache版证书压缩包下载到本地。




3. 解压Apache证书，并将Apache证书、证书链和秘钥文件上传到服务器的Apache安装目录中下的cert目录（没有这个目录就手动新建一个）




## 在apache服务器上配置密钥

0. 打开Apache/conf/httpd.conf，找到以下参数进行配置并保存


```shell
#LoadModule ssl_module modules/mod_ssl.so   
#删除行首的配置语句注释符号“#”加载mod_ssl.so模块启用SSL服务，Apache默认是不启用该模块的。如果找不到该配置，请重新编译mod_ssl模块。
#Include conf/extra/httpd-ssl.conf   删除行首的配置语句注释符号“#”。
```

1. 打开服务器上的Apache/conf/extra/httpd-ssl.conf配置文件，找到以下参数配置后保存。

```
    SSLProtocol all -SSLv2 -SSLv3    
    SSLCipherSuite HIGH:!RC4:!MD5:!aNULL:!eNULL:!NULL:!DH:!EDH:!EXP:+MEDIUM    
    SSLHonorCipherOrder on
    SSLCertificateFile cert/domain name_public.crt    
    SSLCertificateKeyFile cert/domain name.key    
    SSLCertificateChainFile cert/domain name_chain.crt   
```


2. 重启Apache服务器使SSL配置生效。

命令如下：  

```  
    $ /usr/local/apache2/bin/apachectl restart apaceh
```

3. 测试https://yourdomain.com


<br>

> 本文作者： 强王  
> 本文标题： SSL配置说明  
> 发布时间： 2019年3月8日 - 23时30分  
> 版权声明： 本文由 强王 原创，采用 保留署名-非商业性使用-禁止演绎 4.0-国际许可协议   
> 转载请保留以上声明信息！  