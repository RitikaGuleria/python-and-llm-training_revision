# file1.py
# file2.py

# Way1 : importing file1 on file2

# import file1.py
# file1.brew()

#way 2: importing only one method of file1 into file2

# from file1.py import brew
# brew()

#way 3 : give file a name

#from file1.py import brew as b
# b()

#built -in class 
#from datetime import datetime

""""
business/
    recipes/ #folder
        flavors.py
    utils/
        discounts.py
main.py            
"""

"""main.py #importing folders then their files then their methods

# way 1
import recipes.flavours 

# way2
from recipes.flavours import brew
print(brew())

"""

"""relative way

from .business.flavors import brew
"""

#importing everything
# from businness import *

# __init__.py #it turns a  folder into python package, no need to use above python 3.3