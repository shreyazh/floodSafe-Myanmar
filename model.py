import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_model():
    # Loading historical data
    historical_data = pd.read_csv(" https://data.humdata.org/dataset/46c703fe-7ba1-484b-a38c-8c53f0cf00c4/resource/796986b9-038f-416c-ad9c-9c0317d72b91/download/myanmar-admin1-flood.csv")
    # we are taking the datset in .csv from https://data.humdata.org/
    X = historical_data[['rainfall', 'soil_humidity', 'temperature', 'water_level']]
    y = historical_data['flood_risk']  # Binary target: 1 for high flood risk, 0 for low

    
    # Train-test split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    # values can differ, we've choosen this
    

    # Initializing and training of our model
    model = RandomForestClassifier()
    model.fit(X_train, y_train)


    # Saving accuracy for reference
    accuracy = accuracy_score(y_test, model.predict(X_test))
    print(f"Model accuracy: {accuracy * 100:.2f}%")


    # Saving the trained model
    joblib.dump(model, "flood_prediction_model.pkl")
    return model


# Prediction system
def load_model():
    return joblib.load("flood_prediction_model.pkl")
