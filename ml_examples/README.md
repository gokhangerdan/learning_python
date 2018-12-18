# Estimating the hubble types of spiral galaxies

```python
from sklearn.ensemble import RandomForestClassifier

import pandas as pd

import numpy as np

np.random.seed(0)

df = pd.read_table('courteau99.dat', sep='\s+')

df = df.drop(df.index[0])

df=df[(df['Hubble'] == 'Sb') | (df['Hubble'] == 'Sa') | (df['Hubble'] == 'Sc') | (df['Hubble'] == 'SBa') | (df['Hubble'] == 'SBb') | (df['Hubble'] == 'SBc')]

df = df.reset_index()

df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75

train, test = df[df['is_train']==True], df[df['is_train']==False]

features = df.columns[1:63]

y = pd.factorize(train['Hubble'])[0]

clf = RandomForestClassifier(n_jobs=2, n_estimators=500, random_state=0)

clf.fit(train[features], y)

clf.predict(test[features])

clf.predict_proba(test[features])[0:10]

preds = np.array(list(set(df['Hubble'])), dtype='<U10')[clf.predict(test[features])]

print(preds[0:5])

print(test['Hubble'].head())

print(pd.crosstab(test['Hubble'], preds, rownames=['Actual Species'], colnames=['Predicted Species']))

print(list(zip(train[features], clf.feature_importances_)))
```
