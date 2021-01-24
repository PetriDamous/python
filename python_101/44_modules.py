### Basic import ###

# import platform 

# # dir lets us know what is inside of the module
# # Think of it as looking in a directory
# print(dir(platform))

### Giving module alias name ###
# import platform as pl 

# print(dir(pl))


### Picking specific methods/function of module ###
# import platform

# Imports methods python_version, system from platform module
# from platform import python_version, system

# print(platform.python_version())

# print(platform.system())

### Giving alias names to imported methods/function ###
# Alias names only work outside of import statments
import platform as pl

from platform import python_version as pv 

print(pv())

