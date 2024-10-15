from flask import Flask, request, render_template
import pickle
import numpy as np
import sklearn
import flask
from sklearn.preprocessing import StandardScaler

# Load the trained model (make sure you have a trained model saved as 'model.pkl')
model_path = 'model.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

# Initialize the scaler (you need to ensure the scaler used during model training is consistent)
scaler = StandardScaler()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    # Extract data from form (convert form values to appropriate data types)
    form_values = request.form

    # Convert form data to float/integer for each of the 10 features
    credit_score = float(form_values['credit_score'])
    country = int(form_values['country'])  # assuming country is encoded as an integer
    gender = int(form_values['gender'])    # assuming gender is binary (e.g., 0 for male, 1 for female)
    age = int(form_values['age'])
    tenure = int(form_values['tenure'])
    balance = float(form_values['balance'])
    products_number = int(form_values['products_number'])
    credit_card = int(form_values['credit_card'])  # assuming 0/1 for no/yes
    active_member = int(form_values['active_member'])  # assuming 0/1 for no/yes
    estimated_salary = float(form_values['estimated_salary'])

    # Combine all the features into an array
    features = np.array([[credit_score, country, gender, age, tenure, balance, products_number, credit_card, active_member, estimated_salary]])

    # Scale the features using StandardScaler
    scaled_features = scaler.fit_transform(features)

    # Make prediction
    prediction = model.predict(scaled_features)
    output = 'Churn' if prediction[0] == 1 else 'No Churn'

    return render_template('index.html', prediction_text='Customer is predicted to {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
