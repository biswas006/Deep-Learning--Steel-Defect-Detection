# Diabetes-Prediction-ML-App

This is a web application built in Python using Streamlit that predicts whether a person has diabetes or not based on their medical attributes. It utilizes the Diabetes dataset obtained from Kaggle.

The web app allows users to input various medical attributes such as the number of pregnancies, plasma glucose concentration, blood pressure, skin thickness, insulin level, BMI, diabetes pedigree function, and age. Based on these inputs, the machine learning model predicts whether the person is likely to have diabetes or not.

## Dataset
The dataset used for training the model is the "Diabetes Dataset" available on Kaggle. You can find the dataset [here](https://www.kaggle.com/datasets/mathchi/diabetes-data-set). It consists of several features related to diabetes, such as pregnancies, glucose concentration, blood pressure, skin thickness, insulin level, BMI, diabetes pedigree function, and age. The dataset also includes an "Outcome" column indicating whether the person has diabetes (1) or not (0).

## Model
This app is built on SVM classifier- the best performing among all considered models for the given dataset. The prediction accuracy was clocked at 78% on the test data.

## Medical Feature Significance 
Significance of features highlighted by the model (in decreasing order)
![Significance of  features in the model (in decreasing order)](https://github.com/biswas006/Diabetes-Prediction-ML-App/assets/54642211/c79c597e-6ffa-4947-8b1f-b589dfaacad8)

## Usage
Once you access the web app in your web browser, you will see a sidebar with input sliders for various medical attributes. Adjust the sliders to input the corresponding values for each attribute.

After providing the input values, the app will use a machine learning model (SVM Classifier) trained on the dataset to make a prediction. It will display whether the person is likely to have diabetes or not based on the input attributes. 

### Screenshot of the Web App
![Web App Screenshot](https://github.com/biswas006/Diabetes-Prediction-ML-App/assets/54642211/663068aa-2c0b-4516-98c3-02a2778a9a1c)

## Contributing
Contributions to this project are welcome. If you find any issues or want to add new features, feel free to open an issue or submit a pull request.

## Acknowledgments
- The Diabetes dataset used in this project is obtained from Kaggle and was contributed by Mathchi. You can find the dataset [here](https://www.kaggle.com/datasets/mathchi/diabetes-data-set).
- This web app is built using the Streamlit library for Python. Streamlit provides a simple and efficient way to create interactive web applications with machine learning capabilities.

## Contact
If you have any questions or suggestions regarding this project, please feel free to reach out to me.

- Email: biswas.tech21@gmail.com



