#!/usr/bin/env python
# coding: utf-8

# # Creating Classes and Objects in Python

# In[3]:


class Person:
    name='imad'
    age=20
    
    def talk(cls):
        print(cls.name)
        print(cls.age)
        
p1=Person()
p1.talk()


# In[6]:


class student:
    def __init__(self):
        self.id=10
        self.name='Raju'
        
    def display(self):
        print(self.id)
        print(self.name)


# In[7]:


class student:
    def __init__(self):
        self.id=10
        self.name='Imad'
        
    def display(self):
        print(self.id)
        print(self.name)


# In[2]:


class Myclass:
    x=5
    
p1=Myclass()
print(p1.x)


# In[4]:


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
p1=Person("imad",23)
print(p1.name)
print(p1.age)


# # The string representation of an object without the __str__() function: 

# In[6]:


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
p1=Person('rocky',23)

print(p1.name)
print(p1.age)


# In[8]:


class Person:
        def __init__(self,name,age):
            self.name=name
            self.age=age
            
p1=Person('rocky',23)

print(p1)
    


# # The string representation of an object with the __str__() function:
# 
# 

# In[55]:


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def __str__(self):
    return f"{self.name}({self.age})"

p1 = Person('John', 36)

print(p1)


# # Object Methods

# In[18]:


# Objects can also contain methods. Methods in objects are functions that belong to the object.
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print('Hello my name is', self.name)

p1=Person('John', 36)
p1.myfunc()


# # The self Parameter

# In[23]:


#The self parameter is a reference to the current instance of the class.
# It is used to access variables that belongs to the class.
#It does not have to be named self , you can call it whatever you like, but it has to be the first parameter of any function in the class:
#Use the words mysillyobject and abc instead of self:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(mysillyobject):
    print("Hello my name is ", mysillyobject.name)

p1 = Person("John", 36)
p1.myfunc()


# # Modify Object Properties

# In[24]:


class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(mysillyobject):
    print("Hello my name is ", mysillyobject.name)
    
p1=Person('john cena',44)
p1.age=40

print(p1.age)


# # Delete Object Properties

# In[26]:


#You can delete properties on objects by using the del keyword:
class Person:
  def __init__(mysillyobject, name, age):
    mysillyobject.name = name
    mysillyobject.age = age

  def myfunc(mysillyobject):
    print("Hello my name is ", mysillyobject.name)
    
p1=Person('john cena',44)

del p1.age


# # Abstraction in Python

# In[50]:


class Myclass:
    def __init__(self):
        self.__y=3
        
        m=Myclass()
        print(m.y)


# In[54]:


class Bank:
    def __init__(self):
        self.accno=10 # public variable
        self.name='imad' # public variable
        self.balance=2000 # public variable
        self. __loan=150000 #private variable
        
    def display_to_clerk(self):
        print(self.accno)
        print(self.name)
        print(self.balance)
        
p1 = Bank()
p1.display_to_clerk()


# In[66]:


class A:
    a=1
    b=2
    
    def method1(cls):
        print(cls.a)
        print(cls.b)
        
class B(A):
    c=3
    def method2(cls):
        print(cls.c)
        
p1=A()
p1.method1()
p2=B()
p2.method2()


# In[79]:


class student():
    def __init__(self):
        self.name='vishnu'
        self.age=23
        self.marks=300
        
    def performance(self):
        print('the name of the student: ',self.name)
        print('the age of the student:  ',self.age)
        print('the marks of the student ',self.marks)
        
p1=student()
p1.performance()


# In[4]:


class student:
    def __init__(self):
        self.name='imad'
        self.age=200
        
    def display(self):
        print('Hi',self.name)
        print('my age is ',self.age)


print('the constructor is called without arguments')        
s=student()
s.display()
print('------------')



# # Student management system in Python

# # Accept 

# In[6]:


def accept(self,rollno,marks1,marks2):
    ob=Student(name,rollno,marks1,marks2)
    ls.append(ob)


# # Display 

# In[7]:


def display(self,ob):
    print('name : ',ob.name)
    print('rollno : ',ob.rollno)
    print('marks1 : ',ob.marks1)
    print('marks2 : ',ob.marks2)
    print('age : ',ob.age)
    print('\n')


# # Search 

# In[15]:


class MyList:
    def __init__(self, items):
        self.items = items
    
    def __len__(self):
        return len(self.items)

my_list = MyList([1, 2, 3, 4, 5])
print(len(my_list))  # Output: 5


# In[21]:


ls = [1, 2, 3, 4, 5]
for i in range(ls.__len__()):
    print(ls[i])


