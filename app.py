# import numpy as np
import numpy as np
import pickle
from flask import Flask, render_template, request

# Create a Flask app
app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def home():
    return render_template('index.html')
# Define the endpoint for the prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the request
    data = request.form.values()
    int_features=[float(x) for x in data]
    features=[np.array(int_features)]

    #Extract the input features from the data
    # latitude = float(data['latitude'])
    # longitude = float(data['longitude'])
    # features=np.array(latitude,longitude)
    # # date = float(data['date'])
    # # time = float(data['time'])


    # Make a prediction using the machine learning model
    prediction = model.predict_proba(features)
    for i, prob in enumerate(prediction):
        print(f'New area {i + 1}: {prob[1] * 100:.2f}% probability of being crime prone')
        output= prob[1] * 100


#     # Format the prediction as a JSON response
#     response = {
#         'crime_rate': float(prediction[0])
#     }

    return render_template('index.html',prediction_text='Probability of this area is crime or not is {}'.format(output))


if __name__ == '__main__':
    app.run(debug=True)
