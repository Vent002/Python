# Python学习第一天

  ## 初识 Python

### Python简介

### 一.Python的历史

1.  1989年圣诞节，Guido von Rossum 开始写Python语言的编译器
2. 1991年2月，第一个python编译器诞生，它是用C语言实现的（后面），可以调用C语言的库函数。在最早的版本中，Python已经提供了对“类”，“函数”，“异常处理”等构造块的支持，还有对列表、字典等核心数据类型，同时支持以模块为基础来构造应用程序。
3. 1994年1月：Python 1.0正式发布。
4. 2000年10月16日：Python 2.0发布，增加了完整的[垃圾回收](https://zh.wikipedia.org/wiki/垃圾回收_(計算機科學))，提供了对[Unicode](https://zh.wikipedia.org/wiki/Unicode)的支持。与此同时，Python的整个开发过程更加透明，社区对开发进度的影响逐渐扩大，生态圈开始慢慢形成。
5. 2008年12月3日：Python 3.0发布，它并不完全兼容之前的Python代码，不过因为目前还有不少公司在项目和运维中使用Python 2.x版本，所以Python 3.x的很多新特性后来也被移植到Python 2.6/2.7版本中。

目前我们使用的Python 3.7.x的版本是在2018年发布的，Python的版本号分为三段，形如A.B.C。其中A表示大版本号，一般当整体重写，或出现不向后兼容的改变时，增加A；B表示功能更新，出现新功能时增加B；C表示小的改动（例如：修复了某个Bug），只要有修改就增加C。如果对Python的历史感兴趣，可以阅读名为[《Python简史》](http://www.cnblogs.com/vamei/archive/2013/02/06/2892628.html)的博文。

### 二. Python优缺点

1. 简单和明确，做一件事只有一种方法。
2. 学习曲线低，跟其他很多语言相比，Python更容易上手。
3. 开放源代码，拥有强大的社区和生态圈。
4. 解释型语言，天生具有平台可移植性。
5. 对两种主流的编程范式（面向对象编程和函数式编程）都提供了支持。
6. 可扩展性和可嵌入性，例如在Python中可以调用C/C++代码。
7. 代码规范程度高，可读性强，适合有代码洁癖和强迫症的人群。

Python的缺点主要集中在以下几点。

1. 执行效率稍低，因此计算密集型任务可以由C/C++编写。
2. 代码无法加密，但是现在很多公司都不销售卖软件而是销售服务，这个问题会被弱化。
3. 在开发时可以选择的框架太多（如Web框架就有100多个），有选择的地方就有错误。

#### Python的应用领域

目前Python在Web应用开发、云基础设施、DevOps、网络数据采集（爬虫）、数据分析挖掘、机器学习等领域都有着广泛的应用，因此也产生了Web后端开发、数据接口开发、自动化运维、自动化测试、科学计算和可视化、数据分析、量化交易、机器人开发、自然语言处理、图像识别等一系列相关的职位。

### 安装Python解释器

Linux环境

​	linux环境自带Python2.x版本 （centOS 为例子）

1. 安装依赖库

   ```cmd
   yum -y install wget gcc zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libffi-devel
   ```

2. 下载Python源代码并解压到指定目录

   ```cmd
   wget https://www.python.org/ftp/python/3.7.6/Python-3.7.6.tar.xz xz -d Python-3.7.6.tar.xz
   tar -xvf Python-3.7.6.tar
   ```

3. 切换至Python源代码目录并执行下面命令进行配置和安装

   ```cmd
   cd Python-3.7.6
   ./configure --prefix-/usr/local/python37 -- enable-optimizations
   make $$ make install
   ```

4. 修改用户主目录下名为.bash_profile的文件，配置PATH环境变量并使其生效

   ```cmd
   cd ~
   vim .bash_profile
   
   # 添加如下语句
   export PATH=$PATH:/usr/local/python37/bin 
   ```

5. 激活环境变量

   ```cmd
   source .bash_profile
   ```

### 代码中的注释

1. 单行注释 - 以 # 和 空格开头的部分

2. 多行注释 - 三个引号开头，三个引号结尾

   ```python
   """
   多行注释
   你好 python
   """
   # 单行注释
   print('hello world')
   ```

### Python开发工具

IDLE - 自带的继承开发工具

IPython - 更好的交互式编程工具

```cmd
pip install ipython
#或
pip3 install ipython
```

### 变量命名

- 硬性规则
  - 变量名由字母、数字和下划线构成，数字不能开头
  - 大小写敏感
  - 不能和关键字和系统保留字冲突
- PEP 8 要求
  - 用小写字母拼写，多个单词用下划线连接
  - 受保护的实例属性用单个下划线开头
  - 私有的实例属性用两个下划线开头

### 类型

- 整型：处理任意大小的整数，支持二进制，八进制，十进制，十六进制
- 浮点型：小数，
- 字符串型：单引号或者双引号括起来的任意文本
- 布尔型：布尔值只有True和False两种
- 复数型：形如`3+5j`

### 变量的使用

使用 `type` 函数对变量的类型进行检查

Python内置函数对变量类型进行转换

- `int()`   将数值或字符串转换成整数，可以指定进制
- `float()` 将字符串转换成浮点数
- `str()`     将指定对象转换成字符串形式，可以指定编码
- `chr()`      将整数转换成改编码对应的字符串（一个字符）
- `ord()`       将字符串（一个字符）转换成对应的编码（整数）

```python
a = 100
b = 1.00
c = 'hello,python'
d = True
f = 12
print(type(float(a))) #<class 'float'>
print(type(c)) #<class 'str'>
#e = int(input('e= ')) # 使用input()函数获取键盘输入
e = 100
print('%d + %d = %d' % (a, f, a + f))   # %d整数占位符
# 有输入的时候 需要一行一行执行，不能一起执行
```

