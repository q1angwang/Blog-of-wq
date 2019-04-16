# ubuntu-mysql

###安装 
sudo apt install mysql-server

### 启停
$ mysqld start
$ mysql.server start 
$ mysql.server stop
$ mysql.server restart
$ sudo /usr/local/mysql/support-files/mysql.server start

$ service mysqld start
$ service mysqld stop
$ service mysqld restart




### 状态
$ service mysqld status
$ systemctl status mysqld.service
    //systemctl是一个systemd工具，主要负责控制systemd系统和服务管理器
$ ps -ef | grep mysqld



### 配置文件
查看配置文件 my.cnf 的位置
$ whereis my.cnf
输出： my: /etc/my.cnf
编辑
$ vi /etc/my.cnf

### 错误日志
log_error=/var/log/mysqld.log 的配置，通过命令 tail -25 /var/log/mysqld.log 查看 MySQL 错误日志










# 数据库语句

show databases;

create database if not exists test;

drop database fk;

show tables from test;

use test;

 8 create table tb_dept(
 9     Id int primary key auto_increment,#部门编号 整形 主键 自增长
10     Name varchar(18),#部门名称
11     description varchar(100)#描述
12 );
13 
14 show tables from test;
15 
16 desc tb_dept;#查看表信息
17 
18 show create table tb_dept;
19 
20 use test;
21 #员工表
22 create table tb_emp(
23 id int primary key auto_increment,#auto_increment只是MySQL特有的
24 Name varchar(18),
25 sex varchar(2),
26 age int,
27 address varchar(200),
28 email varchar(100)
29 );
31 drop table tb_dept;
32 #修改列类型
33 #注意：不是任何情况下都可以去修改的，
34 #只有当字段只包含空值时才可以修改。
35 alter table tb_emp modify sex  varchar(4);
36 #增加列
37 alter table tb_emp add tel varchar(12);
38 #删除列
39 alter table tb_emp drop tel;
40 alter table tb_emp drop column tel;
41 #列改名
42 alter table tb_emp change Name emp_Name varchar(18);
43 #更改表名
44 alter table tb_emp rename emp;
45 rename table emp to tb_emp;
46 
47 insert into dept_emp (Name,sex,age,address,email)values('','','','','');
48 
49 #约束
50 #是在表上强制执行地数据校验规则，主要用于保证数据库地完整性
51 /*
52 not null 
53 unique 唯一键tb_depttb_dept
54 primary key 
55 foreign key 外键
56 check 检查
57 */
58 
59 create table tb_emp(
60 id int primary key auto_increment,
61 Name varchar(18),
62 sex varchar(2) default'男' check(sex='男'or sex='女'),#表级写法check 在mysql中不起作用
63 age int,
64 address varchar(200),
65 email varchar(100) unique,
66 dept_id int,#references tb_dept(id) #表级写法外键不起作用
67 constraint foreign key fk_emp(dept_id) references tb_dept(id)
68 );
69 
70 #创建表之后在添加
71 alter table tb_emp add constraint foreign key fk_emp(dept_id) references tb_dept(id);


# 报错
1. Failed to start mysqld.service: Unit mysqld.service not found.

$ systemctl enable mysql.service 


$ chkconfig --list
```BASH
-bash-4.2# chkconfig --list

Note: This output shows SysV services only and does not include native
      systemd services. SysV configuration data might be overridden by native
      systemd configuration.

      If you want to list systemd services use ‘systemctl list-unit-files‘.
      To see services enabled on particular target use
      ‘systemctl list-dependencies [target]‘.

aegis           0:off   1:off   2:on    3:on    4:on    5:on    6:off
agentwatch      0:off   1:off   2:on    3:on    4:on    5:on    6:off
iprdump         0:off   1:off   2:on    3:on    4:on    5:on    6:off
iprinit         0:off   1:off   2:on    3:on    4:on    5:on    6:off
iprupdate       0:off   1:off   2:on    3:on    4:on    5:on    6:off
jexec           0:off   1:on    2:on    3:on    4:on    5:on    6:off
mysql.server    0:off   1:off   2:on    3:on    4:on    5:on    6:off
```
服务名不是mysqld 而是 mysql.server
service mysql.server restart 









### refer
一个报错解决
https://github.com/jaywcjlove/mysql-tutorial/blob/master/chapter2/2.3.md#启动报错处理
