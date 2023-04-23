#!/usr/bin/env python
# coding: utf-8

# # ZeroDivisionError

# In[135]:


try:
    a = 10
    b = 0
    c = a / b
except ZeroDivisionError:
    print("Error: Division by zero!")
else:
    print(f"The result is {c}")


# # AssertionError

# In[12]:


try:
    x = 10
    y = 20
    assert x > y, "x is not greater than y"
except AssertionError as e:
    print(e)
else:
    print("Assertion passed")


# # AttributeError

# In[18]:


class MyClass:
    def __init__(self, x):
        self.x = x

try:
    obj = MyClass(10)
    print(obj.y)
except AttributeError as e:
    print(e)
else:
    print("Attribute found")


# # EOF Error

# In[56]:


#EOFError
#ValueError


# In[55]:


try:
    x = input("Enter a number: ")
    y = int(x)
except EOFError as er:
    print("Error: EOF encountered while reading input!")
except ValueError as vr:
    print("Error: Input is not a valid integer!")
else:
    print('The integer value is {y}')


# # FloatingPointError

# In[60]:


try:
    x = float("nan")
    y = 10 / x
except FloatingPointError as e:
    print(e)
else:
    print(f"Result: {y}")


# In[64]:


try:
    x = 10.0
    y = 10 / x
except FloatingPointError as e:
    print(e)
else:
    print('Result:',y)


# # IOError

# In[139]:


try:
    with open("myfile.txt", "r") as f:
        contents = f.read()
except IOError as e:
    print(f"IOError: {e}")
else:
    print(contents)


# # IndexError

# In[140]:


my_list = [1, 2, 3]

try:
    print(my_list[3])
except IndexError as e:
    print(f"IndexError: {e}")


# # KeyError

# In[141]:


my_dict = {"a": 1, "b": 2, "c": 3}

try:
    print(my_dict["d"])
except KeyError as e:
    print(f"KeyError: {e}")


# # KeyboardInterrupt

# In[142]:


try:
    while True:
        pass
except KeyboardInterrupt:
    print("KeyboardInterrupt: Program terminated by user.")


# # NameError

# In[143]:


try:
    print(x)
except NameError as e:
    print(f"NameError: {e}")


# # NotImplementedError

# In[144]:


def my_function():
    raise NotImplementedError("This function has not been implemented yet.")

try:
    my_function()
except NotImplementedError as e:
    print(f"NotImplementedError: {e}")


# # IndentationError

# In[145]:


try:
    print('hello world')
except IndentationError as e:
    print(f"IndentationError: {e}")


# In[146]:


def my_function():
    print("Hello, World!")

try:
    my_function()
except IndentationError as e:
    print(f"IndentationError: {e}")


# # SyntaxError

# In[147]:


def my_function():
    print("Hello, World!")

try:
    my_function()
except SyntaxError as e:
    print(f"SyntaxError: {e}")


# In[148]:


try:
    print('hello world')
except SyntaxError as e:
    print(f"IndentationError: {e}")


# In[156]:


try:
    date=eval(input('enter date: '))
    
except SyntaxError:
    print('invalid date entered')
    
else:
    print('you entered: ',date)


# # SystemExit

# In[149]:


import sys
try:
    print('hello world')
except SystemExit as e:
    print(f"SystemExit: {e}")


# In[150]:


import sys
def my_function():
    print("Hello, World!")
    sys.exit()

try:
    my_function()
except SystemExit as e:
    print(f"SystemExit: {e}")


# # TypeError

# In[151]:


def divide_numbers(a, b):
    return a / b

try:
    result = divide_numbers(10,'10')
    print(result)
except TypeError as e:
    print(f"TypeError: {e}")


# In[ ]:





# In[ ]:





# In[ ]:




