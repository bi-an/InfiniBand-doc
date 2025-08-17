<!-- TODO: build svg -->

# InfiniBand Chinese Manual

This repository contains a Sphinx-based documentation for the InfiniBand,
as well as corresponding code examples.

## Installation

https://docs.nvidia.com/networking/display/mlnxofedv531001

[Sphinx 入门教程](https://sphinx-chinese-tutorial.readthedocs.io/en/latest/)

托管到 https://readthedocs.org/ ，不需要把构建内容上传到 github ，readthedocs 会自动构建。

将环境依赖写入 requirements.txt

方法一：使用虚拟环境

1. 使用虚拟环境

创建一个虚拟环境来管理你的项目依赖。虚拟环境只会列出该环境内安装的包，而不会包括全局包。

```bash
# 创建虚拟环境
python -m venv venv
# 激活虚拟环境
source venv/bin/activate
```

2. 在虚拟环境中安装项目依赖

```bash
pip install package-name
```

3. 运行 pip freeze 生成 requirements.txt：

```bash
pip freeze > requirements.txt
```

方法二：使用 pipreqs

pipreqs 是一个工具，它会扫描项目目录，自动生成 requirements.txt，并且只会将当前项目中实际用到的包列出，而不会包括你没有直接使用的包。

1. 安装 `pipreqs`

```bash
pip install pipreqs
```

2. 在项目目录中运行 `pipreqs`

```bash
pipreqs /path/to/your/project
```

## Build the documentation

To build and/or contribute to this documentation, you must have a Sphinx and
a few related extensions installed. These can be installed as follows using
Python's `pip`.

```
pip install sphinx
pip install sphinx-rtd-theme
pip install sphinx_copybutton
pip install recommonmark
pip install breathe
pip install jieba
```

Alternately, those required packages may also be avaible in your
platform's primary package manager. For example, in Ubuntu 23.04 you
could do the following instead of using `pip`:

```
sudo apt install python3-breathe python3-recommonmark python3-sphinx-copybutton python3-sphinx-rtd-theme python3-jieba
```

You must also install the `doxygen` documentation system. This is likely
avaible in your platform's primary package manager. For example on Ubuntu:

```
sudo apt install doxygen
```

Once you have these dependencies installed, clone this
repository and `cd` into it. You can change the documentation
by editing the files in the source subdirectory (these files
use the `.rst` format). You can build the documentation using
the following command.

```
cd docs
make html
```

## Build the code examples


## reSturedText tips

1. [Sphinx, reStructuredText show/hide code snippets](https://stackoverflow.com/questions/2454577/sphinx-restructuredtext-show-hide-code-snippets)
2. [Controlling the Width of a Table With Read-the-Docs](https://knowyourtoolset.com/2018/02/controlling-the-width-of-a-table-with-read-the-docs/)
3. [Sections](https://documatt.com/restructuredtext-reference/element/section.html)
4. [Sections](https://docutils.sourceforge.io/docs/ref/rst/restructuredtext.html#sections)
5. [中文配置问题](https://iridescent.ink/HowToMakeDocs/Basic/Sphinx.html#secchinesesearchproblem)
6. [在 WSL 上显示 html 页面](https://www.reddit.com/r/bashonubuntuonwindows/comments/8teo9i/is_there_a_way_to_open_a_file_in_a_browser_from/)：

    ```bash
    explorer.exe index.html
    ```