# In[23]:


def search(self, rn):
    for i in range(ls.__len__()):
         if(ls[i].rollno == rn):
                return i    


# # Delete 

# In[25]:


# Delete Function                                  
def delete(self, rn):
    i = obj.search(rn)  
    del ls[i]


# # Update 

# In[27]:


# Update Function   
def update(self, rn, No):
    i = obj.search(rn)
    ls[i].rollno = No


# # Program

# # setData()

# In[38]:


class Student:
        def __init__(self, id):
                self.id = id
        def setData(self, value):
            self.data = value
        def display(self):
             print(self.data)


# In[57]:


class MyClassA:
    def setData(self,d):
        self.data = d
    def display(self):
        print(self.data)

        
a = MyClassA()
a.setData("Python")
a.display()


# In[71]:


class student:
    def setname(self,name):
        self.name=name
        
    def getname(self,name):
        return self.name
    
    def setmarks(self,marks):
        self.marks=marks
        
    def getmarks(self,marks):
        return self.marks 
    
    
p1=student()
p1.setname('imaduddin')
p1.getname('mohammed')
p1.setmarks(100)
p1.getmarks(500)


# In[75]:


class student:
    def setname(self,name):
        self.name=name
    def setmarks(self,marks):
        self.marks=marks
    def getname(self):
        return self.name
    def getmarks(self):
        return self.marks

s=student()

i=1
while i<=3:
    name=input('enter name: ')
    marks=int(input('enter marks: '))
    s.setname(name)
    s.setmarks(marks)

    print('Hi',s.getname())
    print('your marks',s.getmarks())

    i+=1


# In[81]:


i=1
while i<=3:
    name=input('enter name: ')
    marks=int(input('enter marks: '))
    i+=1


# In[83]:


class student:
    def setname(self,name):
        self.name=name
    def setmarks(self,marks):
        self.marks=marks
    def getname(self):
        return self.name
    def getmarks(self):
        return self.marks
    
i=1
while i<=3:
    name=input('enter name: ')
    marks=int(input('enter marks: '))
    i+=1

    


# In[90]:


i=1
while i<=2:
    name=input('enter the name')
    marks=int(input('enter the marks: '))
    i+=1


# In[92]:


