import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl", "rb"))

st.title("🚢 Titanic Survival Prediction")

# User Inputs
pclass = st.selectbox("Passenger Class", [1, 2, 3])
sex = st.selectbox("Sex", ["Male", "Female"])
age = st.slider("Age", 1, 80, 25)
sibsp = st.number_input("Siblings/Spouses aboard", 0, 5, 0)
parch = st.number_input("Parents/Children aboard", 0, 5, 0)
fare = st.number_input("Fare", 0.0, 500.0, 50.0)
embarked = st.selectbox("Embarked", ["C", "Q", "S"])

# Encoding (same as training)
sex = 1 if sex == "Male" else 0
embarked_dict = {"C": 0, "Q": 1, "S": 2}
embarked = embarked_dict[embarked]

# Prediction
if st.button("Predict"):
    input_data = np.array([[pclass, sex, age, sibsp, parch, fare, embarked]])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Passenger Survived ✅")
    else:
        st.error("Passenger Did Not Survive ❌")