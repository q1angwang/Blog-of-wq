# Anaconda
Anaconda是一个包含180+的科学包及其依赖项的发行版本。其包含的科学包包括：conda, numpy, scipy, ipython notebook等。





## conda
conda是包及其依赖项和环境的管理工具。 

- 适用语言：Python, R, Ruby, Lua, Scala, Java, JavaScript, C/C++, FORTRAN。  
- 适用平台：Windows, macOS, Linux  
- 用途：  
    ① 快速安装、运行和升级包及其依赖项。  
    ② 在计算机中便捷地创建、保存、加载和切换环境。  
    
    如果你需要的包要求不同版本的Python，你无需切换到不同的环境，因为conda同样是一个环境管理器。仅需要几条命令，你可以创建一个完全独立的环境来运行不同的Python版本，同时继续在你常规的环境中使用你常用的Python版本。——Conda官方网站  

- conda为Python项目而创造，但可适用于上述的多种语言。

- conda包和环境管理器包含于Anaconda的所有版本当中。    

- conda结合了pip和virtualenv的功能。    
 






## 验证conda已安装
    
    conda --version
终端上将会以 conda 版本号的形式显示当前安装conda的版本号。如： conda 3.11.0


如若默认设置环境变量未成功，也可自行进行设置:`$ vim ~/.bash_profile`，在文件末尾添加：`
export PATH="/Users/MyungHo/anaconda/bin:$PATH"`，然后退出vim使变量生效：`$ source ~/.bash_profile`


## 源
Anaconda的服务器在国外，导致使用conda命令安装应用包时偶有发生速度巨慢的现象，所幸国内清华大学TUNA镜像源中有Anaconda仓库的镜像可供使用

<https://mirrors.tuna.tsinghua.edu.cn/help/anaconda/>

    $ cp ~/.condarc{,.bak}
    # 快速创建channels配置文件的备份
    $ conda config --add channels  https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
    $ conda config --set show_channel_urls yes
查看是否配置成功

    $ cat ~/.condarc
    $ conda config --show-sources


## 更新conda
    conda update conda

## 卸载conda
 

    $ conda deactivate  #退出所有环境。
    # 清理 .bashrc、/etc/profile.d 中有关 conda 的启动脚本、环境变量。
    $ rm -rf ~/anaconda3
Linux 或 macOS删除Anaconda安装目录即可。



















## 管理环境
可视化直接管理即可，使用Anaconda Navigator

注意：此时以及下面创建的python2或其他环境是py本身的，并没有带Spyder的IDLE。  
如果需要对应的Spyder(以一个python2.7的名字叫python2的env为例)：
    
    conda install -n python2 spyder
    conda install -n python2 jupyter
    activate python2
    spyder
    jupyter notebook


显示已创建环境：

    conda info --envs
    conda info -e
    conda env list

创建新环境：

    conda create --name <env_name> <package_names>
    conda create --name python2 python=2.7 
    conda create -n python3 python=3.5 numpy pandas
新创建的环境将会被保存在 `/Users/<user_name>/anaconda3/env` 目录下

复制环境：

    conda create --name <new_env_name> --clone <copied_env_name>
    conda create --name py2 --clone python2

切换环境：

    linux:
    source activate <env_name>          
    source deactivate
    windows:
    activate <env_name>               
    deactivate

    conda activate <env_name>
    conda deactivate

删除环境：

    conda remove -n <env_name>
    conda remove --name <env_name> --all 

<!-- 环境嵌套:
当已经激活某个环境时，再次 conda activate envname 将发生环境嵌套，而不是切换。

多个环境嵌套时，软件包可能产生异常行为。

Python 需格外小心！若最内层环境没有安装 Python，所有与 Python 有关的程序（尤其是 pip ）将逐层向外 fallback 直至 base，很容易造成污染。

可通过 conda info 的 shell level 来检查嵌套情况。

如非特别必要，不建议使用环境嵌套。

默认允许 2 层环境嵌套，可通过 conda config --set max_shlvl number 调至更高或将该特性关闭。
 -->

















# 共享环境

共享环境非常有用，能让他人同步你代码中所用的包，并确保其版本正确。在github上共享代码时，最好同样创建环境文件并将其包括在代码库中。方便他人安装代码的所有依赖项。

在当前的所在环境存为YAML文件（包括python版本和所有的包名称）：
    
    conda env export > environment.yaml

其他电脑上使用：
    
    source activate xxxx
    conda env update -f=environment.yaml
    # 更新xxxx所在的环境

不使用conda的用户，还可以使用 `pip freeze > environment.txt` 将一个txt文件导出并包括在其中。

[参考pip官方](https://pip.pypa.io/en/stable/reference/pip_freeze/)

    $ env1/bin/pip freeze > requirements.txt
    $ env2/bin/pip install -r requirements.txt





















## 包管理

列出：

    conda list


查找安装：

    conda search --full-name <package_full_name>
    conda search <text> #模糊查找

    conda install <package_name> #在当前环境中安装包
    # 当使用 conda install 无法进行安装时，可以使用pip进行安装。例如：see包。但pip只是包管理器，无法对环境进行管理。想在指定环境安装包，需先切换到指定环境中，再使用pip。

    conda install --name <env_name> <package_name>
    conda install --name python2 pandas 
    # conda install 无法进行安装时，可以考虑从http://Anaconda.org中获取安装包的命令


卸载：

    conda remove --name <env_name> <package_name> #卸载指定环境中的包

更新：

    conda update conda 
    # 先更新conda再更新其他包
    # 不要更新 anaconda 元包，这将导致大量软件包回滚到最近一个 Anaconda 发行版中冻结的过时版本。
    conda update <package_name>
    conda upgrade <package_name>   #--all






# 官方文档：
<https://conda.io/en/latest/>