#!/usr/bin/env python
# coding: utf-8

# <html><center><h2 class="red-text" style="color: red;">scrape a table</h2></center></html>

# In[17]:


import urllib.request
import pandas as pd
url = "https://en.wikipedia.org/wiki/Programming_languages_used_in_most_popular_websites"

with urllib.request.urlopen(url) as i:
    html = i.read()
    
data = pd.read_html(html)[0]
print(data.head())


# In[ ]:




