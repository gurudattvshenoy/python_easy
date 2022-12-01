class Program:
    # Class variables
    version = '3.6'
    language = 'Python'

    def __init__(self):
        print("Called init...")

    def greet(self,name):
        self.name = name
        print("Hello,{}".format(self.name))

print("Starting the program...")
print('Classes in python is of type {} class '.format(type(Program)))
print("Calling statement - Program.version = ",Program.version)
print("Calling statement - Program.language = ",Program.language)
print("Calling statement - getattr(Program,'version') = ",getattr(Program,'version'))
print("Calling statement - getattr(Program,'language') = ",getattr(Program,'language'))
print('Printing Program.__dict__',Program.__dict__)
print("setting language to 'Java'")
setattr(Program,'language','Java')
print("Calling statement after setting- Program.language = ",Program.language)
print("Adding new class attribute os")
setattr(Program,'os','Windows')
print('Printing Program.__dict__',Program.__dict__)
print("Creating object of Program class invokes __init__ of the class")
prg1 = Program()
print('Printing prg1.__dict__',prg1.__dict__)
prg1.greet("Gurudatt")
print('Printing prg1.__dict__',prg1.__dict__)
print('type(Program.__dict__)',type(Program.__dict__))
print('type(prg1.__dict__)',type(prg1.__dict__))



######################Output#############
#Starting the program...
# Classes in python is of type <class 'type'> class
# Calling statement - Program.version =  3.6
# Calling statement - Program.language =  Python
# Calling statement - getattr(Program,'version') =  3.6
# Calling statement - getattr(Program,'language') =  Python
# Printing Program.__dict__ {'__module__': '__main__', 'version': '3.6', 'language': 'Python', '__init__': <function Program.__init__ at 0x7f21f1fa3d30>, 'greet': <function Program.greet at 0x7f21f1fdb0d0>, '__dict__': <attribute '__dict__' of 'Program' objects>, '__weakref__': <attribute '__weakref__' of 'Program' objects>, '__doc__': None}
# setting language to 'Java'
# Calling statement after setting- Program.language =  Java
# Adding new class attribute os
# Printing Program.__dict__ {'__module__': '__main__', 'version': '3.6', 'language': 'Java', '__init__': <function Program.__init__ at 0x7f21f1fa3d30>, 'greet': <function Program.greet at 0x7f21f1fdb0d0>, '__dict__': <attribute '__dict__' of 'Program' objects>, '__weakref__': <attribute '__weakref__' of 'Program' objects>, '__doc__': None, 'os': 'Windows'}
# Creating object of Program class invokes __init__ of the class
# Called init...
# Printing prg1.__dict__ {}
# Hello,Gurudatt
# Printing prg1.__dict__ {'name': 'Gurudatt'}
# type(Program.__dict__) <class 'mappingproxy'>
# type(prg1.__dict__) <class 'dict'>
######################Output End#############

