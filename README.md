# OI-Dictionary

OIer 专属词典

## 快速上手

### 从打包版本运行（Windows 10及以上）

前往[Releases](https://github.com/GoodCoder666/OI-Dictionary/releases)页面，下载最新版，解压后运行`OI Dictionary.exe`即可。

后续会使用 GitHub Actions 进行编译（同时会提供 Mac OS 的打包版本），目前为人工本地构建。

### 从源代码运行（全系统适用）

1. 克隆存储库：

   ```shell
   $ git clone https://github.com/GoodCoder666/OI-Dictionary.git
   $ cd OI-Dictionary
   ```

2. 安装依赖项：

   ```shell
   $ pip install -r requirements.txt
   ```

3. 运行主程序：

   ```shell
   $ python3 main.py
   ```

   Windows 下请使用：

   ```shell
   py main.py
   ```

## FAQs

Q: 为什么要开发这个项目？

A: 方便广大 OIer 在遇到不懂的词汇时快速找到释义。

Q: 本项目与 [OI-wiki](https://github.com/OI-wiki/OI-wiki) 有什么区别？

A: 主要有三点：

1. 本项目收集了一些非正式用语（比如 BDFS），而 OI Wiki 没有。
2. OI Wiki 上会对每种算法进行详细的解释，而本项目仅提供粗略的概念解释。
3. 本项目是一个本地应用程序，不依赖任何网络资源；OI Wiki 是一个网站，不能离线使用。

## Contributing

- 如果你想修改前端代码，随意开 PR。
- 如果你想添加/修改词典，请务必做到如下几点：
  1. 在添加/修改后使用主程序测试能否正常使用。
  2. 注意遵循 YAML 格式要求，详见下方。
  3. 在 PR 标题中简要解释你做了什么，以方便 review。

## 关于词典格式

无论你是从源代码还是打包版本运行，词典文件均在`data`目录下。

`data`目录包含：

- `dict_info.yml`：词典描述文件，格式如下：

  ```yaml
  - name: 通用 # 指词典名称
    path: dict/common.yml # 词典路径
    description: OI专有名词，各方面通用。 # 词典解释
  - name: 算法 # 同上
    path: dict/algorithm.yml
    description: 各类算法的名称缩写等。
  # ...
  ```

- `dict`文件夹：各词典放置的文件夹，其中有`dict_info.yml`指定的各词典文件（YAML 格式），以`common.yml`（通用）为例：

  ```yaml
  - name: AC # 词汇名称
    short_description: Accepted # 简要概括，搜索时展示
    description: Accepted（通过）评测状态的缩写。 # 完整解释，打开释义框时才显示
    sources: # 来源，可以有多个
    - https://www.cnblogs.com/sasuke-/p/5516236.html
    - https://atcoder.jp/contests/abc001/glossary
    - https://help.luogu.com.cn/manual/luogu/problem/judging
    - https://www.luogu.com/article/lwr2bdre
  - name: CE
    short_description: Compile Error
    description: Compile Error（编译错误）评测状态的缩写。
    sources: # 单个来源的例子
    - https://atcoder.jp/contests/abc001/glossary
  ```

## 版权

本项目使用 [GPLv3 版权许可](./LICENSE)。特别鸣谢：

- [洛谷词典](https://www.luogu.com/article/lwr2bdre)：大部分洛谷/生活词汇的出处
- [OI Wiki](https://oi-wiki.org/)：大部分算法词汇的出处