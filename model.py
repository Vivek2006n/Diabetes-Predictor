import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import os
import pickle

class DiabetesModel:
    def __init__(self):
        self.model_path = 'diabetes_model.pkl'
        self.scaler_path = 'scaler.pkl'
        
        # Check if model exists, otherwise train a new one
        if os.path.exists(self.model_path) and os.path.exists(self.scaler_path):
            self.model = pickle.load(open(self.model_path, 'rb'))
            self.scaler = pickle.load(open(self.scaler_path, 'rb'))
        else:
            self.train_model()
    
    def train_model(self):
        # Load the Pima Indians Diabetes Dataset
        # This is a placeholder. In a real application, you would load your dataset
        # For demonstration, we'll create a simple synthetic dataset
        
        # Features: Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigree, Age
        X = np.array([
            [6, 148, 72, 35, 0, 33.6, 0.627, 50],
            [1, 85, 66, 29, 0, 26.6, 0.351, 31],
            [8, 183, 64, 0, 0, 23.3, 0.672, 32],
            [1, 89, 66, 23, 94, 28.1, 0.167, 21],
            [0, 137, 40, 35, 168, 43.1, 2.288, 33],
            [5, 116, 74, 0, 0, 25.6, 0.201, 30],
            [3, 78, 50, 32, 88, 31.0, 0.248, 26],
            [10, 115, 0, 0, 0, 35.3, 0.134, 29],
            [2, 197, 70, 45, 543, 30.5, 0.158, 53],
            [8, 125, 96, 0, 0, 0.0, 0.232, 54],
            # Add more sample data as needed
        ])
        
        # Target: 0 = No Diabetes, 1 = Diabetes
        y = np.array([1, 0, 1, 0, 1, 0, 1, 0, 1, 1])
        
        # Normalize the data
        self.scaler = StandardScaler()
        X_scaled = self.scaler.fit_transform(X)
        
        # Train a Random Forest model
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)
        self.model.fit(X_scaled, y)
        
        # Save the model and scaler
        pickle.dump(self.model, open(self.model_path, 'wb'))
        pickle.dump(self.scaler, open(self.scaler_path, 'wb'))
    
    def predict(self, input_data):
        # Scale the input data
        input_scaled = self.scaler.transform(input_data)
        
        # Make prediction
        prediction = self.model.predict(input_scaled)
        
        return prediction