
#This notebook will be mainly used for the capstone project.
#These programs will be necessary to analyze data 

import pandas as pd
import requests
from bs4 import BeautifulSoup
print("Imported!")


# In[14]:
#Within the project, these data sources will be used and scrapped using the following programs 

url = "https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M"
extracting_data = requests.get(url).text
wiki_data = BeautifulSoup(extracting_data, 'lxml')


# In[15]: the wikipedia data will be then organized into a graph based on the following parameters

wiki_data


# In[16]: the data will be organized in the following manner


column_names = ['Postalcode','Borough','Neighborhood']
toronto = pd.DataFrame(columns = column_names)

content = wiki_data.find('div', class_='mw-parser-output')
table = content.table.tbody
postcode = 0
borough = 0
neighborhood = 0

for tr in table.find_all('tr'):
    i = 0
    for td in tr.find_all('td'):
        if i == 0:
            postcode = td.text
            i = i + 1
        elif i == 1:
            borough = td.text
            i = i + 1
        elif i == 2: 
            neighborhood = td.text.strip('\n').replace(']','')
    toronto = toronto.append({'Postalcode': postcode,'Borough': borough,'Neighborhood': neighborhood},ignore_index=True)


# In[17]: the data will be cleaned in the following manner 

clean dataframe 
toronto = toronto[toronto.Borough!='Not assigned']
toronto = toronto[toronto.Borough!= 0]
toronto.reset_index(drop = True, inplace = True)
i = 0
for i in range(0,toronto.shape[0]):
    if toronto.iloc[i][2] == 'Not assigned':
        toronto.iloc[i][2] = toronto.iloc[i][1]
        i = i+1


# In[18]:the following data fram will be created 


df = toronto.groupby(['Postalcode','Borough'])['Neighborhood'].apply(', '.join).reset_index()
df


# In[19]:the data frame will be described in the following manner 


df.describe()


# In[20]:


df = df.dropna()
empty = 'Not assigned'
df = df[(df.Postalcode != empty ) & (df.Borough != empty) & (df.Neighborhood != empty)]


# In[21]: the data will be grouped as follows 


def neighborhood_list(grouped):    
    return ', '.join(sorted(grouped['Neighborhood'].tolist()))
                    
grp = df.groupby(['Postalcode', 'Borough'])
df_2 = grp.apply(neighborhood_list).reset_index(name='Neighborhood')


# In[22]:the data will be viewed as followed 


df_2.describe()


# In[23]:the data will be visalized as follows


print(df_2.shape)
df_2.head()


# In[24]:the data will be saved as follows


df_2.to_csv('toronto.csv', index=False)


# In[ ]:




