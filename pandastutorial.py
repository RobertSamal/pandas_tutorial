# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 10:01:13 2022

@author: lodek
"""

#first we need to import pandas to work with data frames
import pandas as pd

mydf = pd.read_csv("HR_comma_sep.csv")

#check the shape of the dataframe
# print(mydf.shape)

# #to display the columns in the CSV
# print(mydf.columns)


# #dislpay the values in the head
# print(mydf.head(7))

# #display the tail of this data frame
# print(mydf.tail(10))

#get the informtion about the data frame
# print(mydf.info())

#describe () gives us a better and detail understanding of dataframe
# print(mydf[["average_montly_hours","last_evaluation"]].describe()) 

print(mydf[["time_spend_company","satisfaction_level"]])

#creating a newdata frame from our current data frame
df2 = mydf[["average_montly_hours","sales","salary"]]

#specifyies index to take [rows,columns]
df3 = mydf.iloc[0:3,2:5]
print(df3)

#we need all rows to 500 and columns 0, 3 , 9
df4 = mydf.iloc[:100,[0,3,9]]

#create new column for our data frame
df4["Feedback"] = "Good"

#add a new column from existing columns
mydf["monthly_hourlypay"]= mydf["average_montly_hours"] * 500

mydf["Total_income"] = mydf["monthly_hourlypay"] + 1000

#deleting a column
del mydf["Total_income"]

#converts the string to upper case
mydf["salary"].str.upper()

#concatunate strings
#we create a new column 
mydf["salary_comments"] = mydf["salary"].str.upper() + "- new salary"


hardworkers = mydf [ ["satisfaction_level","time_spend_company","average_montly_hours"]]

#incorporating conditions and creating a new datframe workers with more than 200 hours
top_hardworkers = hardworkers [  hardworkers["average_montly_hours"] >=200  ]

print(top_hardworkers["average_montly_hours"].min())

#two conditions can be written separately with brackets
hardworkers2 = hardworkers[  (hardworkers["average_montly_hours"]>=200) & (hardworkers["satisfaction_level"]>=0.8) ]


#the one here is a condition for true meaning values will ascend if it was 0 it will be descend
ascendingvalues = hardworkers2.sort_values(["satisfaction_level","time_spend_company","average_montly_hours"],ascending=[1,0,1])

#new column and new series
mydf["Product"] = mydf["satisfaction_level"] * mydf["average_montly_hours"]
testing = mydf["Product"]

mydf_grouped = mydf.groupby(["salary","sales"],as_index=False)["satisfaction_level"].sum()
