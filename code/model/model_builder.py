# model_builder.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

def build_and_train_model(data_path):
    # Load the dataset
    df = pd.read_csv(data_path)

    # Assume the target variable is 'target' and features are all other columns
    X = df.drop('target', axis=1)
    y = df['target']

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize the linear regression model
    model = LinearRegression()

    # Train the model
    model.fit(X_train, y_train)

    # Make predictions on the test set
    y_pred = model.predict(X_test)

    # Evaluate the model performance
    mse = mean_squared_error(y_test, y_pred)
    print(f'Mean Squared Error on Test Set: {mse}')

    # Save the trained model
    joblib.dump(model, 'linear_regression_model.joblib')
    print('Model saved successfully.')

if __name__ == "__main__":
    # Provide the path to your dataset
    data_path = 'path/to/your/dataset.csv'

    # Build and train the model
    build_and_train_model(data_path)
