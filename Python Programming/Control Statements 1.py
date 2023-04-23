#!/usr/bin/env python
# coding: utf-8

# In[1]:


import math
r=float(input('enter radius: '))
area=math.pi*r**2
print("the area of circle is : ", area)
print('area of circle= {:0.2f}'. format(area))


# # Control Statements
# 
# # if statements
# # if...else statements
# # if...elif...else statements
# # while loop
# # for loop
# # else suite
# # break statement
# # Continue Statement
# # pass Statement
# # assert statement 
# # return statement

# # The if statement

# In[ ]:


num=1
if num==1:
    print('one')


# In[ ]:


num = int(input("enter the number?"))  
if num%2 == 0:  
    print("Number is even...")  
else:  
    print("Number is odd...")  
        


# In[ ]:


x=9
if num%2==0:
    print('number is even',x)
else:
    print('number is odd',x)
    


# In[ ]:


n=int(input('enter the number: '))
if n%2==0:
    print('number is even',n)
else:
    print('number is odd',n)


# In[ ]:


n=int(input('enter the number: '))
if n%2==0:
    print('number is even',n)
else:
    print('number is odd',n)
   


# In[ ]:


num=-5
if num==0:
    print('is zero',num)
elif num>0:
    print('is positive',num)
else:
    print('is negative',num)


# In[ ]:


num=5
if x==0:
    print('zero')
elif x==1:
    print('one')
elif x==2:
    print('two')
elif x==3:
    print('three')x


# In[ ]:


x=1
while x<=30:
    x+=2
    print(x,end=',')


# In[ ]:


x=1
while x<=30:
    x+=2
    print(x,end=',')


# In[ ]:


for i in range(1,20,2):
    print(i,end=',')


# In[ ]:


str='hello'
for ch in str:
    print(ch,sep='')
else:
    print(ch,end=',')


# In[ ]:


list=[10,20,30,40,50,60,70,80]
for ele in list:
    print(list,end=',')


# In[ ]:


lst=[10,20,30,40]
m sum=0
for i in list:
    print(i)
    sum+=2
    print(sum,end=',')


# In[ ]:


sum=0
for i in range(0,20,2):
    print(i)
    sum+=2


# In[ ]:


i=40
for i in range(0,40,2):
    for j in range(0,40,2):
        i+=2
        j+=2
        print('the values are',i,end=',')
        print('the values are',j,end=',')
        break;

        


# In[ ]:


for i in range(1,11):
    for j in range(1,i+1):
        print("x ",end='')
    print()


# In[ ]:


for i in range(1,11):
    for j in range(1,i+1):
        print('x ',end='')
    print()


# In[ ]:


x=10
while x>=1:
    print('x= ',x)
    x=x-1
   # print('out of loop')


# In[ ]:


x=10
while x>=1:
    print('x= ',x)
    x=x-1
    if x==5:
        break
print('out of loop')


# In[ ]:


def sum(a,b):
    print(a+b)
    
sum(5,10)
sum(15,10)


# In[ ]:


def sub(a,b):
    print(a-b)
sub(5,10)


# In[ ]:


def sum(a,b):
    return a+b

res=sum(5,10)
print('the result is ',res)


# # Fibonacci Series

# In[11]:


given_number = int(input("How many terms? "))

# first two terms
n1=0
n2=1
count=0

print('Fibonacci sequence:')
while count < given_number:
        print(n1)
        n = n1 + n2
       # update values
        n1 = n2
        n2 = n
        count += 1


# In[8]:


given_number=9
n1=0
n2=1
c=0

while c<given_number:
    print(n1)
    n=n1+n2
    n1=n2
    n2=n
    c+=1


# In[9]:


def sum_sub(a,b):
    
    c=a+b
    d=a-b
    return c,d

x,y=sum_sub(10,15)
print('result of addition: ',x)
print('result of subtraction: ',y)


# In[10]:


def sum_sub_mul_div(a,b):
    c=a+b
    d=a-b
    e=a*d
    f=a/d
    return c,d,e,f
x,y,z,r=sum_sub_mul_div(10,24)
print(x,y,z,r,end='')


# In[32]:


def display(str):
    def message():
        return 'how r u ? '
    res=message()+str
    return res
print(display('krishna'))


# In[24]:


def mofify(lst):
    lst=[10,20,30,40]
print(lst,id(lst))


# In[33]:


def attach(s1,s2):
    s3=s1+s2
    print('total string: ',s3)
attach('new','york')


# In[1]:


def grocery(item,price):
    print('item=%s' % item)
    print('price=%.2f' % price)
    
grocery(item='sugar',price=50.34)


# In[10]:


def grocery(item,quality,weight,company,price):
    print('item=%s' % item)
    print('price=%.2f' % price)
    print('quality=%s' % quality)
    print('weight=%d' % weight)
    print('company=%s' % company)

grocery(item='sugar',price=200.0,quality='sanofi',weight=25,company='imad technologies')


# In[13]:


def grocery(item,price=40.0):
    print('item=%s' % item)
    print('price=%f' % price)
    
grocery(item='sugar',price=50.00)
grocery(item='sugar')


# In[16]:


a=1
def myfunction():
    b=2
    print('a= ',a)
    print('b= ',b)
    
myfunction()
print(a)
print(b)


# In[1]:


student=(10,'imad',50,60,65)
len(student)


# In[4]:


fees=(250000.00)*4
print(fees)


# In[7]:


fees=(250000.00,)*4
print(fees,)


# In[1]:


print('enter the elements: ',end='')
n=int(input())

for i in range(n):
    print('enter the keys: ',end='')
    
    k=input()
    print('enter the key values: ',end='')
    
    v=int(input())
    print('enter the values: ',end='')
    x.update({k:v})
    print('the dictionary is',x)


# In[ ]:




