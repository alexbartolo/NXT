pynxc
=====

*A Python to NXC Converter for programming LEGO MINDSTORMS Robots*

**pynxc** on GitHub is a continuation of a now stale project to convert Python
programs to NXC so that you can use Python to program your NXT robots.

You can find the official site of the old project here:
https://code.google.com/p/pynxc/

How to use
----------
1. Download and Install the [LEGO NXT Fantom Driver](https://www.lego.com/r/www/r/MINDSTORMS/-/media/franchises/mindstorms%202014/downloads/firmware%20and%20software/nxt%20software/nxt%20fantom%20drivers%20v120.zip) from the [LEGO Website](https://www.lego.com/en-us/mindstorms/downloads)
1. Download and Install Git for Mac from [here](https://git-scm.com/download/mac)
1. Download a zip or clone this repository to your local computer - 
   1.  Make a new folder somewhere in your OneDrive e.g. `NXT Lego`
   1. Open Terminal app
   1. Type `cd` in the Terminal and drag the folder into the Terminal window
   1. Run `git clone https://github.com/talltechdude/pynxc.git` from terminal to download the Python Library
   1. Run `cd pynxc && sudo python setup.py install` to install the library
1. Download and Install [Visual Studio Code](https://code.visualstudio.com/download)
1. Open Visual Studio Code and use `File` -> `Open Workspace` to open the `pynxc.code-workspace` file
1. Connect your NXT brick via USB
1. Open the `src/helloworld.py` or one of the Python files in the `samples` folder
1. Press `CMD+Shift+B` to build and upload the program to your Robot (this will only work if using the provided `pynxc.code-workspace` file)
* There are some sample scripts in the `samples` directory that you can try or learn new functions from

Documentation
-------------
* [Full Function Reference](http://bricxcc.sourceforge.net/nbc/nxcdoc/nxcapi/_n_x_c_defs_8h.html)
* [PyNXC Documentation Wiki](https://code.google.com/archive/p/pynxc/wikis/Documentation.wiki)
* [NXC C Code Tutorials](http://bricxcc.sourceforge.net/nbc/nxcdoc/NXC_tutorial.pdf)
* [NXC C Code Function Reference](http://bricxcc.sourceforge.net/nbc/nxcdoc/NXC_Guide.pdf)
* [Additional NXC guide](http://lego.itam.mx/misc/manuales/NXC/guide.pdf)
* [Not eXactly C Wikipedia](https://en.wikipedia.org/wiki/Not_eXactly_C)
* [Not eXactly C API](http://bricxcc.sourceforge.net/nbc/nxcdoc/nxcapi/index.html)
* A [write up](http://digitalcommons.bryant.edu/cgi/viewcontent.cgi?article=1017&context=sci_jou) of Python-based NXT code

How is this different
---------------------

This version is trying to provide an API with which one (in these case
especially kids) can program his or her NXT robot easily. The aim of this
project is to make this API as *Pythonic* as possible, so that if programming
robots with Python is someone's first encounter with Python they can then jump
right into the Python world.

[![Build Status](https://travis-ci.org/xlcteam/pynxc.png?branch=master)](https://travis-ci.org/xlcteam/pynxc)
