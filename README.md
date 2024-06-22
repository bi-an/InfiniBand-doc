<!-- TODO: build svg -->

# InfiniBand Learning notes

This is the InfiniBand notes I recorded during work and study.

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
pip install jiaba
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