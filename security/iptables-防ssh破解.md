# iptables-防ssh破解

关键词：入侵排查 ssh安全 爆破管控



服务器是使用密码登陆时，可以关注登陆日志

查看命令(centos)：

    cat /var/log/auth.log
    cat /var/log/secure
    报警：Failed password for root XXX.XXX.XXX.XXX；
    额外可以查看auth.log文件大小



查看哪些ip尝试暴破ssh：
    
    grep "Failed password for root" /var/log/auth.log | awk '{print $11}' | sort | uniq -c | sort -nr | more 


防暴力破解的命令：

    iptables -I INPUT -p tcp --dport 22 -i eth0 -m state --state NEW -m recent --set
对于外来TCP协议数据，端口号22，网络接口是eth0，状态是新连接，那么把它加到最近列表中

    iptables -I INPUT -p tcp --dport 22 -i eth0 -m state --state NEW -m recent --update --seconds 60 --hitcount 4 -j DROP
对于这样的连接，如在最近列表中，并且在60s内连接>=四次，那么丢弃该数据。
其中-m是模块的意思。

合：
有人从一个 IP 一分钟内连接尝试四次 ssh 登录的话，那么它就会被加入黑名单，后续连接将会被丢弃。




其他安全设置例如修改ssh端口，禁止root用户登录，禁止密码登录也可以让vps更安全,可参考这里.
https://blog.phpgao.com/vps_ssh.html


# vim /etc/ssh/sshd_config
PermitRootLogin no





# refer：
https://www.secbug.net/technologys/148.html

https://blog.phpgao.com/vps_ssh.html

https://blog.fazero.me/2015/08/13/利用iptables防止ssh暴力破解/