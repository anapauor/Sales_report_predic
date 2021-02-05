
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model

df = pd.read_csv("/home/ana/Documentos/Proyectos/Sales/all_data.csv")

print(df.head())
prod_per_year = (df.groupby('month')['totalprod']).mean()
X = (prod_per_year.reset_index())['year']
X = X.values.reshape(-1, 1)
y = (prod_per_year.reset_index())['totalprod']

plt.scatter(X, y)
plt.show()

regr = linear_model.LinearRegression()
regr.fit(X, y)
m =regr.coef_
b = regr.intercept_
print(m, b)

y_predict = regr.predict(X)

plt.plot(X, y_predict)
plt.show()

X_future = np.array(range(2013, 2050))
X_future = X_future.reshape(-1, 1)

future_predict = regr.predict(X_future)
plt.plot(X_future, future_predict)
plt.show()