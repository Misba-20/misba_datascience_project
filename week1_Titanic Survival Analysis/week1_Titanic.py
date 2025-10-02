#1)Pandas to read the data
print("--------------1)Original data set----------------")
import pandas as pd
import matplotlib.pyplot as mp
titanic=pd.read_csv("gender_submission.csv")
print(titanic)
#2)Rename columns
print("---------2)a)Renaming Columns using inplace--------------")
titanic.rename(columns={"PassengerId":"ID","Survived":"Status for clarity"},inplace=True)
print(titanic)
print("---------b)Renaming Columns using new variable--------------")
new=titanic.rename(columns={"PassengerId":"ID","Survived":"Status for clarity"})
print(new)
#Explore the dataset
print("---------3)->a)Head--------------")
print(titanic.head(10))
print("---------b)Tail--------------")
print(titanic.tail(10))
print("---------c)Information--------------")
print(titanic.info())
print("---------d)Shape--------------")
print("Shape:",titanic.shape)
#Filter data
print("--------------4)->a)Extract the top 10 survivors-------------------")
filters=titanic[titanic["Status for clarity"]==1].head(10)
print(filters)
print("------------------b)Extract the top 10 non-survivors-------------")
filters=titanic[titanic["Status for clarity"]==0].head(10)
print(filters)
#Compute counts
print("----------------------5)Total number of survival and non survival----------------------")
count=titanic["Status for clarity"].value_counts()
print("only count:",count)
print("Total number of survivors:",count[1])
print("Total number of non-survivors:",count[0])
#Calculate percentages
print("---------------------6)Percentage---------------------")
total=len(titanic)
survivors=count[1]
percentage=survivors/total
print("percentage of survivors:",percentage)
non_survivors=count[0]
percentage=non_survivors/total
print("percentage of  non-survivors:",percentage)

count.plot(kind='bar',color=["pink","violet"])
mp.xlabel("Status 0=Not Survived,1=Survived")
mp.ylabel("no.of persons")
mp.title("Survived vs non survived")
mp.xticks(rotation=0)
mp.show()