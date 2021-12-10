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