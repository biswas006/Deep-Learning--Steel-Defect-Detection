
"""
@Author Biswas Kumar
"""

import numpy as np
import pickle
import streamlit as st
loaded_model = pickle.load(open('trained_model.sav', 'rb'))

# creating a function for prediction
def diabetes_prediction(input_data):
    

    # changing the input_data to numpy array
    input_data_as_numpy_array = np.asarray(input_data)

    # reshape the array as we are predicting for one instance
    input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshaped)
    print(prediction)

    if (prediction[0] == 0):
      return 'The person is not likely to have diabetes.'
    else:
      return 'The person is likely to have diabetes.'
  
def main():
    
    
    # Title
    st.title('Diabetes Prediction Web App')
    st.subheader("- Predict if a person has diabetes using Machine learning")
  
    #Input data from users through Sliders!
    # Add user input fields for the features
    
    Pregnancies = st.slider("Number of Pregnancies", 0, 17, 1)
    Glucose = st.slider("Plasma Glucose Concentration", 0, 200, 100)
    BloodPressure = st.slider("Blood Pressure (mm Hg)", 0, 122, 70)
    SkinThickness = st.slider("Skin Thickness (mm)", 0, 99, 20)
    Insulin = st.slider("Insulin Level (mu U/ml)", 0, 846, 79)
    BMI = st.slider("BMI", 0.0, 67.1, 30.0)
    DiabetesPedigreeFunction = st.slider("Diabetes Pedigree Function", 0.078, 2.42, 0.3725)
    Age = st.slider("Age (years)", 21, 81, 30)

    
    #code for prediction 
    diagnosis = ''
    
    #creating a button for prediction
    if st.button('Diabetes Test Result'):
        diagnosis = diabetes_prediction([str(Pregnancies),str(Glucose),str(BloodPressure),str(SkinThickness),str(Insulin),str(BMI),str(DiabetesPedigreeFunction),str(Age)])
    
    st.success(diagnosis)
    
if __name__=='__main__':
    main()
