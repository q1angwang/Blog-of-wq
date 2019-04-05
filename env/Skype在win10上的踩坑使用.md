# Skype在win10上的踩坑使用


## 缘起：
海外高校导师需要Skype进行视频面试。




## 0. win10自带
自带的是Skype for business：  
![](skype-for-business.png)


使用outlook账号，一直显示"正在连接服务器饼登陆"，并在等待后报错：  
![](skype-for-business-error.png)

关注下登陆地址后的一行话
![](skype-for-business-need-organization.png)

是个典型的问题
![](skype-for-business-need-organization1.png)

解决：

    请问你是使用自己的微软账号登录，还是用公司提供的 Office 365 账号登录？

    如果用的是微软账号，那么只能登录 Skype，是无法登录 Skype for Business 的。





## 安装

在官网1 <https://www.skype.com/zh-Hans/get-skype/> 贴出的获取地址会跳转到Microsoft store 【ms-windows-store://pdp/?productid=9WZDNCRFJ364&cid=scom-web-store】

所安装的Store版Skype在xd校园网/xian联通4G网测试下，均不可以登陆成功。

![](skype-store-round.png)

![](skype-store-error.png)



## 换用baidu下载的安装包解决了

官网2 <http://skype.gmw.cn/down/>  
可以直接得到安装包，正常登陆正常通话正常视频。  
谢[skyel1u](http://skyel1u.github.io)师傅





## 其他
- Windows叫Microsoft store，你说AppStore别人会误解你所在的平台。

- 紧急(建立)联系可以通过<https://web.skype.com>网页版获得服务，网页版无法语音视频。

- 借着使用了Microsoft store，学习下UWP应用的概念<>。