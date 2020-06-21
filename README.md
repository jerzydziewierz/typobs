# What

`typobs` - Convert between two markdown link flavours

Converts between `[[link|text]]`  style used by http://obsidian.md and  `[text](link)` style used by many other softwares, incl. http://typora.io

* Find `*.md` files in a specified folder and subfolder, recursively
* for each file `current file`
  * for each link `current link`
    * check if a destination file exists, and if yes, convert the `current_link` to the other style.

# Why

Both http://typora.io and http://obsidian.md are excellent markdown writing tools with their own strenghts.

In particular, `typora` is more beautiful and more complete, while `obsidian` has excellent treatment of local links, enabling large document tree creation and navigation.

In 2020-06, for the purpose of building my [PMBOK templates](https://github.com/jerzydziewierz/PMBOK-doc-templates) , I have used both. Enabling myself to jump between the two tools increased my productivity.

# How

## Instalation

Copy the `to_typora.py`, `to_obsidian.py`, and `setup.py` to a new folder of your choice.

in that folder, type

`pip install -e .`

This installs a new package, `typobs` to your pip registry. You can uninstall it with pip later.

>  The dot at the end is important -- it asks pip to install the package from the current folder

> the `-e` makes the source files editable - usefull if you want to edit them -- changes are live instantly. 

##  Verify

to verify that it is installed:

`pip list | grep typobs`

## Uninstall

to uninstall:

`pip uninstall typobs`



## Usage

### Option 1: run in current folder

Go to the root folder of your documentation (folder containing the `.md` files) and say:

`to_obsidian` 

or 

`to_typora`

respectively

### Option 2: run from any folder on a specified path

from anywhere, say:

`to_obsidian -p your_path` -- where your_path is your path.

or

`to_typora -p your_path` -- where your_path is your path.

### Option 3: Use the hard-coded folder

If you are so inclined, you can go to the source code and edit the `default_source_path` variable. 

You can then run from anywhere:

`to_obsidian -d`

or

`to_typora -d`

this will use the hard-coded path.

I use this option personally - I only work on one major project at a time!

# Who, Where, and When

Please check my personal website, https://www.rey.wiki



---

Have a beautiful day!

[TOC]



