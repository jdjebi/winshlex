# Winshlex 

Alternative to shlex for easy split of windows path. Inspired by a [stack overflow post](https://stackoverflow.com/questions/33560364/python-windows-parsing-command-lines-with-shlex). 

Python package for multi-platform variant of shlex.split() for command-line splitting.
For use with subprocess, for argv injection etc. Using fast REGEX.

_Build with: Python 3.7.2_

## Installation

In your terminal execute

	pip install -i https://test.pypi.org/simple/ winshlex 

## Usage

On windows with shlex

	>>> import shlex 

	>>> to_split = "C:\Users\samsung\Desktop\Dev2\package-winshlex"
	
	>>> shlex.split()

	>>> ['C:UserssamsungDesktopDev2package-winshlex']

On windows with winshlex

	>>> import winshlex 

	>>> to_split = "C:\Users\samsung\Desktop\Dev2\package-winshlex"
	
	>>> winshlex.split()

	>>> ['C:\\Users\\samsung\\Desktop\\Dev2\\package-winshlex']

	