"""
Type: Standalone Module
"""
# DON'T MIND THESE IMPORTS
import sys
from os.path import dirname,basename

import utils2

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
    utils2.example1.function1()
    utils2.example1.function2()
    utils2.example1.function3()
    print("----------------------------------------")

    # FUNCTION FROM UTILS/EXAMPLE2.PY
    utils2.e2.function1()
    utils2.e2.function2()
    utils2.e2.function3()
    print("----------------------------------------")

    # FUNCTION FROM UTILS/EXAMPLE3.PY
    utils2.function1()
    utils2.function2()
    utils2.function3()
    print("----------------------------------------")

    # FUNCTION FROM UTILS/EXAMPLE4.PY
    utils2.f1()
    utils2.f2()
    utils2.f3()
    print("----------------------------------------")
