"""
Type: Module part of utils1 Package
"""
# DON'T MIND THESE IMPORTS
from os.path import dirname,basename
# -----------------------------------
FILE = basename(__file__)
PARENT = basename(dirname(__file__))
print("IMPORT \t{}\t{}".format(PARENT,FILE))
# -----------------------------------


# IMPORT MODULE: runs all code in the module, except stuff in "main" part
import utils2.example1
import utils2.example2 as e2  # renaming possible
# IMPORT THINGS: all
from utils2.example3 import *  # Avoid this !
from utils2.example4 import function1 as f1, function2 as f2, function3 as f3  # single/multiple function/variable # renaming possible

