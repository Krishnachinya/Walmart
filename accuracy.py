import pandas as pd
from sklearn.metrics import r2_score,mean_squared_log_error

def best_fit(X, Y):

    xbar = sum(X)/len(X)
    ybar = sum(Y)/len(Y)
    n = len(X) # or len(Y)

    numer = sum([xi*yi for xi,yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi**2 for xi in X]) - n * xbar**2

    b = numer / denum
    a = ybar - b * xbar

    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    return a, b

# def refine_sales(data):
#     data.Weekly_Sales[data['Weekly_Sales'] > 30000] = 4
#     data.Weekly_Sales[(data['Weekly_Sales'] > 15000) & (data['Weekly_Sales'] <= 30000)] = 3
#     data.Weekly_Sales[(data['Weekly_Sales'] > 5000) & (data['Weekly_Sales'] <= 15000)] = 3
#     data.Weekly_Sales[(data['Weekly_Sales'] > 1000) & (data['Weekly_Sales'] <= 5000)] = 2
#     data.Weekly_Sales[(data['Weekly_Sales'] > 0) & (data['Weekly_Sales'] <= 1000)] = 1
#     data.Weekly_Sales[data['Weekly_Sales'] <= 0] = 0
#     return data


# trained = refine_sales(pd.read_csv('RandomForestRegressors.csv'))
# test = refine_sales(pd.read_csv('test_accuracy.csv'))

trained = pd.read_csv('RandomForestRegressors.csv')
test = pd.read_csv('test_accuracy.csv')




trained = trained['Weekly_Sales']
test = test['Weekly_Sales']

a, b = best_fit(trained, test)
# plot points and fit line
import matplotlib.pyplot as plt
plt.xlim(0, 30000)
plt.ylim(0, 30000)
plt.scatter(trained, test,color=['red'])
yfit = [a + b * xi for xi in test]
plt.plot(test, yfit)
plt.show()

print r2_score(test, trained)
print mean_squared_log_error(abs(test), abs(trained))
