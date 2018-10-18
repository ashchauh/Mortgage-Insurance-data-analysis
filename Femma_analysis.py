
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import sklearn
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


df_femma=pd.read_csv(r'C:\Users\achauhan\Desktop\Radian\Fema_data\Important_Fema\DisasterDeclarationsSummaries.csv')


# In[3]:


df_femma.info()


# In[4]:


df_femma.head()


# In[5]:


df_femma.describe()


# In[12]:


df_2000=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty00.xlsx')


# In[13]:


df_2001=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty01.xlsx')


# In[14]:


df_2002=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty02.xlsx')


# In[15]:


df_2003=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty03.xlsx')


# In[16]:


df_2004=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty04.xlsx')


# In[17]:


df_2005=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty05.xlsx')


# In[18]:


df_2006=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty06.xlsx')


# In[19]:


df_2007=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty07.xlsx')


# In[20]:


df_2008=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty08.xlsx')


# In[21]:


df_2009=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty09.xlsx')


# In[22]:


df_2010=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty10.xlsx')


# In[23]:


df_2011=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty11.xlsx')


# In[24]:


df_2012=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty12.xlsx')


# In[25]:


df_2013=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty13.xlsx')


# In[26]:


df_2014=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty14.xlsx')


# In[27]:


df_2015=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty15.xlsx')


# In[28]:


df_2016=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty16.xlsx')


# In[30]:


df_2017=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Unemployment_data\laucnty17.xlsx')


# In[35]:


frames=[df_2000,df_2001,df_2002,df_2003,df_2004,df_2005,df_2006,df_2007,df_2008,df_2009,df_2010,df_2011,df_2012,df_2013,df_2014,df_2015,df_2016,df_2017]


# In[37]:


df_unemp=pd.concat(frames,sort=False)


# In[39]:


df_unemp.head()


# In[40]:


df_unemp.info()


# In[42]:


#df_unemp.describe()


# In[6]:


df_femma['state'].value_counts()


# In[7]:


df_femma


# In[8]:


#shape(df_femma)


# In[8]:


df_femma['incidentType'].value_counts()


# In[18]:


"""fig1, ax1 = plt.subplots()
sizes=df_femma['incidentType']
labels='No Data', 'Full', 'Full Doc'
explode = (0.1, 0, 0) 
ax1.pie(sizes, labels=labels, explode= explode, autopct='%1.1f%%',
        shadow=True, startangle=90)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

plt.show()"""
grade_type=df_femma['incidentType'].value_counts()


# In[20]:


sns.set(style="darkgrid")
sns.barplot(grade_type.values,grade_type.index, alpha=.99)
plt.title('Frequency Distribution')
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Incident Type', fontsize=12)
plt.show()


# In[23]:


corrmat = df_femma.corr()
f, ax = plt.subplots(figsize=(10, 10))
sns.heatmap(corrmat, square=True);


# In[25]:


corrmat


# In[27]:


df_cleaned=pd.read_excel(r'C:\Users\achauhan\Desktop\Radian\Fema_data\Important_Fema\cleaned.xlsx')


# In[28]:


df_cleaned.info()


# In[33]:


Ind_house=df_cleaned['ihProgramDeclared']


# In[31]:


"""sns.set(style="darkgrid")
sns.barplot(grade_type.values,grade_type.index, alpha=.99)
plt.title('Frequency Distribution')
plt.ylabel('Number of Occurrences', fontsize=12)
plt.xlabel('Incident Type', fontsize=12)
plt.show()"""


# In[ ]:


#df_pivot=df_state_agg.pivot_table("""index='Address State'""", values='', aggfunc='mean')


# In[67]:


sizes=Ind_house.value_counts()
fig1, ax1 = plt.subplots()

#explode = (0.1, 0, 0) 
ax1.pie(sizes, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.legend(loc=1, labels={0:'Not Declared',1:"Declared"})
plt.title('Percentage of Individuals and household was declared for the disaster')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[66]:


sizes=df_cleaned['iaProgramDeclared'].value_counts()
fig1, ax1 = plt.subplots()

#explode = (0.1, 0, 0) 
ax1.pie(sizes, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.legend(loc=1, labels={0:'Not Declared',1:"Declared"})
plt.title('Percentage of individual Assistance program was declared for this disaster')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[65]:


sizes=df_cleaned['paProgramDeclared'].value_counts()
fig1, ax1 = plt.subplots()

#explode = (0.1, 0, 0) 
ax1.pie(sizes, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.legend(loc=1, labels={1:'Declared',0:"Not Declared"})
plt.title('Percentage of Public Assistance program was declared for this disaster')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()


# In[68]:


sizes=df_cleaned['hmProgramDeclared'].value_counts()
fig1, ax1 = plt.subplots()

#explode = (0.1, 0, 0) 
ax1.pie(sizes, autopct='%1.1f%%', shadow=True, startangle=90)
ax1.legend(loc=1, labels={0:'Declared',1:"Not Declared"})
plt.title('Percentage of Hazard Mitigation program was declared for this disaster')
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.show()

