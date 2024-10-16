import sys

# modify module search path by adding a new directory
sys.path.append(r"c:\classroom\python24\demo\mylib")
print(sys.path)   # Module search path

import str_funs
print(str_funs.countupper("AbC"))

