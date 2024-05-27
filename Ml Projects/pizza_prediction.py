'''
1.import pakages
2.load dataset
3.split the dataset into x-axis(input) and y-axis(output)
4.split the dataset into training and testing
5.Call/use the Algorithm
6.Train the Model
7.Predict the Output
'''
#pip install pandas
#pip install scikit-learn

#1.import pakages
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import pandas as pd

#2.load dataset
df = pd.read_csv('pizza.csv')
# print(df.tail())
print(df)


#3. split dataset into x-axis(input) and y-axis(output)
x = df[["age","weight"]]
y = df["buy_pizza"]
print(x)
print(y)

#4. split the dataset into training and testing
x_train,x_test,y_train,y_test = train_test_split(x,y, test_size=0.1)

#5.call Algorithm
model = LogisticRegression()

#6.Train the model
model.fit(x_train,y_train)

#7.predict the output of the model
pred = model.predict([[31,109]])
print(pred)

if pred[0] == 1:
    print("Enjoy eating pizza!!")
else:
    print("Go to Gym")
