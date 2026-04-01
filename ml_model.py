import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('data.csv')

le_interest = LabelEncoder()
le_crowd = LabelEncoder()
le_season = LabelEncoder()
le_city = LabelEncoder()

data['interest'] = le_interest.fit_transform(data['interest'])
data['crowd'] = le_crowd.fit_transform(data['crowd'])
data['season'] = le_season.fit_transform(data['season'])
data['city'] = le_city.fit_transform(data['city'])

X = data[['budget', 'interest', 'crowd', 'season']]
y = data['city']

model = DecisionTreeClassifier()
model.fit(X, y)

def predict_ml(data_input):
    df = pd.DataFrame([data_input])

    df['interest'] = le_interest.transform([df['interest'][0]])
    df['crowd'] = le_crowd.transform([df['crowd'][0]])
    df['season'] = le_season.transform([df['season'][0]])

    pred = model.predict(df)[0]
    
    return le_city.inverse_transform([pred])[0]
   