#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import os
import numpy as np


# In[3]:


budget_data = "Resources/budget_data.csv"
budget_data_df = pd.read_csv(budget_data, encoding="ISO-8859-1")


# In[4]:


in_thousands = budget_data_df["Profit/Losses"]
budget_data_df["in Dollars"] = in_thousands.map('${:,.2f}'.format)
budget_data_df.head(20)


# In[5]:


total_months = budget_data_df["Date"].describe().loc[["count"]]
analysis_df = pd.DataFrame(total_months)
rename_months = analysis_df.rename(columns={"Date":"Months"})
rename_months


# In[6]:


net_total = budget_data_df["Profit/Losses"].sum()
print(f'Total Net Profit: $ {net_total}')


# In[7]:


describe = budget_data_df["Profit/Losses"].describe().loc[['mean','min','max']]
describe_df = pd.DataFrame(describe)
describe_df["In Dollars"] = describe.map('${:,.2f}'.format)
describe_df = describe_df[["In Dollars"]]
describe_df


# In[8]:


budget_data_df.loc[budget_data_df.loc[:,"Profit/Losses"]==1170593,:]


# In[9]:


budget_data_df.loc[budget_data_df.loc[:,"Profit/Losses"]==-1196225,:]


# In[10]:


max_min_df = pd.DataFrame({"Type":["Max","Min"],"Case":[25,44],
           "Date":["Feb-2012","Sep-2013"],
           "In Dolars":["$1,170,593.00","-$1,196,225.00"]})
max_min_df


# In[11]:


print("Financial Analysis")
print("---------------------------")
output_df = pd.DataFrame({
    
"Output" : ["Total Months: 86", 
    "Total Net Profit: $ 38,382,578.00", 
    "Average Change: $446,309.05", 
    "Greatest Increase: Feb-2012 $1,170,593.00", 
    "Greatest Decrease: Sep-2013 -$1,196,225.00"]
})

print(output_df)


# In[12]:


output_df.to_csv("main_bank_output.csv", index=False, header=True)


# In[ ]:




