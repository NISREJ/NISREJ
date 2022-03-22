#!/usr/bin/env python
# coding: utf-8

# In[100]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[101]:


data = pd.read_csv('petrol.csv')


# In[102]:


print(data)


# In[103]:


plt.figure()
plt.subplot(2 , 2, 1)
plt.hist(data['Delhi'],label='delhi',density=True)
plt.legend()


plt.subplot(2 , 2, 2)
plt.hist(data['Kolkata'],label='kolkata',density=True, color='r')
plt.legend()


plt.subplot(2 , 2, 3)
plt.hist(data['Mumbai'],label='mumbai',density=True, color='g')
plt.legend()

plt.subplot(2 , 2, 4)
plt.hist(data['Chennai'],label='chennai',density=True, color='m')
plt.legend()
plt.show()


# In[104]:


names =['delhi','kolkata','mumbai','chennai']
ret =[data['Delhi'],data['Kolkata'],data['Mumbai'],data['Chennai']]


# In[105]:


plt.figure()
plt.boxplot(ret , labels=names)
plt.show()


# In[106]:


plt.figure()
fig, ax = plt.subplots(1,1)
plt.violinplot(ret)
ax.set_xticks([1,2,3,4])
ax.set_xticklabels(names)
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




