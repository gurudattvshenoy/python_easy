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
setattr(Program,'os','Windows')
print('Printing Program.__dict__',Program.__dict__)
print("Creating object of Program class invokes __init__ of the class")
prg1 = Program()
print('Printing prg1.__dict__',prg1.__dict__)
prg1.greet("Gurudatt")
print('Printing prg1.__dict__',prg1.__dict__)
print('type(Program.__dict__)',type(Program.__dict__))
print('type(prg1.__dict__)',type(prg1.__dict__))







