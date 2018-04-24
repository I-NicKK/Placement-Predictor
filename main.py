import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('/home/nick/Desktop/PlacementPredictionSystem/student-mat.csv')
df = df.drop('name', 1)
le = LabelEncoder()

for column in df[["favouriteLanguage", "workingField"]].columns:
        df[column] = le.fit_transform(df[column].values)

y = df.placed.values
X = df.drop('placed', axis = 1).values


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=21, stratify=y)

knn = KNeighborsClassifier(n_neighbors=8)

knn.fit(X_train, y_train)

#print(knn.score(X_test, y_test))

z = [[8.6,  7.7,  7.5 ,  7.5,  7.5,  6.8,  7.3 ,  6.0 ,  3 , 8 , 1 ]]


print(knn.predict(z))
