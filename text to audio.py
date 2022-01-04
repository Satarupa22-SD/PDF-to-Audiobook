#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pyttsx3


# In[2]:


pip install pyPDF2


# In[4]:


import pyttsx3
import PyPDF2


# In[5]:


from tkinter.filedialog import *


# In[6]:


book = askopenfilename()
pdfreader=PyPDF2.PdfFileReader(book)
pages = pdfreader.numPages


# In[7]:


for num in range(0,pages)
    page = pdfreader.getPage(num)
    text= page.extractText()
    player=pyttsx3.init()
    player.say(text)
    player.runAndWait()


# In[ ]:




