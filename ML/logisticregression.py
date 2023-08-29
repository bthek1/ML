# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/04_LogisticRegression.ipynb.

# %% auto 0
__all__ = ['df', 'X_train', 'X_test', 'y_train', 'y_test', 'model', 'y_predicted', 'y_probability', 'digits', 'cm', 'report']

# %% ../nbs/04_LogisticRegression.ipynb 5
import pandas as pd
from matplotlib import pyplot as plt


# %% ../nbs/04_LogisticRegression.ipynb 6
df = pd.read_csv("./Data/insurance_data.csv")
df.head()

# %% ../nbs/04_LogisticRegression.ipynb 8
plt.scatter(df.age,df.bought_insurance,marker='+',color='red')

# %% ../nbs/04_LogisticRegression.ipynb 9
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

# %% ../nbs/04_LogisticRegression.ipynb 10
X_train, X_test, y_train, y_test = train_test_split(df[['age']],df.bought_insurance,train_size=0.8)

# %% ../nbs/04_LogisticRegression.ipynb 11
X_test

# %% ../nbs/04_LogisticRegression.ipynb 12
model = LogisticRegression()

# %% ../nbs/04_LogisticRegression.ipynb 13
model.fit(X_train, y_train)

# %% ../nbs/04_LogisticRegression.ipynb 14
X_test

# %% ../nbs/04_LogisticRegression.ipynb 15
y_predicted = model.predict(X_test)
y_predicted

# %% ../nbs/04_LogisticRegression.ipynb 16
y_probability = model.predict_proba(X_test)

# %% ../nbs/04_LogisticRegression.ipynb 17
model.score(X_test,y_test)

# %% ../nbs/04_LogisticRegression.ipynb 18
plt.scatter(df.age,df.bought_insurance,marker='+',color='blue')
plt.scatter(X_test,y_test,marker='+',color='red')
plt.scatter(X_test,y_probability[:,1],marker='+',color='green')
plt.scatter(X_test,y_predicted,marker='*',color='green')

# %% ../nbs/04_LogisticRegression.ipynb 20
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt

# %% ../nbs/04_LogisticRegression.ipynb 21
digits = load_digits()

# %% ../nbs/04_LogisticRegression.ipynb 22
plt.gray() 
for i in range(2):
    plt.matshow(digits.images[i]) 

# %% ../nbs/04_LogisticRegression.ipynb 23
dir(digits)

# %% ../nbs/04_LogisticRegression.ipynb 24
digits.target[:]

# %% ../nbs/04_LogisticRegression.ipynb 25
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

# %% ../nbs/04_LogisticRegression.ipynb 26
model = LogisticRegression()

# %% ../nbs/04_LogisticRegression.ipynb 27
X_train, X_test, y_train, y_test = train_test_split(digits.data,digits.target, test_size=0.2)

# %% ../nbs/04_LogisticRegression.ipynb 28
model.fit(X_train, y_train)

# %% ../nbs/04_LogisticRegression.ipynb 29
model.score(X_test, y_test)

# %% ../nbs/04_LogisticRegression.ipynb 30
model.predict(digits.data[0:5])

# %% ../nbs/04_LogisticRegression.ipynb 31
y_predicted = model.predict(X_test)

# %% ../nbs/04_LogisticRegression.ipynb 32
from sklearn.metrics import confusion_matrix
import seaborn as sn

# %% ../nbs/04_LogisticRegression.ipynb 33
cm = confusion_matrix(y_test, y_predicted)
plt.figure(figsize = (10,7))
sn.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

# %% ../nbs/04_LogisticRegression.ipynb 35
from sklearn.metrics import classification_report

# %% ../nbs/04_LogisticRegression.ipynb 36
report = classification_report(y_test, y_predicted)
print(report)
