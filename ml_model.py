import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from .. import db
from ..models import Company

def train_model():
    companies = Company.query.all()
    data = [(c.name, c.category, c.subcategory) for c in companies]
    df = pd.DataFrame(data, columns=['name', 'category', 'subcategory'])

    X = df[['name']]
    y = df['category']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    # Save the model
    import joblib
    joblib.dump(model, 'app/utils/model.pkl')

def predict():
    model = joblib.load('app/utils/model.pkl')
    # Example prediction
    predictions = model.predict([['Example Company']])
    return predictions