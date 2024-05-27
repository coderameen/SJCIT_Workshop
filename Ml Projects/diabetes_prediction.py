#import pakages
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import train_test_split
import pandas as pd

#load the dataset
df = pd.read_csv('diabetes.csv')
print(df)

#split the dataset into x-axis(input) and y-axis(output)
x = df.iloc[:,:-1]
y = df.iloc[:,-1]
print(x)
print(y)

#splitting the dataset into training and testing
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.2, random_state=60)


#call Algorithm
model = GaussianNB()

#train the model
model.fit(x_train,y_train)

#predict the output of the model
pred = model.predict([[8,99,84,0,0,35.4,0.388,50]])
print(pred)

if pred[0] == 1:
    print("The patient have diabetes")
else:
    print("The patient doesn't have diabetes")
    