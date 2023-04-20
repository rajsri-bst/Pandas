import numpy as np
import pandas as pd

dict1={
          "name":["raj","shyam","rohan","kishav"],
          "marks":[70,80,90,100],
          "city":["basti","mathura","delhi","vrindavan"], 
}

arr=pd.DataFrame(dict1)
print(arr)

arr.to_csv("friend_csv")

arr.to_csv("Friends_csv_False",index=False) # this will give data sheet without row index

x=arr.head(2)  # this will print the two uppermost data
print(x)

y=arr.tail(2)  #this will print the two last most two data
print(y)

z=arr.describe()  # this will give the function which will perform only on numerical value
print(z)

arr1=pd.read_csv("Friend_csv")  # this will used to read any  existing data file
print(arr1)


arr2=arr1['marks']  # this will used to print any specific row or column from the data 
print(arr2)

print(arr1['marks'][0])  # this will print specific element from row or column

arr1.index=['first','second','third','fourth'] # this will used to change the index or row  name 
print(arr1)

ser=pd.Series(np.random.rand(34)) #to create pandas data type that is Series 

print(ser)
print(type(ser))

newdf=pd.DataFrame(np.random.rand(334,5),index=np.arange(334)) # to create pandas data type that is Dataframe
print(newdf)
print(type(newdf))

print(newdf.describe())

print(newdf.dtypes)  # it tell me the data type of a column

print(newdf.head())  # it will give uppermost element 

print(newdf.tail())  # it will give the bottom most element

print(newdf.index)   # it will give the index of a row

print(newdf.columns)  # it will give index of a column

x=newdf.to_numpy()   # it will used to convert data into numpy array
print(x)

print(newdf.T)     # it will used to convert row into column and column into row

print(newdf[0])

newdf2=newdf.copy()  # this will used to copy the existing into new
print(newdf2) 

newdf.loc[0,0]=654   # this will used to change any value present into row and column by writing there row and column number
print(newdf)

newdf.columns=list("ABCDE")  # this will used to change the index name oa a column
print(newdf)

newdf.loc[0,'B']=96358
print(newdf)

x=newdf.loc[[0,1],['C','D']]  # this will print specific row or column
print(x)

x=newdf.loc[:,['C','D']]  # this will print each row with specific column
print(x)

x=newdf.loc[[0,1],:]  # this will print each column with specific row
print(x)

x=newdf.loc[(newdf['A']>0.3)] # this will used to print specific column by giving condition
print(x)

x=newdf.loc[(newdf['A']<0.3) & (newdf['C']>0.1)]
print(x)

print(newdf.iloc[0,4])  # this will used to print the specific value when we did not know the the index name e only know the position 
 # and in loc we used when we know the index 


print(newdf.iloc[[0,5],[1,2]])

x=newdf.drop([1])  # this will used to delete the specific row and here by default axis=0 for row
print(x)

x=newdf.drop(['B'],axis=1)  # this will remove the specific column and here axis =1 compulsory to indicates that it is column 
print(x)

newdf.drop(['B'],axis=1,inplace=True)  # this will remove the column permanently
print(newdf)

print(newdf['C'].isnull())   # it check whether it is null or not

x=newdf['C']=None    # it makes all the value to be none
print(x)

print(newdf.shape)        # it will return the number of row and column

print(newdf.info())