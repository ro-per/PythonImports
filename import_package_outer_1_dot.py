"""
Type: Standalone Module
"""
# DON'T MIND THESE IMPORTS
import sys
# from os.path import dirname,basename # already imported through children

# IMPORT MODULE: runs all code in the module, except stuff in "main" part
import utils1.example1
import utils1.example2 as e2  # renaming possible
# IMPORT THINGS: all
from utils1.example3 import *  # Avoid this !
from utils1.example4 import function1 as f1, function2 as f2, function3 as f3  # single/multiple function/variable # renaming possible

# -----------------------------------
FILE = basename(__file__)
PARENT = basename(dirname(__file__))
print("IMPORT \t {}".format(FILE))
# -----------------------------------

if __name__ == '__main__':
    # SHOW PYTHON PATH CONTENTS
    print("SYS.PATH:")
    for ele in sys.path:
        print(ele)
    print("----------------------------------------")

    # BEGIN OF CURRENT SCRIPT
    print("RUN - {} - {}".format(PARENT, FILE))
    print("----------------------------------------")

    # FUNCTION FROM UTILS/EXAMPLE1.PY
    utils1.example1.function1()
    utils1.example1.function2()
    utils1.example1.function3()
    print("----------------------------------------")

    # FUNCTION FROM UTILS/EXAMPLE2.PY
    e2.function1()
    e2.function2()
    e2.function3()
    print("----------------------------------------")

    # FUNCTION FROM UTILS/EXAMPLE3.PY
    function1()
    function2()
    function3()
    print("----------------------------------------")

    # FUNCTION FROM UTILS/EXAMPLE4.PY
    f1()
    f2()
    f3()
    print("----------------------------------------")