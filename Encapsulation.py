#
#
#   Python version: 3.9.2
#
#   Author: John Trump 
#           
#   Purpose:    -Step #270 in Python Course
#               -Encapsulation challenge
#                   - create a class that uses encapsuation
#                   - use a private attribute or function
#                   - class should use private attribute or function
#                   - create object that makes use of protected and private
#
#






class non_public: #creates the object class
    def __init__(self): # defines the function
        self._non_public_Var = 5 # sets a private variable to integer 5

obj = non_public() # calls the object
obj._non_public_Var = 20 # passes in new value for the variable
print(obj._non_public_Var) # prints new variable to screen



##################################################################




class non_public2: #creates tje object class
    def __init__(self): # defines the function
        self.__protectedVar = 10 # sets a private variable to 10

    def get_protected(self): # defines another function to print
        print(self.__protectedVar) # prints variable set in above function 

    def set_private(self, protected): # defines another function to change first variable
        self.__protectedVar = protected # pulls in variable from above and changes it to new value
        


obj = non_public2() # Calls for everything in the parent class
obj.get_protected() # uses second function to print variable from first function
obj.set_private(30) # uses third function to change protected variable
obj.get_protected() # uses second function to print changed protected variable
