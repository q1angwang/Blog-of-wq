# Android-如何从Win10完全卸载Android Studio？

这个需求源自一次莫名其妙的SDK找不到，下载的SDK解压后AS不识别，该文档解决重装后的清理附属程序的需求。

## 步骤
1. 运行卸载程序

    “ 控制面板”，然后在“ 程序”下选择“ 卸载程序” 。 之后，点击“Android Studio”，然后按卸载 。 如果有多个版本，请将其一起卸载。

2. 删除附属文件

要删除Android-Studio设置文件的任何遗留物，请在文件资源管理器中，转到您的用户文件夹（ `%USERPROFILE%`），并删除`.android` ， `.AndroidStudio`和其他版本的任何类似目录，即`.AndroidStudio1.2`、`.gradle`和`.m2`等

然后转到`%APPDATA%`并删除`JetBrains`目录。
最后，转到C:\Program Files并删除`Android`目录。


3. 删除SDK

要删除SDK的剩余部分，请转至`%LOCALAPPDATA%`并删除Android目录。


4. Android Studio项目
AS默认在`%USERPROFILE%\AndroidStudioProjects`文件夹中创建项目，根据需要进一步操作。

