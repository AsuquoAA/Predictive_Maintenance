# 🔧 Predictive Maintenance for Hydraulic Systems

## 📌 Project Overview
This project is a **Predictive Maintenance Model** for a **hydraulic system**, built using **machine learning** (XGBoost model to be precise) to assess the health of key equipment (Cooler, Pump, and Accumulator). The model uses the values of sensors from a hydraulic test rig to predict if the equipment is **Healthy** or **Needs Maintenance** at any second during the cycle, helping to prevent unexpected failures and optimize maintenance schedules.

## 🚀 Features
- **Database Creation**: Create a database and schema to query the data efficiently for modelling
- **Machine Learning Model**: Trained using the **UCI Hydraulic Test Dataset**.
- **PCA for Dimensionality Reduction**: Used to optimize input data for the model.
- **Streamlit Web App**: A user-friendly interface for real-time predictions.
- **Interactive Visualizations**: Displays maintenance status with a color-coded bar chart.
- **Dynamic System Status**: Provides alerts based on the number of components needing maintenance.
- **Scalable Deployment**: Model can be easily updated and retrained with new data.

---

## Installations
To run this model, you need the following:
1. numpy
2. pandas
3. matplotlib
4. seaborn
5. scikit-learn
6. streamlit
7. joblib

### 1️⃣ **Setup the Environment**
```sh
pip install -r requirements.txt

```
## How to run this project
Clone the Repository:
code: git clone https://github.com/AsuquoAA/Predictive_Maintenance.git
Navigating to directory
code: cd Predictive_Maintenance

---

## 🖥️ How to Use
### 2️⃣ **Run the Streamlit App**
```sh
streamlit run app.py
```

### 3️⃣ **Make Predictions**
- Enter sensor readings in the **sidebar**.
- Click **Predict Condition**.
- View **Predicted Status & Visualizations**.

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

---

## Summary of Workflow

### Database for UCI Hydraulic Test Dataset
As part of this predictive maintenance project, I designed and implemented a database to efficiently store and manage the UCI Hydraulic Test Dataset. The database allows structured querying and retrieval of sensor data, making it easier to analyze trends, monitor equipment performance, and integrate with machine learning models.

#### Database Structure
The database consists of the following key components:
- Sensors Table: Stores the 17 sensor readings for each test sample.
- Equipment Health Table: Contains labels indicating whether the equipment is faulty or healthy.


### Feature Engineering

The dataset was processed to create relevant **features**, such as:
- **Cooler Condition Features**
- **Pump Leakage Features**
- **Accumulator Condition Features**
- **Statistical Summaries of Features**


### 🏗️ Model Development
#### 1️⃣ **Data Preprocessing**
- Feature engineering and statistical summaries
- Handling redundant features
- Applying **Principal Component Analysis (PCA)** for dimensionality reduction
- Data scaling using **StandardScaler**

#### 2️⃣ **Model Training**
- **Algorithm Used**: XGBoost Classifier
- **Classification type**: Multiclass, Multilabel Classification
- **Target Labels**: Each sample may have multiple fault conditions simultaneously, requiring a multilabel classification approach.
  - `0` → **Healthy**
  - `1` → **Needs Maintenance**
  - Multiple labels can be assigned per sample, indicating multiple fault types.
- **Evaluation Metrics**:
  - Macro F1-score
  - Confusion Matrix
  - Classification Report

#### 3️⃣ **Model Deployment**
- Model and preprocessing tools (`scaler.pkl`, `pca.pkl`, `xgboost_model.pkl`) are saved using **Joblib**.
- **Streamlit App** allows real-time predictions based on user input sensor values.


## 🛠️ Technologies Used
- **Python** (Pandas, NumPy, Scikit-Learn, XGBoost)
- PgAdmin
- PostgreSQL
- **Joblib** (Model Persistence)
- **Matplotlib** (Visualizations)
- **Streamlit** (Web Deployment)  

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
New data was synthetically generated for testing with filename 'synthetic_df', the dataset contains 17 columns and 60 rows represneting the reading from the 17 sensors for a period of 60 seconds
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
![Output1](https://github.com/AsuquoAA/Predictive_Maintenance/blob/main/Screenshot%202025-03-07%20at%2014.13.48.png)

-

**Sample after clicking the 'Predict condition' button**
![Output2](https://github.com/AsuquoAA/Predictive_Maintenance/blob/main/Screenshot%202025-03-07%20at%2014.14.10.png)

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

