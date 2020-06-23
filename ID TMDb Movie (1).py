#!/usr/bin/env python
# coding: utf-8

# 
# 
# # Project: Investigate a Dataset (TMDB-Movies)
# 
# ## Table of Contents
# <ul>
# <li><a href="#intro">Introduction</a></li>
# <li><a href="#wrangling">Data Wrangling</a></li>
# <li><a href="#eda">Exploratory Data Analysis</a></li>
# <li><a href="#conclusions">Conclusions</a></li>
# </ul>
# 
# <a id='intro'></a>
# ## Introduction
# 
# This data set contains information about 10,000 movies collected from the Movie Database (TMDb).
# 
# ### Questions
# #### Q1. Which the Six movies are most famous based on popularity score ?
# #### Q2. Which year were the lesser of movies released ? and how many movies released at that year?
# #### Q3. What is the five movies got lowest rated based on the vote average?
# #### Q4. Top Highest revenue Movies of all time Worldwide
# #### Q5. What is the budget trends of movies from year to year?
# #### Q6. Is the release year effect on popularity score of the movies?
# 
# 
# 

# In[249]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# <a id='wrangling'></a>
# ## Data Wrangling
# 
# 
# 
# ### General Properties

# In[250]:


#Importing data from a CSV file and viewing first five rows of the DataFrame
df = pd.read_csv('tmdb-movies.csv')
df.head()


# In[251]:


#Number of rows and columns
df.shape


# In[252]:


#Index, Datatybe and Memory information
df.info()


# 
# 
# ### Data Cleaning (Replace this with more specific notes!)

# In[253]:


#Convert the Dtype 
df['release_date'] = pd.to_datetime(df['release_date'])


# In[254]:


#Type of each column
df.dtypes


# In[255]:


#columns I'm not going to use
df.drop(labels = ['imdb_id','cast','homepage','director','tagline','keywords','overview','production_companies','genres'],axis =1,inplace =True)


# In[256]:


df.info()


# In[257]:


#Checks for null values
df.isnull().sum()


# In[258]:


#Checking if our dataset contains zero or less than zero
BA_zero = df[df.budget_adj == 0]
B_zero = df[df.budget == 0]
RA_zero = df[df.revenue_adj == 0]
R_zero = df[df.revenue == 0]


# <a id='eda'></a>
# ## Exploratory Data Analysis
# 
# > Now that I trimmed and cleaned my data, I'm ready to move on to exploration. Compute statistics and create visualizations with the goal of addressing the research questions that I posed in the Introduction section.
# 
# ### Q1. Which the Six movies are most famous based on popularity score ?
# 

# In[259]:


#Sorts values by popularity in descending order
movies_pop = df.sort_values(by = 'popularity', ascending = False).loc[:,['popularity','original_title']][0:6]


# ##### Based on the below Bar plot we can found the Jurassic world movie got the highest value of Popularity a
# 

# In[260]:


#Shape size
plt.figure(figsize = (8,4))
#Bar plot
ax=sns.barplot(x = 'original_title' , y = 'popularity', data =movies_pop) 
ax.set_xticklabels(ax.get_xticklabels(), rotation=10, fontsize = 10 , ha="right") #Size of the font and rotation
plt.xlabel('Movies' , fontsize = 13) #Name of xlabel
plt.ylabel('Popularity' , fontsize = 13) #Name of Ylabel
plt.title('Most Six Famous Movies',fontsize = 15) #Name of the chart
plt.show()


# ### Q2. Which year were the lesser of movies released ? and how many movies released at that year?

# In[261]:


#Counts the movies released for each year and Sorts values in ascending order
df['release_year'].value_counts(ascending = True)[0:5]


# ### Q3. What is the five movies got lowest rated based on the vote average?

# In[262]:


#Sorts values by vote_average in ascending order
df.sort_values(by = 'vote_average' , ascending = True).loc[:,['vote_average','original_title']][0:5]


# ### Q4. Top Highest revenue Movies of all time Worldwide

# In[263]:


df.sort_values(by = 'revenue',ascending = False).loc[:,['revenue', 'original_title']][0:10]


# In[264]:


movies_revenue = df.sort_values(by = 'revenue',ascending = False).loc[:,['revenue', 'original_title']][0:10]


# ##### Based on the below Line chart we can found the Avatar movie got the highest  revenue (2781505847$)

# In[265]:


#Chart size
plt.figure(figsize = (12,3))
#Line chart
ag=sns.pointplot(x= "original_title", y= "revenue", data= movies_revenue);
ag.set_xticklabels(ag.get_xticklabels(), rotation = 20,ha='right', fontsize = 9);#Size of the font and rotation
plt.xlabel('Movies',fontsize = 9); #Name of xlabel
plt.ylabel('Revenue',fontsize = 9);#Name of ylabel
plt.title('Top Movies revenue',fontsize = 14); #Name of the chart
plt.show()


# ### Q5. What is the budget trends of movies from year to year?
# 

# In[266]:


#Sorts values by budget in descending order
def sort_by_budget(df):
    return df.sort_values(by = 'budget_adj',ascending = False)['original_title'].head(1)


# In[267]:


df.groupby('release_year').apply(sort_by_budget) #applies a function  across each 


# ### Q6. Is the release year effect on popularity score of the movies?
# 

# In[268]:


#Finds the median of each columns
gb_year= df.groupby('release_year').median()


# In[269]:


gb_year['release_year'] = gb_year.index.get_level_values(0)


# ##### - Based on the below Scatter plot there is a positive correlation between release year and popularity
# ##### - The trend  of the below scatter plot is increases year by year
# 
# 

# In[270]:


#Chart size
plt.figure(figsize = (15,11)) 
#Scatter plot
sns.lmplot(x = 'release_year', y = 'popularity', data = gb_year); 
plt.xlabel('Release Year', fontsize = 16); #Name of xlabel
plt.ylabel('Popularity', fontsize = 16); #Name of ylabel
plt.title('Popularity Vs Release Year ',fontsize = 17); #Name of the chart


# ### Conclusion
# 
# ##### After following the analysis steps on my data, now I've a general overview of the data and I found answers to my fourth questions as the below results:
# - The most famous movie based on popularity score is ( Jurrasic World ).
# - In 1961 and 1969 only 31 movies are released, and that result was the lowest value at all the years.
# - (Manos: The Hands of Fate) and (Transmorphers) are the only two movies got the lowest rated of vote average 1.5
# - (Avatar) the highest grossing movie at all the years.
# -
# - Popularity of movies incresing year by year and this means there's a positive correlation between the year and popularity
# 
# ### Limitations
# 
#  There is some missing values or nan values which can effect on results of the data, also the revenue and budget columns they don't have currency unit! also in those two columns had many errorneous zero values l which would have definitely affected my analysis whereas dropping rows with missing values could have effect on my overall analysis.

# In[271]:


from subprocess import call
call(['python', '-m', 'nbconvert', 'Investigate_a_Dataset.ipynb'])

