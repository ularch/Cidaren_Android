## 词达人自动刷题脚本
`词达人自动过班级任务,自学任务`
- 可在手机Termux软件运行
- 自动过自学任务
- 过班级任务
- 随时可能失效,**且用且珍惜**
- 可选择过某一章节
- 得分95+（异常情况下可能90+） 


## 介绍

+ 在原有源码的基础上添加了手动选择特定任务功能
+ 将token等设置从config文件改为了在控制台输入
+ 可自定义选择每一题之间的刷题间隔
+ 将源代码进行适配，可在termux运行
+ Windows可视化GUI版见[ularch/Cidaren Automatic Answers](https://github.com/ularch/Cidaren_Automatic_Answer)

<!-- <details> <summary> <b>日志(点击查看进程)</b> </summary>

</details> -->


## 声明
本项目初始源码来源自 [github123666/cidaren](https://github.com/github123666/cidaren)

**遵循MIT协议,仅供学习参考。**

### **删除请联系harold.lach.lei@gmail.com**

## 使用方法
安装termux
更新已安装软件包
```angular2html
pkg upgrade
```
换清华源
```angular2html
sed -i 's@^\(deb.*stable main\)$@#\1\ndeb https://mirrors.tuna.tsinghua.edu.cn/termux/apt/termux-main stable main@' $PREFIX/etc/apt/sources.list
apt update && apt upgrade
```
下载必要工具
```angular2html
pkg install python vim -y
```
获取访问内部储存权限
```angular2html
termux-setup-storage
```
安装必要库 
```angular2html
pip install requests
```
下载该程序源码，解压、复制源码位置（建议放在download文件夹下）
进入源码文件夹
```angular2html
cd <源码所在文件夹地址>
```
运行程序
```angular2html
python main.py
```
开始愉快的使用吧！

+ 电脑端取token可使用[ularch/Cidaren Automatic Answers](https://github.com/ularch/Cidaren_Automatic_Answer) get token文件夹下的词达人token获取.exe快速获取
+ 手机获取token可使用ProxyPin等抓包软件，此处不做讲解（可能会出获取方法）
