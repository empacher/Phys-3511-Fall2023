#!/usr/bin/env python
# coding: utf-8

# In[83]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'notebook')

def MakeHist():
    ahh = np.random.randn(1000)
    fig = plt.figure()
    be = fig.add_axes([0.1,0.1,0.8,0.8])
    be.set_xlabel('x')
    be.set_ylabel('counts')
    #plt.hist(ahh); why does this not belong here??
    be.set_title('nbins = ') #i tried putting bins and bins(int) into this after a comma. i dont know how to make the number of bins appear in the title!!
    

MakeHist()
plt.hist(ahh,bins = 10);
    
MakeHist()
plt.hist(ahh,bins = 100);
    
MakeHist()
plt.hist(ahh,bins = 1000);
    
    


# In[ ]:





# In[ ]:




