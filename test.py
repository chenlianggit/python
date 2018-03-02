
# coding: utf-8

# In[1]:


import tensorflow as tf


# In[3]:


matrix1 = tf.constant([[3., 3.]])


# In[4]:


matrix2 = tf.constant([[2.],[2.]])


# In[5]:


product = tf.matmul(matrix1, matrix2)


# In[6]:


sess = tf.Session()


# In[9]:


result = sess.run(product)
print (result)


# In[ ]:





# In[ ]:




