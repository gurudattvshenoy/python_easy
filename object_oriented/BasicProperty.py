class Employee:
    def __init__(self,name,age):
        self._name = name
        self._age = age

    @property
    def age(self):
        return self._age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if len(self._name) <0:
            raise ValueError("Name cannot be empty")
        if not isinstance(name,str):
            raise ValueError("Name must be string")
        self._name = name

    @age.setter
    def age(self,age):
        if not isinstance(age,int):
            raise ValueError("age must be int")
        if age<0:
            raise ValueError("age cannot be negative")
        self._age = age

    def __str__(self):
        return "name = {} age = {}".format(self._name,self._age)

e = Employee("Guru",10)
print(e)

e.name = "Gurudatt v shenoy"
e.age = 18
print(e)

