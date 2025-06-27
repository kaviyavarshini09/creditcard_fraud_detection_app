# 💳 Credit Card Fraud Detection using Machine Learning (XGBoost + Streamlit)

This project is a real-time credit card fraud detection system built using **XGBoost** for model training and **Streamlit** for deployment. Users can input 30 transaction features and receive instant predictions about whether the transaction is **fraudulent** or **legitimate**.

---

## 🚀 Demo

![App Screenshot](https://your-screenshot-url-if-you-upload-one)

> 🖥️ Live App (Optional): [https://your-streamlit-app-link](#)

---

## 📂 Project Structure
fraud_pro/
├── model/
│ └── xgb_model.pkl # Trained XGBoost model
├── streamlit_app.py # Streamlit UI for prediction
├── creditcard.csv # Dataset used for model training
├── fraud.ipynb # Jupyter notebook for model training
├── requirements.txt # List of dependencies
└── README.md # Project documentation (this file)

---

## 📊 Dataset

- **Source**: [Kaggle Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)
- **Records**: 284,807 transactions
- **Features**: 30 numerical features (V1–V28, Amount, Time)
- **Target**: `Class` (1 = Fraud, 0 = Legitimate)

---

## 🤖 Model

- **Algorithm**: XGBoost Classifier
- **Accuracy**: ~99% (on balanced test set)
- **Training Script**: Done in `fraud.ipynb`
- **Saved Model**: `xgb_model.pkl`

---

## 🌐 Streamlit Interface

- Users enter 30 numerical transaction features
- Press **Predict** to get fraud detection result
- Backend loads `xgb_model.pkl` and runs inference

---

## 📦 Installation

```bash
# Clone the repo
git clone https://github.com/yourusername/fraud-detection-streamlit.git
cd fraud-detection-streamlit

# Install dependencies
pip install -r requirements.txt

# Run the app
python -m streamlit run streamlit_app.py


