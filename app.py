import streamlit as st
import pickle
import numpy as np  # Import numpy

# Load the model
model_file = 'WEATHER ML/weather_model.sav'
try:
    with open(model_file, 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'weather_model.sav' is in the correct directory.")
    st.stop()

# Streamlit app
st.title('Weather Prediction App')

# Input features
st.header('Enter Weather Features')
precipitation = st.number_input('Precipitation (in mm)', min_value=0.0, step=0.1, value=0.0)
temp_max = st.number_input('Max Temperature (°C)', step=0.1, value=25.0)
temp_min = st.number_input('Min Temperature (°C)', step=0.1, value=15.0)
wind = st.number_input('Wind Speed (km/h)', step=0.1, value=5.0)

# Predict button
if st.button('Predict'):
    try:
        # Prepare input data
        input_data = np.array([[precipitation, temp_max, temp_min, wind]])
        
        # Make prediction
        prediction = model.predict(input_data)
        
        # Display prediction
        st.success(f"Predicted Weather Category: {prediction[0]}")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
