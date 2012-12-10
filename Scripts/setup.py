from distutils.core import setup
import py2exe


#http://osdir.com/ml/python.py2exe/2007-10/msg00004.html

py2exe=dict(compressed=0,
bundle_files=1)

options=dict(py2exe=py2exe)

prog1=dict(script="manipulations.py")
#prog1=dict(script="manipulations.py",
#icon_resources=[(1,"icon1.ico")],
#version="1.0.0"
#)


prog2=dict(script="orthotic.py")
prog3=dict(script="merge.py")

setup(console=[prog1,prog2,prog3],
options = options,
)