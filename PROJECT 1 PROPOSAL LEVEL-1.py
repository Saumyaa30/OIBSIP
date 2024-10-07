#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# #Data Loading and Cleaning: Load the retail sales dataset.

# In[12]:


df1 = pd.read_csv('retail_sales_dataset.csv')
df1


# In[13]:


df2 = pd.read_csv('menu.csv')
df2


# In[14]:


# Check for missing values
df1.isnull().sum()


# In[15]:


# Check for missing values
df2.isnull().sum()


# In[16]:


df = pd.concat([df1, df2], ignore_index=True)


# In[17]:


df.isnull().sum()


# In[18]:


df.fillna(method='ffill', inplace=True)


# In[19]:


df.drop_duplicates(inplace=True)


# In[20]:


print(df.describe())


# In[21]:


df.columns


# In[22]:


df.columns = df.columns.str.strip() 


# In[23]:


print(df.head())


# In[24]:


print(df.tail())


# In[25]:


df1.drop_duplicates(inplace=True)


# In[26]:


df2.drop_duplicates(inplace=True)


# #Descriptive Statistics: Calculate basic statistics (mean, median, mode, standard deviation).

# In[28]:


# Descriptive statistics
descriptive_stats = df.describe(include='all')  # Include all columns
print(descriptive_stats)


# In[29]:


print(df.head())


# In[30]:


print(df.columns)


# In[31]:


# Calculate mean
mean_Age = df['Age'].mean()
print(f'Mean: {mean_Age}')


# In[32]:


# Calculate median
median_Age = df['Age'].median()
print(f'Median: {median_Age}')


# In[33]:


# Calculate mode
mode_Age = df['Age'].mode()
print(f'Mode: {mode_Age.tolist()}')  


# In[34]:


# Calculate standard deviation
std_dev_Age = df['Age'].std()
print(f'Standard Deviation: {std_dev_Age}')

#Time Series Analysis: Analyze sales trends over time using time series techniques.
# In[51]:


df = pd.read_csv('retail_sales_dataset.csv')


# In[52]:


df


# In[53]:


df.columns


# In[54]:


df['Date'] = pd.to_datetime(df['Date'])


# In[55]:


df.set_index('Date', inplace=True)


# In[56]:


print(df.head())


# In[57]:


monthly_sales = df.resample('M')['Total Amount'].sum()


# In[58]:


print(monthly_sales.head())


# In[59]:


plt.figure(figsize=(12, 6))
plt.plot(monthly_sales.index, monthly_sales, marker='o')
plt.title('Monthly Sales Trend')
plt.xlabel('Date')
plt.ylabel('Total Amount')
plt.grid()
plt.show()


# #Customer and Product Analysis: Analyze customer demographics and purchasing behavior.

# #Analyze customer demographics

# In[67]:


gender_counts = df['Gender'].value_counts()


# In[68]:


print("Gender Distribution:")
print(gender_counts)


# In[74]:


gender_counts.plot(kind='bar', color=['pink', 'blue'])
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()


# In[75]:


# Plot age distribution
plt.figure(figsize=(12, 6))
plt.hist(df['Age'], bins=20, color='green', edgecolor='black')
plt.title('Age Distribution of Customers')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.grid()
plt.show()


# #Analyze purchasing Behaviour

# In[76]:


amount_by_gender = df.groupby('Gender')['Total Amount'].sum()


# In[77]:


print("Total Amount Spent by Gender:")
print(amount_by_gender)


# In[100]:


# Plot total amount spent by gender
amount_by_gender.plot(kind='bar', color=['pink', 'blue'])
plt.title('Total Amount Spent by Gender')
plt.xlabel('Gender')
plt.ylabel('Total Amount')
plt.show()


# In[80]:


# Create age groups
bins = [0, 18, 25, 35, 45, 55, 65, 100]
labels = ['<18', '18-24', '25-34', '35-44', '45-54', '55-64', '65+']
df['Age Group'] = pd.cut(df['Age'], bins=bins, labels=labels)


# In[81]:


avg_purchase_by_age = df.groupby('Age Group')['Total Amount'].mean()


# In[82]:


print("Average Purchase Amount by Age Group:")
print(avg_purchase_by_age)


# In[84]:


# Plot average purchase amount by age group
avg_purchase_by_age.plot(kind='bar', color='cyan')
plt.title('Average Purchase Amount by Age Group')
plt.xlabel('Age Group')
plt.ylabel('Average Purchase Amount')
plt.show()


# In[85]:


sales_by_category = df.groupby('Product Category')['Total Amount'].sum()


# In[86]:


print("Total Sales by Product Category:")
print(sales_by_category)


# In[88]:


# Plot total sales by product category
sales_by_category.plot(kind='bar', color='yellow')
plt.title('Total Sales by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales')
plt.show()


# #Visualization:Present insights through bar charts,line plots,and heatmaps.(bar charts and line plots are already done in above)

# In[109]:


pivot_table = df.pivot_table(values='Total Amount', index='Product Category', columns='Gender', aggfunc='sum')


# In[110]:


pivot_table


# In[111]:


plt.figure(figsize=(10, 6))
sns.heatmap(pivot_table, annot=True, fmt=".2f", cmap='YlGnBu', cbar_kws={'label': 'Total Amount'})
plt.title('Total Sales by Product Category and Gender')
plt.xlabel('Gender')
plt.ylabel('Product Category')
plt.show()


# #Thank you
