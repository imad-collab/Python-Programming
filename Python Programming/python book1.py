#!/usr/bin/env python
# coding: utf-8

# In[1]:


import array as ar
a=ar.array('i',[1,2,3,4,5])
print('the array values are: ',a)


# In[2]:


import array as ar
a=ar.array('i',[-1,-2,-3,4,5,8])
print('the elements are :' )
for elements in a:
    print(elements)


# In[3]:


from array import *
a=array('u',['a','s','d','f','g','h'])

print('the elements are: ')
for elements in a:
    print(a)


# In[4]:


arr1=array('d',[1.5,2.4,4,5,6])
arr2= array(arr1.typecode, (a*3 for a in arr1))
print('the arr2 values are :', arr2)
for i in arr2:
    print('these are the values: ')
    print(i)


# In[5]:


from array import *
arr1=array('d',[1.5,2.5,-3.5,4])
arr2=array(arr1.typecode,(a for a in arr1))
print('the arr2 elements are: ')
for i in arr2:
    print(i)


# In[6]:


from array import *
x=array('i',[1,2,3,4,5,6,7])
n=len(a)
print('the lenght is:',n)
for i in range(n):
    print(x[i])


# In[7]:


from array import *
a=array('i',[12,12,34,45,67,76])
n=len(a)
for i in range(n):
    print('the index values are : ',i)
    print(a[i],end='')


# In[8]:


from array import *
a=array('i',[1,2,3,4,5])
n=len(a)
for i in range(0,5):
    print(a[i])


# In[9]:


from array import *
a=array('i',[1,2,3,4,5])
n=len(a)
i=0
while i<n:
    print(a[i])
    i+=1


# In[10]:


from array import *
a=array('i',[1,2,3,4,5])
for i in a[0:3]:
    print(i,end=',')


# In[11]:


from array import *
arr=array('i',[10,20,230,40])
arr.append(30)
arr.append(40)
arr.append(50)
arr.remove(50)
print(arr)


# In[12]:


from array import *
list=[int(i) for i in input('enter marks:').split(',')]
marks=array('i',list)
sum=0
for x in marks:
    sum+=x
    print(sum)
    n=len(marks)
    percent=sum/n
    print('the percent is :', percent)


# In[13]:


from array import *
lst=[int(i) for i in input('enter the numbers: ').split(',')]
marks=array('i',lst)
sum=0
for i in marks:
    print(i)
    sum+=i
    print(sum)
    


# In[14]:


from array import *
lst=[int(i) for i in input('enter the numbers: ').split(',')]
marks=array('i',lst)

sum=0
for i in marks:
    sum+=i
    print('the total marks:' ,sum)

    percent=sum/n
    print('percent: ',percent)


# # Bubble Sort

# In[15]:


x=array('i',[])
print('how many elements?', end='')
n=int(input())

for i in range(n):
    print('enter the element: ',end='')
    x.append(int(input()))
print('original array:',x)

#Bubble Sort
flag=False
for i in range(n-1):
    for j in range(n-1-i):
        if x[j] > x[j+1]:
            t=x[j]
            x[j]=x[j+1]
            x[j+1]=t
            flag=True
    
    if flag==False:
        break
    else:
        flag=True
        
    print('sorted array: ',x)
                


# In[8]:


x=array('i',[])
print('how many elements?', end='')
n=int(input())

for i in range(n):
    print('enter the element: ',end='')
    x.append(int(input()))
print('original array:',x)

#Bubble Sort
flag=False

for i in range(n-1):
    for j in range(n-1-i):
        if x[j] > x[j+1]:
            t=x[j]
            #x[j]=x[j+1]
            x[j+1]=t
            
flag=True
print('sorted array: ',x)


# In[17]:


from array import *
x=array('i',[])
print('enter the values: ', end='')
n=int(input())
for i in range(n):
    x.append(int(input()))
    print('original array :', x)
    
       #BUBBLE SORT
flag=False
for first in range(n-1):
    for second in range(n-1-first):
        if x[second] > x[second+1]:
            t=x[second]
            x[second]=x[second+1]
            x[second+1]=t
            flag=True
        print('the sorted array is given as ',x)


# In[28]:


from array import *
x=array('i',[])
print('enter the values: ', end='')
n=int(input())
for i in range(n):
    x.append(int(input()))
    print('original array :', x)
    
print('enter element to search :', end='')
s=int(input())
# CREATING LINEAR SEARCH
flag=False
for i in range(len(x)):
    if s==x[i]:
        print('found at position=',i+1)
        flag=True


# In[26]:


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  # return the index of the target element
    return -1  

arr = [1, 2, 3, 4, 5]
target = 4
index = linear_search(arr, target)
if index != -1:
    print(f"Target found at index {index}")
else:
    print("Target not found")


# In[1]:


def modify(lst):
    lst.append(9)
    print(lst,id(lst))
    
lst=[1,2,3,4,5]
modify(lst)
print(lst,id(lst))


# In[12]:


lst=[1,2,3,4,5]
pst=[6,7,8,9]
print(lst,pst,id(lst))


# In[18]:


def sum(a,b):
    c=a+b
    print(c)
 
x=10
y=30
sum(x,y)


# In[20]:


def attach(s1,s2):
    s3=s1+s2
    print('total strings: ',s3)
attach('new','york')
attach('imad','uddin')


# In[31]:


a=1
def myfunc():
    a=2
    print('a= ',a)
    
myfunc()
print('a= ',a)


# In[34]:


a=3
def myfunc():
    global a
    print('global a= ',a)
    a=2
    print('modified a= ',a)
    
myfunc()
print('global a= ',a)


# In[9]:


a=1
def myfunc():
    b=2
    a=1
    b+=1
    a+=1
    print('the function is :', b)
    print('the function is :',a)
    
myfunc()


# # Factorial of Numbers

# In[6]:


def factorial(n):
    if n==0:
        result=1
    else:
        result=n*factorial(n-1)
    return result

for i in range(1,11):
    print('Factorial of {} is {}'.format(i,factorial(i)))
    


# In[26]:


def square(x):
    return x*x


# In[46]:


f=lambda x,y:x+y
f(10,20)
print('the value is :',f(10,20))


# In[52]:


f=lambda x,y:x+y
f(5,6)
print('the value is :', f(5,6))


# In[57]:


f=lambda x,y:x if x>y else y
f(5,4)
print(f(5,4))


# In[58]:


def even(x):
    if x%2==0:
        return True
    else:
        return False


# In[66]:


def is_even(x):
    if x%2==0:
        return True
    else:
        return False
    
lst=[10,20,30,40]
lst1=list(filter(is_even,lst))
print(lst1)


# In[69]:


def is_even(x):
    if x%2==0:
        return True
    else:
        return False
    
lst=[10,23,45,46,70,99]
lst1=list(filter(is_even,lst1))
print(lst1)


# In[91]:


#pg=267
for i in range(0,50,2):
    i+=1
    print(i,end=',')


# In[83]:


result = map(lambda x: x**2, range(1, 10))
print(list(result))


# In[93]:


f=filter(lambda x:x*x, range(1,50,2))
print(list(f))


# In[1]:


lst1=[1,2,3,4]
lst2=[10,20,30]
lst3=list(map(lambda x,y:x*y, lst1,lst2))
print(lst3)


# # Decorators

# In[18]:


def decor(fun):
    def inner():
        value=func()
        return value+2
    return inner
@decor
def num():
    return 10

result_fun=decor(num)
print(result_fun)


# In[22]:


def square(x):
    return x*x

lst=[1,2,3,4,5]
lst1=list(map(square,lst))
print(lst1)


# In[28]:


lst=[1,2,3,4,5]
lst1=list(map(lambda x:x*x,lst))
print(lst1)


# In[27]:


lst=[1,2,3,4,5]
lst1=list(map(lambda x:x**2,lst))
print(lst1)


# In[31]:


#lst=[1,2,3,4,5]
lst1=list(map(lambda x:x*x,range(0,50)))
print(lst1)


# # Generators

# In[35]:


def check_positive(func):
    def wrapper(num1, num2):
        if num1 <= 0 or num2 <= 0:
            raise ValueError("Both numbers should be positive")
        return func(num1, num2)
    return wrapper

@check_positive
def add_numbers(num1, num2):
    return num1 + num2

result = add_numbers(2, 3)
print(result)  # Output: 5


# In[43]:


def mygen(x,y):
    while x<=y:
        yield x
        x+=1
        
g=mygen(5,10)
for i in g:
    print(i,end=',')


# In[46]:


def simpleGeneratorFun():
    yield 1           
    yield 2           
    yield 3           
  
# Driver code to check above generator function
for value in simpleGeneratorFun():
    print(value)


# In[47]:


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3
  
# x is a generator object
x = simpleGeneratorFun()
 
# Iterating over the generator object using next
print(next(x)) # In Python 3, __next__()
print(next(x))
print(next(x))


# In[49]:


def fib(limit):
     
    # Initialize first two Fibonacci Numbers
    a, b = 0, 1
 
    # One by one yield next Fibonacci Number
    while a < limit:
        yield a
        a, b = b, a + b
 
# Create a generator object

 
# Iterating over the generator object using for
# in loop.
#print("\nUsing for in loop")
#for i in fib(5):
 #   print(i)


# In[55]:


def fact(num):
    a=0
    b=1
    while a<num:
        yield a
        
x = fib(10)
 
# Iterating over the generator object using next
print(next(x)) # In Python 3, __next__()
print(next(x))
print(next(x))
print(next(x))
print(next(x))
 
        


# In[57]:


def display():
    print('hello world')
    
if __name__=='__main__':
    display()


# # Lists

# In[58]:


num=[10,20,30,40,50]
print('total list= ',num)
print('First=%d, last=%d' % (num[0],num[2]))


# In[63]:


names=['imad','naruto','sasuke','itachi']
print('total names are: ',names)
print('First=%s,last=%s' % (names[0],names[3]))


# In[67]:


for i in range(0,30,3):
    print(i,end=',')


# In[68]:


lst=list(range(0,30,2))
print(lst)


# In[80]:


lst=list(range(1,10))
print(lst)

lst.append(11)
print(lst)
lst.remove(11)
print(lst)
lst.reverse()
print(lst)
lst.copy()
print(lst)
lst.clear()
print(lst)


# In[81]:


while i>=0:
    print(list[i],end='')
    i-=1


# In[85]:


sch1=['imad','naruto','baruto','itachi','sasuke']
sch2=['dami','naruto','baruto','meeni','kakashi']

s1=set(sch1)
s2=set(sch2)
s3=s1.intersection(s2)
print(s3)


# # Tuples

# In[95]:


dict={'Name':'Chandra','Id':'200','Salary':100000}
print('Name of the employee=',dict['Name'])
print('Name of the id=',dict['Id'])
print('Name of the Salary=',dict['Salary'])


# In[98]:


dict={'Name':'Chandra','Id':'200','Salary':100000}
n=len(dict)
print('no of key-value pairs: ',n)


# In[100]:


del dict['Salary']


# In[101]:


dict


# # Dictionary

# In[1]:


dict={'Name':'Chandra','Id':'200','Salary':100000}
print(dict)

print('keys in dict:-',dict.keys())
print('keys in dict:-',dict.values())
print('keys in dict:-',dict.items())


# In[51]:


x={}

print('How many elements? ',end='')
n=int(input())

for i in range(n):
    print('enter the keys: ',end='')
    
    k=input()
    print('enter its value: ',end='')
    
    v=int(input())
    x.update({k:v})
    
    print('the dictionary is: ',x)


# In[52]:


print('How many elements? ',end='')
n=int(input())

for i in range(n):
    print('enter the values: ',end='')
    
    k=input()
    print('enter the key values: ',end='')
    
    v=int(input())
    #print('enter the values: ',end='')
    
    x.update({k:v})
    print('the dic values are : ',x)


# In[24]:


def add_sub(a,b):
    a=a+b
    b=a-b
    c=a*b
    return a,b,c

x,y,z=add_sub(12,12)
print(x)
print(y)


def add_mul(a,b):
        c=a*b
        d=a+b
        return c,d
    
x,y=add_mul(10,30)
print(x)
print(y)


def add_div(a,b):
        c=a*b
        d=a/b
        return c,d
    
x,y=add_div(10,30)
print(x)
print(y)


def add_mod(a,b):
        c=a//b
        d=a+b
        return c,d
    
x,y=add_mod(10,30)
print(x)
print(y)


# In[45]:


x={}

print('enter the number of elements: ')
n=int(input())

for i in range(n):
    print('enter the keys: ',end='')
    k=input()
    print('the the keys')
    v=int(input())
    x.update({k:v})
    
print(x)


# In[46]:


x={}

print('enter the number of elements? ')
n=int(input())

for i in range(n):
    print('the values are ')
    k=input()
    print('the keys are')
    v=int(input())
    x.update({k:v})
    
print(x)


# In[60]:


for i in range(1,11):
    print('* '*(i))


# In[79]:


n=40
n=-1
for i in range(1,11):
    print(' '*n, end='')
    print('* '*(i))
    n-=1
    


# In[68]:


n=40
for i in range(11,1):
    print('     '*n, end='')
    print('* '*(i))
    n-=1


# In[ ]:




