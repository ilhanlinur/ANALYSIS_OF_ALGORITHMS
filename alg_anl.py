#!/usr/bin/env python
# coding: utf-8

# In[1]:


import ctypes


# In[4]:


class DynamicArray:
    
    def __init__(self):

        self._n=0 
        self._capacity = 1 
        self._A = self._make_array(self._capacity)
    def __len__(self):

        return self._n
    
    def __getitem__(self, k):

        if not 0 <= k < self._n:
            raise IndexError('invalid inde')
        return self._A[k]
    
    def append(self, obj):
        if self._n == self._capacity: 
            self._resize(2*self._capacity) 
        self._A[self._n] = obj
        self._n += 1
        
    def _resize(self, c): 

        B = self._make_array(c) 
        for k in range(self._n): 
            B[k] = self._A[k]
        self._A=B 
        self._capacity = c
    def _make_array(self, c): 

        return (c*ctypes.py_object)( )
    


# In[3]:


c=DynamicArray()
for i in range(10):
    c.append("add an item"+ str(1))
    print(str(i)+" eklendi, dizi boyutu: "+ str(c.__len__()))


# In[44]:





# In[45]:





# In[46]:





# In[47]:





# In[ ]:





# In[ ]:




