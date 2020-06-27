#!/usr/bin/env python
# coding: utf-8

# In[7]:


# 1. Length of a string
str=input("Enter the string:")
print("Length of the input string is:",len(str))


# In[8]:


# 2. Character Frequency
def char_frequency(str1):
    dict={ }
    for n in str1:
        keys=dict.keys()
        if n in keys:
            dict[n]+=1
        else:
            dict[n]=1
    return dict
print(char_frequency('google.com'))


# In[9]:


#3. To get a single string from two string
def chars_mix_up(a,b):
    new_a=b[:2]+a[2:]
    new_b=a[:2]+b[2:]
    return new_a+' '+new_b
print(chars_mix_up('abc','xyz'))


# In[11]:


# string display in uppercase and lower case
user_input=input("What's your fav language?")
print("My fav language is",user_input.upper())
print("My fav language is",user_input.lower())


# In[12]:


# To remove a newline in python
str1='Python Exercise\n'
print(str1)
print(str1.rstrip())


# In[13]:


# To count occurrence of a substring
str1='The quick brown fox jumps over the lazy dog.'
print()
print(str1.count("fox"))
print()


# In[15]:


# convert a string in a list
str1='Apple,Mango,Banana'
print(f'list of items={str1.split(",")}')


# In[14]:


# To print character of astring using loop
x=input("Enter the string")
for i in x:
    print(i)


# In[16]:


# To find the length without using len()
a="refrigerator"
count=0
for i in a:
    count=count+1
print(count)


# In[10]:


# python program to delete a character 
a=[1,2,3,4,5,6]
del a[1:3]
print(a)


# In[ ]:




