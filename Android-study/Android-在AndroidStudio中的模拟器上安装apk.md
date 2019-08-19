# 在AndroidStudio中的模拟器上安装apk

- 运行模拟器 -> 将需安装的App.apk拖到模拟器屏幕
- 使用`$ adb install xxx.apk`

## 部分报错
在模拟器安装apk时，部分无法安装，报错：
![]()

但是安装有些apk却可以正常安装，这是由于安装的APP中使用了与当前CPU架构不一致的native libraries,所以导致报错，因为现在绝大多数的智能手机还都是采用ARM架构的，虽然android是支持ARM和x86架构，但是它们的指令集是有差别的，APP在开发的时候使用的是ARM的本地库，而我们在用AVD创建模拟器的时候使用的是x86的CPU，因此导致报错。所以，如果APP是在x86架构下编译的我们就创建x86cpu的模拟器，如果APP是在ARM架构编译的我们就创建ARMcpu的模拟器。所以我们先看一下我们的模拟器是什么CPU架构，在AVDManager中查看：

