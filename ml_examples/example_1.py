from sklearn.ensemble import RandomForestClassifier

import pandas as pd

import numpy as np

np.random.seed(0)

# Verisetini dataframe olarak oku
df = pd.read_table('data/courteau99.dat', sep='\s+')

# Gereksiz sütunu at
df = df.drop(df.index[0])

# Spiral galaksiler kalacak şekilde filtrele
df=df[(df['Hubble'] == 'Sb') | (df['Hubble'] == 'Sa') | (df['Hubble'] == 'Sc') | (df['Hubble'] == 'SBa') | (df['Hubble'] == 'SBb') | (df['Hubble'] == 'SBc')]

# İndex numaralarını yeniden yaz
df = df.reset_index()

# Her satıra 0-1 arasında random değer ata ve 0.75 ve altına True değeri ata
df['is_train'] = np.random.uniform(0, 1, len(df)) <= .75

# True değer alanları eğitim için False değer alanları tet için ayır
train, test = df[df['is_train']==True], df[df['is_train']==False]

# Hubble sınıfı hariç tüm kolonları seç
features = df.columns[1:63]

# Hubble sınıfları yerine sayısal değer ata
y = pd.factorize(train['Hubble'])[0]

# Random forest sınıflandırıcı objesini oluştur
clf = RandomForestClassifier(n_jobs=2, n_estimators=500, random_state=0)

# Sınıflandırıcıyı eğit
clf.fit(train[features], y)

# Test verisine tahmin yap
clf.predict(test[features])

# İlk 10 tahminin olasılıklarını bul
clf.predict_proba(test[features])[0:10]

# Sayısal değerleri tekrar sınıf isimlerine dönüştür
preds = np.array(list(set(df['Hubble'])), dtype='<U10')[clf.predict(test[features])]

# İlk 5 tahmini yazdır
print(preds[0:5])

# İlk 5 gerçek değeri yazdır
print(test['Hubble'].head())

# Confision matrixi yazdır
print(pd.crosstab(test['Hubble'], preds, rownames=['Actual Species'], colnames=['Predicted Species']))

# Parametrelerin etki oranlarını yazdır
print(list(zip(train[features], clf.feature_importances_)))
