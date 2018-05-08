import pandas as pd
import numpy as np
df = pd.read_csv('train.csv')
df = df[df.Date >= '2011-11-11']
msk = np.random.rand(len(df)) <= 0.7

train = df[msk]
test = df[~msk]
train.to_csv('train_accuracy.csv',index=False)
test.to_csv('test_accuracy.csv',index=False)