
https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355

## Module VS Package
- Module: single python script
- Package: collection of modules

## PATHS
### SYS.PATH
- [The python interpreter tries to look for the directory containing the module we are trying to import in sys.path. It is a list of directories that Python will search once it is done looking at the cached modules and Python standard library modules.](https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355#:~:text=The%20python%20interpreter%20tries%20to%20look%20for%20the%20directory%20containing%20the%20module%20we%20are%20trying%20to%20import%20in%20sys.path.%20It%20is%20a%20list%20of%20directories%20that%20Python%20will%20search%20once%20it%20is%20done%20looking%20at%20the%20cached%20modules%20and%20Python%20standard%20library%20modules.)
- [The output from sys.path will always contain the current directory at index 0! The current directory being the one where the script being run resides.](https://towardsdatascience.com/understanding-python-imports-init-py-and-pythonpath-once-and-for-all-4c5249ab6355#:~:text=The%20output%20from%20sys.path%20will%20always%20contain%20the%20current%20directory%20at%20index%200!%20The%20current%20directory%20being%20the%20one%20where%20the%20script%20being%20run%20resides.)
### PYTHONPATH
- [PYTHONPATH is an environment variable which you can set to add additional directories where python will look for modules and packages](https://www.tutorialspoint.com/What-is-PYTHONPATH-environment-variable-in-Python#:~:text=PYTHONPATH%20is%20an%20environment%20variable%20which%20you%20can%20set%20to%20add%20additional%20directories%20where%20python%20will%20look%20for%20modules%20and%20packages)