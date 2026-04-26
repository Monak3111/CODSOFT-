🚢 Titanic Survival Prediction

A Machine Learning project that predicts whether a passenger survived the Titanic disaster based on various features such as age, gender, passenger class, fare, and more. The model is trained using classification algorithms and deployed as a web application using Streamlit.

---

## 📌 Project Overview

This project uses historical Titanic dataset data to build a predictive model. It demonstrates the complete ML pipeline:
---

## 📊 Dataset Information

The dataset contains the following features:

* PassengerI

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit

---

## 🧠 Machine Learning Model

* Algorithm: Random Forest Classifier
* Train-test split used for evaluation
* Model trained on cleaned and preprocessed data

---

## 🔧 Data Preprocessing Steps

* Dropped unnecessary columns:

  * PassengerId
  * Name
  * Ticket
  * Cabin

* Handled missing values:

  * Age → filled with median
  * Embarked → filled with mode

* Encoded categorical variables:

  * Sex
  * Embarked

---

## 🚀 Project Structure

titanic_project/
│── app.py              # Streamlit web app
│── model.py            # Model training script
│── model.pkl           # Saved trained model
│── titanic.csv         # Dataset
│── requirements.txt    # Dependencies

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```
git clone <your-repo-link>
cd titanic_project
```

### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```

### 3️⃣ Train the model

```
python model.py
```

### 4️⃣ Run the Streamlit app

```
streamlit run app.py
```

---

## 💻 Web App Features

* User-friendly interface
* Input passenger details
* Instant survival prediction
* Displays result clearly (Survived / Not Survived)

---

## 🎯 Output

The model predicts:

* ✅ Survived
* ❌ Not Survived

based on the input passenger data.

---

## 📈 Future Improvements

* Add model accuracy and evaluation metrics
* Use advanced models (XGBoost, Logistic Regression)
* Improve UI design
* Deploy on cloud platforms

---

## 🤝 Acknowledgment

This project is created as part of a Machine Learning internship task and is intended for learning and demonstration purposes.

---

## 📬 Contact

Feel free to connect for feedback or collaboration!
