#!/usr/bin/env python
# coding: utf-8

# In[1]:


## Area


# In[2]:


import numpy as np      # to get the value of pi 


# In[3]:


radius = input("Enter the value of radius : ")    #get the user input of radius
r = float(radius)
area = np.pi * r ** 2                             # formula for area of circle
print("Input of the radius : ", r, " ,area of the circle is", area) 


# In[4]:


## Extension


# In[5]:


file = input("enter the file name : ")
typeoffile = file.split(('.'))
print("File name is : " + file[:], ",the type of file is : " + repr(typeoffile[-1]))


# In[ ]:




