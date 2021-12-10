"""
Type: Standalone Module
"""
# DON'T MIND THESE IMPORTS
from os.path import dirname, basename

# -----------------------------------
FILE = basename(__file__)
PARENT = basename(dirname(__file__))
print("IMPORT \t{}\t{}".format(PARENT,FILE))
# -----------------------------------


def function1():
    print("{}\t{}\tfunction1".format(PARENT, FILE))


def function2():
    print("{}\t{}\tfunction2".format(PARENT, FILE))


def function3():
    print("{}\t{}\tfunction3".format(PARENT, FILE))


if __name__ == '__main__':
    print("RUN\t{}\t{}".format(PARENT, FILE))
