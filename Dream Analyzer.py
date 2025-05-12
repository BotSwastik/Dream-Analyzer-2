#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv(r"E:\Data Storage\Dream Analyzer\Dream_data.csv")


# In[4]:


df.head(10)


# In[5]:


df.shape


# In[6]:


df["Sleep_time_Updated"] = ["8-10 PM" if 20<= int(t.split(':')[0]) < 22 else
                           "10-11 PM" if 22<= int(t.split(':')[0]) < 23 else
                           "11-12 AM" if 23<= int(t.split(':')[0]) else
                           "12-2 AM" if 0<= int(t.split(':')[0]) < 2 else
                           "2-4 AM" if 2<= int(t.split(':')[0]) < 4 else
                           ">4 AM" for t in df["Sleep_Time"]]


# In[7]:


df["Sleep_time_review"] = ["Good" if t == "8-10 PM" else
                          "Okay" if t == "10-11 PM" else
                          "Bad" if t == "11-12 AM" else
                          "Severe" if t == "12-2 AM" else
                          "Very Severe" if t == "2-4 AM" else
                          "Alarming"
                          for t in df["Sleep_time_Updated"]]


# In[8]:


df["Dream_intensity_updt"] = [1 if t == "Low" else
                             2 if t == "Medium" else
                             3 for t in df["Dream_Intensity"]]


# In[9]:


df["Sleep_Hour"] = pd.to_datetime(df["Sleep_Time"], format="%H:%M").dt.hour


# In[10]:


total_count = df["Dream_ID"].count()
print(total_count)


# In[11]:


df["Dream_Type"].unique()


# In[12]:


df["Dream_Intensity"].unique()


# In[13]:


df["Mood_Before_Sleep"].unique()


# In[14]:


df["Sleep_Duration"].unique()


# In[15]:


df["Sleep_Time"].nunique()


# In[16]:


Freq  = df.groupby("Sleep_Duration")["Dream_ID"].count().reset_index()
Freq.rename(columns={"Dream_ID":"Dream_count"}, inplace = True)
Freq["% Distribution"] = ((Freq["Dream_count"]/total_count)*100).round(2).astype(str)+'%'
Freq.head(15)


# In[17]:


DT_freq  = df.groupby("Dream_Type")["Dream_ID"].count().reset_index()
DT_freq.rename(columns={"Dream_ID":"Dream_count"}, inplace = True)
DT_freq["% Distribution"] = ((DT_freq["Dream_count"]/total_count)*100).round(2).astype(str)+'%'
DT_freq.head(10)


# In[18]:


MBS_freq = df.groupby("Mood_Before_Sleep")["Dream_ID"].count().reset_index()
MBS_freq.rename(columns={"Dream_ID":"Dream_count"}, inplace = True)
MBS_freq["% Distribution"] = ((MBS_freq["Dream_count"]/total_count)*100).round(2).astype(str)+'%'
MBS_freq.head(10)


# In[19]:


df["merged"] = df["Mood_Before_Sleep"]+'-'+df["Dream_Type"]
df.head()


# In[20]:


MRG_freq = df.groupby("merged")["Dream_ID"].count().reset_index()
MRG_freq.rename(columns={"Dream_ID":"Dream_count"}, inplace = True)
MRG_freq = MRG_freq.sort_values(by = "Dream_count", ascending = False) .reset_index()
MRG_freq["% Distribution"] = ((MRG_freq["Dream_count"]/total_count)*100).round(2).astype(str)+'%'
MRG_freq.head(30)


# In[21]:


Time_Freq  = df.groupby("Sleep_time_Updated")["Dream_ID"].count().reset_index()
Time_Freq.rename(columns={"Dream_ID":"Dream_count"}, inplace = True)
Time_Freq = Time_Freq.sort_values(by = "Dream_count", ascending = False) .reset_index()
Time_Freq["% Distribution"] = ((Time_Freq["Dream_count"]/total_count)*100).round(2).astype(str)+'%'
Time_Freq.head(30)


# In[22]:


Time_Dream = df.groupby(["Sleep_Time","Dream_Type"])["Dream_ID"].count().reset_index()
Time_Dream.rename(columns={"Dream_ID":"Dream_count"}, inplace = True)
Time_Dream["% Distribution"] = ((Time_Dream["Dream_count"]/total_count)*100).round(2).astype(str)+'%'
Time_Dream.head(30)


# In[23]:


Col_num = df[["Sleep_Duration", "Sleep_Hour", "Dream_intensity_updt"]]
Col_num.head()


# In[24]:


cor_matt = Col_num.corr()


# In[25]:


# Plot the heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(cor_matt, annot=True, cmap="coolwarm", fmt=".2f")
plt.title("Correlation Heatmap of Sleep Features")
plt.show()


# In[26]:


sns.boxplot(x="Dream_Intensity", y="Sleep_Duration", data=df)

