# ubuntu lamp apache

    $ sudo apt-get install apache2 php
    $ apache2 -v
    $ php -v
    $ cat /etc/apache2/mods-enabled/phpxxxxx.load
    //若无，安装sudo apt-get install libapache2-mod-php 

    $ sudo apt-get install mysql-server php-mysql
    $ cat /etc/php/7.0/mods-available/mysqli.ini
    $ cat /etc/php5/conf.d/mysql.ini

    $ sudo service mysql restart
    $ sudo service apache2 restart


也可使用一条命令：

    sudo apt-get install apache2 php mysql-server php-mysql
    sudo tasksel  install lamp-server
