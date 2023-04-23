import numpy as np
import pickle
from flask import Flask,request, render_template

const form = document.querySelector('#prediction-form');

# Create a Flask app
app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

# Define the endpoint for the prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.get_json()

    # Extract the input features from the data
    latitude = float(data['latitude'])
    longitude = float(data['longitude'])
    property_crime = float(data['property_crime'])
    burglary = float(data['burglary'])
    larceny_theft = float(data['larceny_theft'])

    # Make a prediction using the machine learning model
    prediction = model.predict([[latitude, longitude, property_crime, burglary, larceny_theft]])

    # Format the prediction as a JSON response
    response = {
        'crime_rate': float(prediction[0])
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)e
