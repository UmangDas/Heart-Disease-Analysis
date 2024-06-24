# %% [markdown]
# Heart Disease Project(First stage : Data analysis)

# %% [markdown]
# Importing Libraries

# %%
import pandas as pd 
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import seaborn as sns
%matplotlib inline

# %% [markdown]
# Load the dataset

# %%
Main_dataset=pd.read_csv('heart.csv')
Main_dataset=pd.DataFrame(Main_dataset)

# %% [markdown]
# Displayed the first 10 rows in dataset

# %%
print(Main_dataset.shape)
styled_table=Main_dataset.head(10).style.applymap(lambda x: 'background-color : white; color: black; border: 1px solid black')
styled_table

# %% [markdown]
# Displayed the last 10 row on dataset

# %%
styled_table=Main_dataset.tail(10).style.applymap(lambda x: 'background-color : white; color: black; border: 1px solid black')
styled_table

# %%
# Take a look at the column name 

Main_dataset.columns.values

# %%
# Cheching for null values

Main_dataset.isnull().sum()

# %%
# Concise summary of the dataset

Main_dataset.info()

# %% [markdown]
# Histogram of all Numerical Columns

# %%
Main_dataset.hist(bins=50, grid=False, figsize=(20,15))

# %% [markdown]
# Descriptive Statistics

# %%
desc_stat=Main_dataset.describe()
styled_desc_stat=desc_stat.style.applymap(lambda x: 'background-color : white; color: black; border: 1px solid black').set_caption('Descriptive Statistics')
styled_desc_stat

# %% [markdown]
# HEART DISEASE ANALYSIS QUESTIONS:

# %% [markdown]
# 1.How many people have heart disease and how many don't?
# 
# 2.People of which sex have the most heart disease?
# 
# 3.People of which sex have which type of chest pain?
# 
# 4.People of which chest pain are most prone to have a heart disease?
# 
# 5.What is the disturbance of age among people with and without heart disease?
# 
# 6.What is the average cholesterol level among people with and without heart disease?
# 
# 7.Is there a realationship between exercise included angina(exang) and heart disease?
# 
# 8.How does the slope of the peak exercise SI segment relate to the presence of the heart disease?

# %%
# 1. How many people have heart disease and how many don't?
#  Getting values

print(Main_dataset['target'].value_counts())

# %%
# Visualizing the first question

plt.figure(figsize=(14,6))
colors = ['#4D3425','#E4512B']
sns.set_style('whitegrid')
sns.countplot(x='target',hue='target', data=Main_dataset, palette=colors,legend = True)
plt.title('Heart Disease Distribution')
plt.xlabel('Heart Disease')
plt.ylabel('Count')
plt.xticks([0,1],['No Heart Disease','Heart Disease'])
plt.show()

# %%
# Calculate the count for each category

counts = Main_dataset['target'].value_counts()
lables =['No Heart Disease','Heart Disease']
colors = ['#4D3425','#E4512B']
plt.figure(figsize=(8,8))
plt.pie(counts, labels=lables, colors=colors, autopct='%1.1f%%',startangle=140)
plt.title('Heart Disease Distribution')
plt.show()

# %%
# Checks how many male and female are in the dataset

Main_dataset['sex'].value_counts()

# %%
# Calculate the count for each category

counts = Main_dataset['sex'].value_counts()
lables =['Male','Female']
colors = ['#4D3425','#E4512B']
plt.figure(figsize=(8,8))
plt.pie(counts, labels=lables, colors=colors, autopct='%1.1f%%',startangle=140)
plt.title('Sex Distribution')
plt.show()

# %%
# People who of which sex have the most heart disease?
# Creating a cross tabulation(Crosstab)

cross_tab=pd.crosstab(Main_dataset['sex'],Main_dataset['target'])
cross_tab

# %%
# Plotting the countplot

plt.figure(figsize=(14,6))
colors = ['#4D3425','#E4512B']
sns.countplot(x='sex',hue='target', data=Main_dataset)
plt.title('Heart Disease By Sex')
plt.xlabel('Sex')
plt.ylabel('Count')
plt.xticks([0,1],['Male','Female'])
plt.legend(title ='Heart Disease',labels =['No Heart Disease','Heart Disease'])
plt.show()

# %%
# 3.People of which sex have which type of chest pain?
# counting the values for each chest pain type

cp_counts = Main_dataset['cp'].value_counts()
plt.figure(figsize=(12,8))
cp_counts.plot(kind='bar', color=['#4D3425','#E4512B','#2ECC71','#F39C12'])
plt.title('Chest Pain Type VS count')
plt.xlabel('Chest Pain Type')
plt.ylabel('Count')
plt.xticks(rotation =90)
plt.grid(axis='x')
plt.show()

# %%
# Creating a cross tabulation(Crosstab)

cross_tab=pd.crosstab(Main_dataset['cp'],Main_dataset['sex'])
cross_tab

# %%
# Distribution of chest pain type by sex

pd.crosstab(Main_dataset.sex,Main_dataset.cp).plot(kind='bar',figsize=(14,6),color=['#4D3425','#E4512B','#2ECC71','#F39C12'])
plt.xticks(rotation=0)
plt.title('Type of chest pain by sex')
plt.xlabel('0 = Female, 1 = Male')

# %%
# 4. People with which chest pain are most prone to have heart disease?
# Creating a cross tabulation(Crosstab)

cross_tab=pd.crosstab(Main_dataset['cp'],Main_dataset['target'])
cross_tab


# %%
# Plotting the countplot

plt.figure(figsize=(14,6))
colors = ['#4D3425','#E4512B']
sns.countplot(x='cp',hue='target', data=Main_dataset)
plt.title('Heart Disease By Chest Pain Type')
plt.xlabel('Chest Pain Type')
plt.ylabel('Count')
plt.xticks([0,1,2,3])
plt.legend(title ='Heart Disease',labels =['No Heart Disease','Heart Disease'])
plt.show()

# %%
# 5. What is the distribution of age among people with and without heart disease?

cross_tab=pd.crosstab(Main_dataset['age'],Main_dataset['target'])
cross_tab

# %%
# Plotting the countplot

plt.figure(figsize=(14,6))
colors = ['#4D3425','#E4512B']
sns.histplot(x='age',hue='target', data=Main_dataset, multiple='stack',kde=True)
plt.title('Age Distribution By Heart disease')
plt.xlabel('Age')
plt.ylabel('Count')
plt.legend(title ='Heart Disease',labels =['No Heart Disease','Heart Disease'])
plt.show()

# %%
# 6. what is the average cholesterol level in people with and without heart disease?
# Cross tabulation

chol_bins = pd.cut(Main_dataset['chol'],bins = [0,20,239,500], labels=['Desirable','Borderline high','High'])
Main_dataset['chol_category']=chol_bins

# Creating the cross tabulation

cross_tab=pd.crosstab(Main_dataset['chol_category'],Main_dataset['target'])
cross_tab


# %%
# Violin plot

plt.figure(figsize=(14,6))
sns.violinplot(x='target',y='chol',data=Main_dataset,hue='target',palette=['#4D3425','#E4512B'],dodge=False)
plt.title('Cholesterol Level By Heart Disease')
plt.xlabel('Heart Disease')
plt.ylabel('Cholesterol Level')
plt.xticks([0,1],['No Heart Disease','Heart Disease'])
plt.show()

# %%
# 7.Is there a realtionship between exercise induced angina(exang) and heart disease?
# Creating the cross tabulation(Crosstab)

cross_tab=pd.crosstab(Main_dataset['exang'],Main_dataset['target'],margins=True)
cross_tab

# %%
# Plotting the countplot

plt.figure(figsize=(14,6))
colors = ['#4D3425','#E4512B']
sns.countplot(x='exang',hue='target', data=Main_dataset)
plt.title('Exercise Induced Angina By Heart Disease')
plt.xlabel('Exercise Induced Angina')
plt.ylabel('Count')
plt.xticks([0,1],['No','Yes'])
plt.legend(title ='Heart Disease',labels =['No Heart Disease','Heart Disease'])
plt.show()

# %%
# 8. How  does the slope of the peak exercise SI segment relate to heart disease?
# Creating the cross tabulation(Crosstab)

cross_tab=pd.crosstab(Main_dataset['slope'],Main_dataset['target'],margins=True)
cross_tab

# %%
# Plotting the countplot

plt.figure(figsize=(14,6))
colors = ['#4D3425','#E4512B']
sns.countplot(x='slope',hue='target', data=Main_dataset)
plt.title('Slope Of The Peak Exercise ST Segment By Heart Disease')
plt.xlabel('Slope Of The Peak Exercise ST Segment')
plt.ylabel('Count')
plt.xticks([0,1,2],[0,1,2])
plt.legend(title ='Heart Disease',labels =['No Heart Disease','Heart Disease'])
plt.show()

# %%
plt.figure(figsize=(14,6))
sns.histplot(data=Main_dataset,x='age',bins=30,kde=True,edgecolor='black')
plt.title('Distribution plot with Normal Distribution')
plt.xlabel('Age')
plt.ylabel('Density')
plt.show()

# %%
plt.figure(figsize=(14,6))
sns.histplot(data=Main_dataset,x='thalach',bins=30,kde=True,color='red',edgecolor='black')
plt.title('Distribution plot for Maximum Heart Rate')
plt.xlabel('Maximum Heart Rate')
plt.ylabel('Density')
plt.show()


