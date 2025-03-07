# 🔧 Predictive Maintenance for Hydraulic Systems

## 📌 Project Overview
This project is a **Predictive Maintenance Model** for a **hydraulic system**, built using **machine learning** to assess the health of key equipment (Cooler, Pump, and Accumulator). The model predicts whether the equipment is **Healthy** or **Needs Maintenance**, helping to prevent unexpected failures and optimize maintenance scheduling.

## 🚀 Features
- **Machine Learning Model**: Trained using the **UCI Hydraulic Test Dataset**.
- **PCA for Dimensionality Reduction**: Used to optimize input data for the model.
- **Streamlit Web App**: A user-friendly interface for real-time predictions.
- **Interactive Visualizations**: Displays maintenance status with a color-coded bar chart.
- **Dynamic System Status**: Provides alerts based on the number of components needing maintenance.
- **Scalable Deployment**: Model can be easily updated and retrained with new data.

---

## 📊 Dataset
The model was trained on the **UCI Hydraulic Test Dataset**, which contains sensor readings from a hydraulic system, including:
- **Pressure sensors** (P1-P6)
- **Temperature sensors** (T1-T4)
- **Flow sensors** (F1-F2)
- **Stable_Efficiency**
- **Cooling_Efficiency**
- **Cooling_Power**
- **Efficiency Power Signals**
- **Vibration sensors**
The dataset can be accessed <a href="https://archive.ics.uci.edu/dataset/447/condition+monitoring+of+hydraulic+systems">here</a>

The dataset was processed to create relevant **features**, such as:
- **Cooler Condition Features**
- **Pump Leakage Features**
- **Accumulator Condition Features**
- **Statistical Summaries of Features**

---

## 🛠️ Technologies Used
- **Python** (Pandas, NumPy, Scikit-Learn, XGBoost)
- **Joblib** (Model Persistence)
- **Matplotlib** (Visualizations)
- **Streamlit** (Web Deployment)

---

## 🏗️ Model Development
### 1️⃣ **Data Preprocessing**
- Feature engineering and statistical summaries
- Handling redundant features
- Applying **Principal Component Analysis (PCA)** for dimensionality reduction
- Data scaling using **StandardScaler**

### 2️⃣ **Model Training**
- **Algorithm Used**: XGBoost Classifier
- **Target Labels**:
  - `0` → **Healthy**
  - `1` → **Needs Maintenance**
- **Evaluation Metrics**:
  - Accuracy, Precision, Recall, and F1-score
  - Confusion Matrix for classification performance

### 3️⃣ **Model Deployment**
- Model and preprocessing tools (`scaler.pkl`, `pca.pkl`, `xgboost_model.pkl`) are saved using **Joblib**.
- **Streamlit App** allows real-time predictions based on user input sensor values.

---

## 🖥️ How to Use
### 1️⃣ **Setup the Environment**
```sh
pip install -r requirements.txt
```

### 2️⃣ **Run the Streamlit App**
```sh
streamlit run app.py
```

### 3️⃣ **Make Predictions**
- Enter sensor readings in the **sidebar**.
- Click **Predict Condition**.
- View **Predicted Status & Visualizations**.

---

## 📌 Key Components of the Web App
### **Input Fields**
- Sidebar form to input **sensor readings**.
- Fields automatically convert values into a **Pandas DataFrame**.

### **Model Prediction**
- Input data is **transformed using Scaler & PCA**.
- XGBoost model predicts the **maintenance status**.

### **System Health Indicators**
- **Bar Chart**: Shows equipment status (**Green = Healthy, Red = Needs Maintenance**).
- **Alerts**: System-wide maintenance warnings based on the number of faulty components.

---

## 🔄 Testing with New Data
To test the model with **new sensor readings**:
1. Manually enter new readings in the Streamlit interface.
2. Click **Predict Condition** to view results.
3. The model will process the input and display:
   - **Predicted Status**
   - **System Health Indicator**
   - **Maintenance Alerts**

---

## Sample Output
**Sample before clicking the 'Predict condition' button**
![Output1]()

**Sample after clicking the 'Predict condition' button**
![Output2]()

---

## ⚡ Future Improvements
🔹 **Expand Dataset**: Incorporate real-world industrial data.  
🔹 **Time Series Analysis**: Predict failures in advance.  
🔹 **Deploy on Cloud**: Host the model for wider accessibility.  

---

## 🤝 Contributors
👨‍💻 **[Anthony Asuquo]** – Machine Learning & Deployment  

---

## Appreciation
This project utilizes the UCI Hydraulic Test Dataset from the UCI Machine Learning Repository. Special thanks to the UCI ML team and contributors for making this dataset publicly available for research and development.

---

## 📜 License
This project is for educational and research purposes. The dataset used in this project is provided by the UCI Machine Learning Repository and follows its respective licensing terms.

---

### 🚀 **Built for Reliability, Efficiency, and Industrial AI Applications!**

