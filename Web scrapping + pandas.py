#!/usr/bin/env python
# coding: utf-8

# ## First Project 
# ### Scrapping Data from Real Website + Pandas

# In[7]:


from bs4 import BeautifulSoup
import requests


# In[13]:


#web scrapping proccess
# Select site you want to scrape
url = "https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue"

# use requests command to collect data and store in a variable
page = requests.get(url)

# use beautifulsoup method to import data from page, safe in a variable. 
# use txt to select type, dont forget to add html to set a pattern
soup = BeautifulSoup(page.text, 'html')

#print variable soup with all the scrapped data from the website
print(soup).prettify


# In[25]:


soup.find_all("table")[1]


# In[24]:


soup.find_all("table", class_ = 'wikitable sortable')


# In[22]:


table = soup.find_all("table")[1]


# In[29]:


print(table)


# In[36]:


world_titles = table.find_all("th")


# In[37]:


world_titles


# In[38]:


world_table_titles = [title.text.strip() for title in world_titles]

print(world_table_titles)


# In[39]:


import pandas as pd


# In[42]:


df = pd.DataFrame(columns = world_table_titles)
df


# In[48]:


column_data = table.find_all('tr')


# In[52]:


for row in column_data[1:]:
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    lenght = len(df)
    df.loc[lenght] = individual_row_data


# In[56]:


df


# In[59]:


df.to_csv(r'C:\Users\dfm_n\OneDrive\Área de Trabalho\companies.csv', index = False)


# In[ ]:




