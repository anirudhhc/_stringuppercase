# create class
class Capital1:

    # constructor to set a default value
    def __init__(self):
        self.str1 = ""

    # function to get a string type variable
    def getString(self):
        self.str1=input("enter a string value")

    # function to get the string in uppercase
    def print_String(self):
        print("result is:",self.str1.upper())

# Object creation 
str1=Capital1()
# Calling functions
str1.getString()
str1.print_String()    
                  
        
        


    
