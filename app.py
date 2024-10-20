from flask import Flask, request, jsonify, render_template
import tensorflow as tf
import numpy as np
import pandas as pd
import pickle

app = Flask(__name__)

# Load the trained model
model = tf.keras.models.load_model('house_price_model.h5')

# Load the fitted preprocessor
with open('preprocessor.pkl', 'rb') as f:
    preprocessor = pickle.load(f)

# Home route to render the HTML form
@app.route('/')
def home():
    return render_template('index.html')  # This HTML form will allow users to input house details.

# Prediction route to handle form submissions or JSON input
@app.route('/predict', methods=['POST'])
def predict():
    try:
        if request.is_json:
            data = request.get_json()  # Expecting JSON data
        else:
            data = request.form.to_dict()  # Get data from form

        # Define numeric and categorical features
        numeric_features = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 
                            'total_bedrooms', 'population', 'households', 'median_income']

        # Convert input to a DataFrame (ensure numeric fields are converted to floats)
        input_data = pd.DataFrame([data])

        # Handle numeric conversions, and ensure no missing values
        for feature in numeric_features:
            if feature in input_data:
                input_data[feature] = input_data[feature].astype(float)
            else:
                return jsonify({'error': f'Missing value for {feature}'}), 400

        # Preprocess the data using the loaded preprocessor
        input_data_processed = preprocessor.transform(input_data)

        # Make prediction using the preprocessed data
        predicted_price = model.predict(input_data_processed)

        # Convert the prediction to a native Python float for JSON serialization
        predicted_price = float(predicted_price[0][0])

        # Return the predicted price in the HTML template
        return render_template('index.html', predicted_price=predicted_price)

    except ValueError as e:
        return jsonify({'error': f'ValueError: {str(e)}'}), 400
    except Exception as e:
        return jsonify({'error': f'An error occurred: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
