#!/usr/bin/env python
# coding: utf-8

# # Assignment :1
#   ## Use the dictionary, port1 = {21: "FTP", 22:"SSH", 23: "telnet", 80: "http"}, and make a new dictionary in which keys become values and values become keys, as shown: Port2 = {“FTP":21, "SSH":22, “telnet":23,"http": 80}

# In[4]:


port1 = {21:"FTP",22:"SSH",23:"telnet",80:"http"}
port2 = {value:key for key,value in port1.items()}
print(port2)


# # Assignment 2 : 
# 
# Take a list of tuple as shown below.
# [(1,2), (3,4), (5,6),(4,5)]
# Make a new list which contains sum of number of tuples. 
# For example 
# Input 
# [(1,2), (3,4), (5,6)]
# Out put [3,7,11]

# In[8]:


list1 = [(1,2),(3,4),(5,6),(4,5)]
list2 = [sum(i)for i in list1]

print (list2)


# # Assignment 3 :
# 
# Take a list as shown below 
# [(1,2,3), [1,2], ['a','hit','less']]
# The List contains tuple and lists. Make the elements of inner lists and tuples to outer list
# 
# 

# In[12]:


list1 =  [(1,2,3), [1,2], ['a','hit','less']] 
list2 =[]
list2 =[i for each in list1 for i in each]

print(list2)


# In[ ]:




