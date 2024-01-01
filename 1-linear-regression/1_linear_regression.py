# -*- coding: utf-8 -*-
"""1-linear-regression.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Y78N2vkR4ZvLqzeInj9iAn2qe4QgFiRC

# Linear regression

### Data
![image.png](data:image/png;base64,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)
"""

from sklearn.linear_model import LinearRegression
import numpy as np

## data
xonalar = [1, 2, 3, 5, 6, 7]
narxlar = [150, 200, 250, 350, 400, 450]

# listni numpyga o'tkazishimiz kerak, chunki sklearn numpy asosida ishlaydi
X = np.array(xonalar).reshape(-1, 1)
y = np.array(narxlar)
print(X.shape)
print(y.shape)

"""## O'rganish jarayoni"""

model = LinearRegression()
model.fit(X, y)

"""## Bashorat qilish (predict)"""

yangi_data_point = np.array(4).reshape(-1, 1)
yangi_narx = model.predict(yangi_data_point)
print(yangi_narx)

yangi_data_point = np.array(8).reshape(-1, 1)
yangi_narx = model.predict(yangi_data_point)
print(yangi_narx)

"""## Vizualizatsiya"""

import matplotlib.pyplot as plt


y_predicted = model.predict(X)

plt.scatter(X, y, color='blue', label="Data points")
plt.xlabel("Xonalar soni")
plt.ylabel("Narxi")

plt.plot(X, y_predicted, color='red', label="Regression Chiziq")
plt.show()

