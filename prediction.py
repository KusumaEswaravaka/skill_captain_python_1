import numpy as np
from statistics import mode
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Placeholder for data_dict - replace this with the actual definition or import
data_dict = {
    "symptom_index": {
        "Itching": 0,
        "Skin Rash" : 1,
        "Nodal Skin Eruptions" : 2
    },  # Replace with your symptom_index
    "predictions_classes": []  # Replace with your predictions_classes
}

# Placeholder for your feature matrix (X) and target variable (y) - replace with actual data
X = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])  # Example feature matrix
y = np.array([0, 1, 0])  # Example target variable

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Placeholder for models - replace these with your actual machine learning models
final_rf_model = RandomForestClassifier()
final_nb_model = GaussianNB()
final_svm_model = SVC()

# Train your models
final_rf_model.fit(X_train, y_train)
final_nb_model.fit(X_train, y_train)
final_svm_model.fit(X_train, y_train)

def predictDisease(symptoms):
    symptoms = symptoms.split(",")

    # creating input data for the models
    input_data = [0] * len(data_dict["symptom_index"])
    
    for symptom in symptoms:
        if symptom in data_dict["symptom_index"]:
            index = data_dict["symptom_index"][symptom]
            input_data[index] = 1
        else:
            print(f"Warning: Symptom '{symptom}' not found in the dictionary.")

    # reshaping the input data and converting it
    # into a suitable format for model predictions
    input_data = np.array(input_data).reshape(1, -1)

    # generating individual outputs
    rf_prediction = final_rf_model.predict(input_data)[0]
    nb_prediction = final_nb_model.predict(input_data)[0]
    svm_prediction = final_svm_model.predict(input_data)[0]

    # making the final prediction by taking the mode of all predictions
    final_prediction = mode([rf_prediction, nb_prediction, svm_prediction])
    predictions = {
        "rf_model_prediction": rf_prediction,
        "naive_bayes_prediction": nb_prediction,
        "svm_model_prediction": svm_prediction,
        "final_prediction": final_prediction
    }
    return predictions

# Testing the function
print(predictDisease("Itching,Skin Rash,Nodal Skin Eruptions"))
