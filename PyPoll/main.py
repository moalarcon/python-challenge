#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd


# In[3]:


file = "Resources/election_data.csv"


# In[4]:


file_df = pd.read_csv(file)
file_df.head()


# In[8]:


total_votes = file_df.count()
#total_votes_df = pd.DataFrame(total_votes)
#total_votes_df
total_votes


# In[9]:


candidates = file_df['Candidate'].value_counts()
candidates


# In[21]:


percent_votes = file_df['Candidate'].value_counts() / 3521001
percent_votes_df = pd.DataFrame(percent_votes)

percent_votes_df = percent_votes_df.style.format({'Candidate': '{:,.0%}'.format})
percent_votes_df


# In[38]:


print("           Election Results           ")
print("--------------------------------------")
#print("Total Votes: 3,521,001 ; Winner: Khan")
output_df = pd.DataFrame({                      
    "Candidates": ["Total_Votes", "Khan(winner)", "Correy", "Li", "O'Tooley"],
    "Percent_Vote": ["", "63%", "20%", "14%", "3%"],
    "Total_Votes": ["3,521,001", "2,218,231", "704,200","492,940", "105,630"]})
print(output_df)


# In[41]:


output_df.to_csv("Main_Poll.csv", index=False, header=True)


# In[ ]:




