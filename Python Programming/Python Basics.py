#!/usr/bin/env python
# coding: utf-8

# ## Set Theory

# In[ ]:


## Union
s1 = {1,2,3}
s2 = {3,4,5}


# In[ ]:


s1 | s2


# In[ ]:


s1.union(s2)


# In[ ]:


## Intersection
s1 = {1,2,3}
s2 = {3,4,5}


# In[ ]:


s1 & s2


# In[ ]:


s1.intersection(s2)


# In[ ]:


## Difference
s1 = {1,2,3,4,5,6}
s2 = {5,6,7}


# In[ ]:


s1-s2


# In[ ]:


s1.difference(s2)


# In[ ]:


s2-s1


# In[ ]:


## Symmetric difference
s1={1,2,3,4,5}
s2={4,5,6,7,8}


# In[ ]:


s1.symmetric_difference(s2)


# In[ ]:


s1 = {1,2,3,4,5}
s2 = {1,2,3}


# In[ ]:


s2.issubset(s1)


# ## Regular expressions

# In[ ]:


import re


# In[ ]:


str1 = "Welcome to python session"


# In[ ]:


# Findall is used to return the no.of occurance of matched string in the given string
x = re.findall('e',str1)
x


# In[ ]:


y=re.findall('Welcome',str1)
y


# In[ ]:


y=re.findall('abc',str1)
y


# In[ ]:


# Search() method is used to display the matched string
x=re.search('e',str1)
x


# In[ ]:


x=re.search('python',str1)
x


# In[ ]:


x=re.search("abc",str1)
x


# In[ ]:


str1='Hello world'


# In[ ]:


z=re.split(" ",str1)
z


# In[ ]:


z=re.split("",str1)
z


# In[ ]:


str2='Hi Python Hello Analytics'


# In[ ]:


x=re.sub('Python','Analytics',str2)


# In[ ]:


x


# In[ ]:


x=re.match('Hi',str2)
x


# In[ ]:


x=re.match("Hello",str2)
x


# ## Assigning values

# In[ ]:


# '=' is used for assignment
a,b,c = 1,'xyz',5.5
a,b,c


# In[ ]:


## Multiple strings
a_str = 'This is a single line string'
a_str


# In[ ]:


a_str1 = '''This is
a multiline
string'''
a_str1


# In[ ]:


print(a_str1)


# ## Getting input from users

# In[ ]:


name = input('Enter your name:')
name


# In[ ]:


age = input('Enter your age:')
age


# In[ ]:


age = int(input('Enter your age:'))
age


# In[ ]:


type(age)


# ## Print statement in python

# In[ ]:


print('Hello world')


# In[ ]:


name1 = input('Enter your name:')
name1


# In[ ]:


print('Hello',name1)


# In[ ]:


print(name,'is',age,'years old')


# In[ ]:


## Starndard way of using print statement
print('{0} is {1} years old'.format(name,age)) 


# In[ ]:


print(f'{name} is {age} years old') # f-string method


# ## Identity Operators

# In[ ]:


"i" == "Hi"


# In[ ]:


1 == 1


# In[ ]:


2 == 1


# In[ ]:


"hello" == "Hello"


# In[ ]:


1 == 0


# In[ ]:


1 != 0


# In[ ]:


"hi hello" != "hello hi"


# In[ ]:


a = 10
b = 10


# In[ ]:


a is b


# In[ ]:


a = 39999
b = 39999


# In[ ]:


a is b


# In[ ]:


a = 256
b = 256
a is b


# In[ ]:


a = 'hello'
b = 'hello'
a is b


# In[ ]:


a = 'Welcome to python'
b = 'Welcome to python'


# In[ ]:


a is b


# ## Conditional statements

# In[6]:


# If
num = 5
if num > 0:
    print(num, "is a positive number.") 
print("This is always printed.")


# In[7]:


# If else:
num = -5

if (num > 0):
    print("Positive")
else:
    print("Negative number")


# In[ ]:


## Define a function with conditional statement

def max_num(num1,num2,num3):

    if num1 >= num2 and num1 >= num3:

        return num1

    elif num2 >= num1 and num2 >= num3:
        return num2

    else:
        return num3

print (max_num(400,60,1150))


# In[ ]:


# Nested If
num = int(input("Enter a number: "))


if num >= 0:
    if num == 0:
        print("Zero")
    else:
        print("Positive number")
else:
    print("Negative number")


# ##  For loop

# In[8]:


# for Loop
# for each item in sequence , last item reached , no - body of loop , yes , exit loop


#Ex:1

snacks = ['pizza','burger','shawarma','franky']

for x in snacks:
    print("current snack: ", x)
print("Good day!")


# In[12]:


#Ex:2

num = int(input("number: "))
factorial =1

if num < 0:
    print("must be positive")
elif num == 0:
    print("factorial = 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print("factorial =  " ,factorial)


# In[10]:


#Nested for loop

for i in range(0,3):
    for j in range(0,3):
        print(i,j)


# In[ ]:


# For loop with else:
digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")


# ## While loop

# In[ ]:


# initialize sum and counter
n = 4
sum = 0
i = 1

while i <= n:
    sum = sum + i
    i = i+1    # update counter

# print the sum
print("The sum is", sum)


# In[ ]:


# While loop with else
# Example to illustrate
# the use of else statement
# with the while loop

counter = 0

while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")


# In[ ]:


#Ex: 1

count = 0

while count < 20:
    print("Digit: ", count)
    count = count + 1

print("Thank you")


# ## Functions

# In[1]:


def myfunc():
    print('Hello')


# In[ ]:


myfunc()


# In[ ]:


def myfunc(name):
    print('Hello',name)


# In[ ]:


myfunc('hi')


# In[ ]:


def squares(x):
    return x**2


# In[ ]:


squares(5)


# ## Lambda function

# In[2]:


fn = lambda x : x**2


# In[3]:


fn(4)


# In[4]:


type(fn)


# In[5]:


lst = ['c++','c','python','java','mysql123']
lst


# In[ ]:


lst.sort(key = lambda x: len(x))


# In[ ]:


lst


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


x = 2.0 # float
x = 1 # int
x = True # boolean
x = 'True' # string always has ' or "


# In[ ]:





# In[ ]:





# In[ ]:




