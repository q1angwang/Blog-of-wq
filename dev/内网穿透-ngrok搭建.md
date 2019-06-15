# Ngrok搭建

## 过程记录

$ sudo apt install golang-go
$ git clone https://github.com/tutumcloud/ngrok

生成自签名证书：
//export NGROK_DOMAIN="test.qiangwang.site"
$ NGROK_DOMAIN="test.qiangwang.site"
$ openssl genrsa -out rootCA.key 2048
$ openssl req -x509 -new -nodes -key rootCA.key -subj "/CN=$NGROK_DOMAIN" -days 5000 -out rootCA.pem
$ openssl genrsa -out device.key 2048
$ openssl req -new -key device.key -subj "/CN=$NGROK_DOMAIN" -out device.csr
$ openssl x509 -req -in device.csr -CA rootCA.pem -CAkey rootCA.key -CAcreateserial -out device.crt -days 5000
$ cp rootCA.pem assets/client/tls/ngrokroot.crt
//cp rootCA.pem assets/client/tls/ngrokroot.crt  #复制rootCA.pem到assets/client/tls/并更名为ngrokroot.crt
//cp server.crt assets/server/tls/snakeoil.crt #复制server.crt到assets/server/tls/并更名为snakeoil.crt
//cp server.key assets/server/tls/snakeoil.key #复制server.key到assets/server/tls/并更名为snakeoil.key
后两步在启动时指定 -tlsCrt即可

编译：
$ GOOS=linux GOARCH=386 make release-server
$ GOOS=windows GOARCH=386 make release-client
scp -i ~/test2.pem  ubuntu@52.15.198.8:~/ngrok/bin/windows_386/ngrok.exe ./


配置域名：
在域名解析网站解析域名，解析主机记录类型为`A记录`，记录值填`vps`外网地址

    ngrock 和 *.ngrok.xxx.com

服务器启动：
$ ./bin/ngrokd -tlsKey=device.key -tlsCrt=device.crt -domain="$NGROK_DOMAIN" -httpAddr=":5000" -httpsAddr=":5001"
$ ./ngrokd -domain=test.qiangwang.site -httpAddr=":5000" -httpsAddr=":5001"
$ ./ngrokd -domain="test.qiangwang.site" -httpAddr=":5000" -httpsAddr=":5001"
$ ./ngrokd -domain="$NGROK_DOMAIN" -httpAddr=":801" -httpsAddr=":802"

客户端运行：
.\ngrok.exe -config=.\ngrok.cfg 80
.\ngrok.exe -config=.\ngrok.cfg -subdomain=test 80
.\ngrok.exe -config=ngrok.cfg start http

ngrok.cfg内容如下
    server_addr: "test.qiangwang.site:4443"
    trust_host_root_certs: false








## 相关拓展：

### 客户端配置前缀
ngrok.cfg
```json
server_addr: "test.com:8083"
trust_host_root_certs: false
tunnels:
  http:
    subdomain: "www"
    proto:
      http: "5000"
      
  https:
    subdomain: "www"
    proto:
      https: "5001"
 
  // ssh:
  //   remote_port: 2222
  //   proto:
  //     tcp: "22"
```

启动:
ngrok.exe -config ngrok.cfg start http https ssh



### 修改控制端口(-tunnelAddr)
ngrokd -domain="tunnel.test.com" -httpAddr=":8080" -httpsAddr=":8081" -tunnelAddr=":443"
server_addr: "tunnel.test.com:443"



### 服务端自启动配置
已把 ngrokd 文件拷贝到 vps 的Home目录，转移到这里：sudo mkdir /opt/ngrkd & sudo mv ngrokd /opt/ngrokd/

然后使用 systemd 设置自启动服务，
$sudo vim /lib/systemd/system/ngrokd.service
```
[Unit]
Description=ngrok server
After=network.target

[Service]
Type=simple
ExecStart=/opt/ngrokd/ngrokd -domain ngrok.xxx.com -httpAddr ":5000" -httpsAddr ":5001" -tunnelAddr ":4443" -log "/var/log/ngrokd.log"
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
启停服务

    $ sudo systemctl enable ngrokd
    $ sudo systemctl start ngrokd
    $ sudo systemctl status ngrokd
<!-- 
在这里提醒一点，我踩到了一个坑，启动客户端服务时日志 (sudo tail -f /var/log/ngrok.log) 出现报错：

[2018/02/13 01:41:28 CST] [DEBG] (ngrok/log.(*PrefixLogger).Debug:79) [view] [term] Waiting for update
[2018/02/13 01:41:28 CST] [EROR] (ngrok/log.Error:120) control recovering from failure dial tcp: lookup ngrok.xxx.com on 8.8.8.8:53: no such host

后面我在内网服务器 ping ngrok.xxx.com 提示找不到 host, 应该是 dns 的问题，nslookup ngrok.xxx.com 看了一下，果不其然，我直接把域名和 IP 写到内服务器的 /etc/hosts 文件上。

systemd 重启客户端服务之后就正常了。

最后通过 ssh -p 23333 username@ngrok.xxx.com 即可远程登录局域网内的服务器。
 -->



### 同一个服务器配置80架站和80直接访问ngrok
用nginx，配置一个server绑定`*.ngrok.qiangwang.site`域名，然后将所有ngrok域名来的请求转发到后端`:8000`端口上，完成反向代理。

nginx配置如下：

```nginx
#ngrok.qiangwang.site.conf
upstream nodejs {
    server 127.0.0.1:8000;
    keepalive 64;
}
server {
    listen 80;
    server_name *.ngrok.qiangwang.site;
    access_log /home/logs/ngrok.qiangwang.site.log;
    location / {
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header Host  $http_host:8000;
        proxy_set_header X-Nginx-Proxy true;
        proxy_set_header Connection "";
        proxy_pass      http://nodejs;
    }
}
```



### go的HTTP测试

内网PC上建立一个简单的http server 程序：hello

```go
//hello.go
package main

import "net/http"

func main() {
    http.HandleFunc("/", hello)
    http.ListenAndServe(":80", nil)
}

func hello(w http.ResponseWriter, r *http.Request) {
    w.Write([]byte("hello!"))
}

```
$ go build -o hello hello.go
$ sudo ./hello



### 关于证书

ngrok 的隧道采用 TSL 传输数据，如果使用默认证书的话任何人都可以连接你搭建的 ngrok 服务，在这里你可以去买，不过还是推荐自己生成证书。













## 问题处理：
  

1. `……(ngrok/log.(*PrefixLogger).Warn:87) [pub:483037c2] Failed to read valid http request: malformed HTTP request……`

    解：检查 ngrok.cfg 文件里的端口号是否与 Listening for control and proxy connections on [::]:4443 后的端口号一致。


2. 可能：监听端口
ngrok 默认监听 IPv6 端口，我大清自有国情，我们需要源码两处
src/ngrok/server/tunnel.go 文件中 net.ListenTCP 后面的 tcp 改为 tcp4
src/ngrok/conn/conn.go 文件中 net.Listen 后面的 tcp 改为 tcp4


3. 控制流量的端口搞错了
Listening for control and proxy connection on [::]:4443













## Refer
Official guide:
https://github.com/inconshreveable/ngrok/blob/master/docs/SELFHOSTING.md


Blog Refer:
https://zpblog.cn/linux/run-ngrok-on-your-own-server.html
https://huangwenwei.com/blogs/ngrok-ssh
https://tsukkomi.org/post/use-ngrok-to-puch-the-nat
https://blog.csdn.net/zhangguo5/article/details/77848658 一分钟启动(win server) 讲了原理
https://luozm.github.io/ngrok 搭建指南

