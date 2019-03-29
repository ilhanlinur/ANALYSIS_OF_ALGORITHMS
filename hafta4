#!/usr/bin/env python
# coding: utf-8

# In[2]:


#matrix_1   mxn
#matrix_2   nxp
#matrix_3=matrix_1  *  matrix_2    ,  mxp


# In[6]:


def get_value_from_row_col(r_1,c_1):   #O(n)
    t=0
    for i in range(len(r_1)):
        t=t+r_1[i]*c_1[i]
    return t
a=[1,2,3,4]
b=[5,6,7,8]

get_value_from_row_col(a,b)


# In[18]:


b=[[1,2,3,4],[5,6,7,8],[1,2,3,4],[5,6,7,8]]     #4x4
a=[[1,2,3,4],[5,6,7,8]]    #2x4 matrix


# In[21]:


def get_row_from_matrix(a,i):
    return a[i]
def get_col_from_matrix(a,j):
    col=[]
    for row in a:
        col.append(row[j])
#         for indis in range(len(row)):
#             if (indis==j):
#                 col.append(row[indis])
                
    return col
get_col_from_matrix(a,1)


# In[29]:


def matrix_multiply(m_1,m_2):    
    m=len(m_1)
    n=len(m_2[0])
    r=[]
    for i in range(m):
        r.append([])
        for j in range(n):
            a=get_row_from_matrix(m_1,i)
            b=get_col_from_matrix(m_2,j)
            c=get_value_from_row_col(a,b)
            r[i].append(c)
    return r
matrix_multiply(a,b)


# In[41]:


def matrix_multiply(m_1,m_2):     #O(mnp), kare matris olursa O(n^3)
    m=len(m_1)
    n=len(m_2[0])
    r=[]
  
    for i in range(m):
        r.append([])
        for j in range(n):
            a=get_row_from_matrix(m_1,i)
            b=get_col_from_matrix(m_2,j)
            c=get_value_from_row_col(a,b)
            r[i].append(c)
    return r
a=[[1,2,3,4],[5,6,7,8]]
b=[[1,2,3],[5,6,7],[1,2,4],[5,7,8]]
matrix_multiply(a,b)


# In[ ]:





# In[ ]:




