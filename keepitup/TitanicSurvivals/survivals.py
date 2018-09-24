# We can use the pandas library in python to read in the csv file.
import pandas as pd
#for numerical computaions we can use numpy library
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1)

# This creates a pandas dataframe and assigns it to the titanic variable.
titanic = pd.read_csv("datasets/train.csv")

# print(titanic)
# Print the first 5 rows of the dataframe.
# titanic.head()
titanic_test = pd.read_csv("datasets/test.csv")
#transpose
# titanic_test.head().T
#note their is no Survived column here which is our target varible we are trying to predict
#transpose
titanic_transpose = titanic_test.head().T
# print(titanic.head().T)

#shape command will give number of rows/samples/examples and number of columns/features/predictors in dataset
#(rows,columns)
titanic_shape = titanic.shape

#Describe gives statistical information about numerical columns in the dataset
#you can check from count if there are missing vales in columns, here age has got missing values
(titanic.describe())

#info method provides information about dataset like
#total values in each column, null/not null, datatype, memory occupied etc
(titanic.info())

#lets see if there are any more columns with missing values
null_columns=titanic.columns[titanic.isnull().any()]
titanic.isnull().sum()

#how about test set??
print(titanic_test.isnull().sum())

