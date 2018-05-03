from flask import Flask, render_template, redirect, url_for, request
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import LabelEncoder

app = Flask(__name__)
data = []

@app.route('/')
def index():
    if len(data)>12:
        del data[0:11]
    
    
    df = pd.read_csv('student-mat.csv')
    df = df.drop('name', 1)
    le = LabelEncoder()
        
    df["favouriteLanguage"] = le.fit_transform(df["favouriteLanguage"].values)
    df["workingField"] = le.fit_transform(df["workingField"].values) 
    
    if data[9].lower()=='python':
        data[9] = 12
    elif data[9].lower()=='angularjs':
        data[9] = 7
    elif data[9].lower() == 'java':
        data[9] = 8
    elif data[9].lower() == 'nodejs':
        data[9] = 10
    elif data[9].lower() == 'sql':
        data[9] = 13
    elif data[9].lower() == 'php':
        data[9] = 10
    elif data[9].lower() == 'swift':
        data[9] = 14
    elif data[9].lower() == 'kotlin':
        data[9] = 9
    elif data[9].lower() == 'html':
        data[9] = 3
    elif data[9].lower() == 'css':
        data[9] = 2
    elif data[9].lower() == 'c':
        data[9] = 0
    elif data[9].lower() == 'c++':
        data[9] = 1
    else:
        data[9] = 12
    
    
    
    
        
        
    if data[10].lower()=='web development':
        data[10] = 12
    elif data[10].lower()=='machine learning':
        data[10] = 7
    elif data[10].lower()=='android':
        data[10] = 1
    elif data[10].lower()=='ios':
        data[10] = 1
    elif data[10].lower()=='tech support':
        data[10] = 10
    elif data[10].lower()=='administrator':
        data[10] = 0
    elif data[10].lower()=='hr':
        data[10] = 4
    elif data[10].lower()=='finance':
        data[10] = 3
    elif data[10].lower()=='buisness accounting':
        data[10] = 2
    elif data[10].lower()=='networking':
        data[10] = 8
    elif data[10].lower()=='ui designer':
        data[10] = 11
    elif data[10].lower()=='hardware':
        data[10] = 5
    elif data[10].lower()=='system admin':
        data[10] = 9
    else:
        data[10] = 7
        
    
    
    
    
    for i in range(0,9):
        data[i] = float(data[i])
       
    y = df.placed.values
    X = df.drop('placed', axis = 1).values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3,random_state=21, stratify=y)
    knn = KNeighborsClassifier(n_neighbors=8)
    knn.fit(X_train, y_train)
    prediction = knn.predict([data])
    if prediction[0] == 'yes':
        result = 'Yes!!! Congratulations'
    else:
        result = 'No. You need work harder.'
    return render_template('hello.html', name = result)


@app.route('/form', methods = ['POST', 'GET'])
def form():
    
    data.append(request.form['name2'])
    data.append(request.form['name3'])
    data.append(request.form['name4'])
    data.append(request.form['name5'])
    data.append(request.form['name6'])
    data.append(request.form['name7'])
    data.append(request.form['name8'])
    data.append(request.form['name9'])
    data.append(request.form['name10'])
    data.append(request.form['name11'])
    data.append(request.form['name12'])
    
    return redirect(url_for('index'))

if __name__ == '__main__':
   app.run(debug = True)
