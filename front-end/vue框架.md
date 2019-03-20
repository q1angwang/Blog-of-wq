# vue框架

Vue (读音 /vjuː/，类似于 view) 是一套用于构建用户界面的渐进式框架。



### 特点
Vue 的核心库只关注视图层，不仅易于上手，还便于与第三方库或既有项目整合。

另一方面，当与现代化的工具链以及各种支持类库结合使用时，Vue 也完全能够为复杂的单页应用提供驱动。

cc





## 官方介绍

<https://cn.vuejs.org/v2/guide/index.html#>








## 框架安装步骤

1. 官网下载node.js对应的版本，进行安装
    //sudo apt install nodejs
2. nodejs -v
3. npm -v
4. npm install -g cnpm –registry=http://registry.npm.taobao.org
npm阿里镜像
5. npm install -g vue-cli
6. cnpm install webpack -g //打包工具

## Hello World 项目
1. 新建vue项目，获取路径和项目及其所在的项目文件夹，为后续安装准备工作
2. vue init webpack firstvue
    不断输 y










## 使用技巧

### 本地调试vue：
    npm run serve

### 发布：
    npm run build

### 发布的dict文件夹
`python -m http.server`在本地开个服务器就能看效果了


### 本地vue.js项目调试的默认端口
默认端口：`8080`
修改/firstvue/config/index.js下的`port`   