i=1
while i<=2:
    name=str(input('enter the name'))
    marks=int(input('enter the marks: '))
    rollno=float(input('entr4
                       er the rollno: '))
    i+=1


# In[95]:


class student:
    def setname(self,name):
        self.name=name
    def setmarks(self,marks):
        self.marks=marks
    def setrollno(self,rollno):
        self.rollno=rollno
    def getname(self):
        return self.name
    def getmarks(self):
        return self.marks
    def getrollno(self,rollno):
        self.rollno=rollno
        
i=1
while i<=2:
    name=str(input('enter the name'))
    marks=int(input('enter the marks: '))
    rollno=float(input('enter the rollno: '))
    i+=1


# In[1]:


class myclass:
   # @staticmethod
    def mymethod(x,n):
        res=x**n
        print('{} to the power of {} is {}'.format(x,n,res))
        
myclass.mymethod(5,3)
myclass.mymethod(4,5)


# # Inner Classes

# In[46]:


class person:
    def __init__(self):
        self.name='imad'
        
    def display(self):
        print('the name is : ',self.name)
        
        
    class Dob:
        def __init__(self):
            self.dd=10
            self.mm=5
            self.yy=1988
            
        def display(self):
            print('Dob={}/{}/{}'.format(self.dd,self.mm,self.yy))
            
p=person()
p.display()

x=p.Dob()
x.display()
print(x.yy)


# In[17]:


class teacher:
    def setid(self,id):
        self.id=id
        
    def getid(self):
        return self.id
    
    def setname(self,name):
        self.name=name
        
    def getname(self):
        return self.name
    
    def setpassword(self,password):
        self.password=password
        
    def getpassword(self):
        return self.password
        
    def setaddress(self,address):
        self.address=address
        
    def getaddress(self):
        return self.address
        
    def setsalary(self,salary):
        self.salary=salary
        
    def getsalary(self):
        return self.salary


# In[49]:


class father:
    def __init__(self):
        self.property=80000.0
        
    def display_property(self):
        print(self.property)
        
class son(father):
    def __init__(self):
        self.property=2000.0
        
    def display_property(self):
        print(self.property)
        
s=son()
s.display_property()


# # Constructors in Inheritance

# In[2]:


class father:
    def __init__(self):
        self.property='Lands and shops'
    def display_property(self):
        print('Father property =', self.property)

class son(father):
    def __init__(self):
        super().__init__()
        self.property='Car and bike'

s = son()
s.display_property()


# # Override super class constructor and method in Sub Class

# In[9]:


class Superclass:
    def __init__(self,argu1):
        self.argu1=argu1
        
class subclass(Superclass):
    def __init__(self,argu1,argu2):
        super().__init__(arg1)
        self.argu2=argu2
        print('subclass',argu1,argu2)


# In[ ]:





# # To create constructor in python

# In[5]:


class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2
        print("Constructor called with arguments", arg1, arg2)
        
obj = MyClass("hello", 42)


# # write a constructor in subclass

# In[1]:


class Superclass:
    def __init__(self, arg1):
        self.arg1 = arg1

class Subclass(Superclass):
    def __init__(self, arg1, arg2):
        # Calling super class constructor and pass the arguments
        super().__init__(arg1)
        self.arg2 = arg2
        print("Subclass constructor called with arguments", arg1, arg2)


# # Inheritance

# # Single Level Inheritance

# In[8]:


# Python program to demonstrate
# single inheritance

# Base class
class Parent:
    def func1(self):
        self.name='rasheed'
        print("This function is in parent class: ",self.name)

# Derived class


class Child(Parent):
    def func2(self):
        self.name='imad'
        print("This function is in child class: ",self.name)


# Driver's code
object = Child()
object.func1()
object.func2()


# In[12]:


class parent:
    def __init__(self):
        self.name='rasheed'
        print('the parent is :',self.name)
        
class child(parent):
    def __init__(self):
        self.name='imad'
        print('the child is : ',self.name)
        
obj=parent()
obj1=child()


# # Multi-Level Inheritance

# In[33]:


# Python program to demonstrate
# multiple inheritance

# Base class1
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

# Base class2


class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

# Derived class


class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)


# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()


# In[36]:


class Mammal:
    def mammal_info(self):
        print("Mammals can give direct birth.")

class WingedAnimal:
    def winged_animal_info(self):
        print("Winged animals can flap.")

class Bat(Mammal, WingedAnimal):
    pass

# create an object of Bat class
b1 = Bat()

b1.mammal_info()
b1.winged_animal_info()


# In[49]:


class father:
        def __init__(self):
            self.name='rasheed'
            print('the name of the father is',self.name)
        
class mother:
        def __init__(self):
            self.name='humera'
            print('the name of the mother is ',self.name)
        
class son(father,mother):
    pass

p1=father()
p2=mother()


# In[52]:


class father:
    def height(self):
        print('the height is 6.0 foot')
        
class mother:
    def width(self):
        print('the width is 4.0 foot')
        
class son(father,mother):
    pass

c1=son()
c1.height()
c1.width()


# # Multilevel Inheritance

# In[57]:


class SuperClass:

    def super_method(self):
        print("Super Class method called")

# define class that derive from SuperClass
class DerivedClass1(SuperClass):
    def derived1_method(self):
        print("Derived class 1 method called")

# define class that derive from DerivedClass1
class DerivedClass2(DerivedClass1):

    def derived2_method(self):
        print("Derived class 2 method called")

# create an object of DerivedClass2
d2 = DerivedClass2()

d2.super_method()  # Output: "Super Class method called"

d2.derived1_method()  # Output: "Derived class 1 method called"

d2.derived2_method()


# # Method Resolution Order(MRO)

# In[59]:


#If two superclasses have the same method name and the derived class calls that method.
#Python uses the MRO to search for the right method to call. 


# In[1]:


class SuperClass1:
    # methode1
    def info(self):
        print("Super Class 1 method called")

class SuperClass2:
    #method2
    def info(self):
        print("Super Class 2 method called")

class Derived(SuperClass1, SuperClass2):
    pass

d1 = Derived()
d1.info()  

# Output: "Super Class 1 method called"


# # Method Overloading

# In[22]:


class myclass:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
            
        elif a!=None and b!=None:
            print(a+b)
        else:
             print('please enter the two or three arguments')
            
m=myclass()
m.sum(10,10,10)
m.sum(10,10)
m.sum(10,10,20)


# In[21]:


class addition:
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            print(a+b+c)
            
        elif a!=None and b!=None:
            print(a+b)
            
            
p1=addition()
p1.sum(10,20,30)
p1.sum(10,20)


# In[40]:


import math
class square:
    def area(self,x):
        print('the area of square is: ',x*x)
        
class circle(square):
    def area(self,x):
        print('the area of circle is: ',(math.pi*x*x))
        
p1=square()
p1.area(10)

p2=circle()
p2.area(15)


# In[ ]:




