import streamlit as st
import numpy as np
import pandas as pd
import joblib  # To load the saved model
import matplotlib.pyplot as plt
from functions import (summary_stat_of_features,split_and_rename_X_summary,
                        removing_redundant_features_columns,create_accumulator_condition_features,
                        create_cooler_conditions_features,create_pump_leakage_features,
                        convert_numpy_to_pandas)


# Load the trained model
@st.cache_data
def load_model():
    model = joblib.load("xgboost_model.pkl")  # Update with your saved model path
    pca = joblib.load("pca.pkl")
    scaler = joblib.load("scaler.pkl")
    return model,pca,scaler

model,pca,scaler = load_model()


# Title of the app and a little intoduction
st.title("🔧 Predictive Maintenance Model")
st.write("This app predicts the condition of a hydraulic test rig system.")
# Sidebar instructions
st.markdown(
    """
    <div style="
        padding: 0px; 
        color: red; 
        border-radius: 0px; 
        font-size: 20px; 
        font-weight: bold;
        text-align: left;">
        Click the <strong>arrow</strong> on the top-left to open the sidebar! Enter sensor readings there. After inputting sensors,
        proceed to clicking the predict condition button to predict condition of test rig
    </div>
    """,
    unsafe_allow_html=True
)

 


# Define user input fields (input field is a sidebar)
st.sidebar.header("Enter Sensor Readings")
st.sidebar.write("🔹 Fill in the sensor readings below:")
# Input fields (based on features)
Pressure_1 = st.sidebar.number_input("Pressure_1 Reading",value=0.00, format="%.2f")
Pressure_2 = st.sidebar.number_input("Pressure_2 Reading",value=0.00, format="%.2f")
Pressure_3 = st.sidebar.number_input("Pressure_3 Reading",value=0.00, format="%.2f")
Pressure_4 = st.sidebar.number_input("Pressure_4 Reading",value=0.00, format="%.2f")
Pressure_5 = st.sidebar.number_input("Pressure_5 Reading",value=0.00, format="%.2f")
Pressure_6 = st.sidebar.number_input("Pressure_6 Reading",value=0.00, format="%.2f")
Temperature_1 = st.sidebar.number_input("Temperature_1 Reading",value=0.00, format="%.2f")
Temperature_2 = st.sidebar.number_input("Temperature_2 Reading",value=0.00, format="%.2f")
Temperature_3 = st.sidebar.number_input("Temperature_3 Reading",value=0.00, format="%.2f")
Temperature_4 = st.sidebar.number_input("Temperature_4 Reading",value=0.00, format="%.2f")
Flow_sensor_1 = st.sidebar.number_input("Flow_sensor_1 Reading",value=0.00, format="%.2f")
Flow_sensor_2 = st.sidebar.number_input("Flow_sensor_2 Reading",value=0.00, format="%.2f")
Stable_efficiency = st.sidebar.number_input("Stable_efficiency Reading",value=0.00, format="%.2f")
Cooling_efficiency = st.sidebar.number_input("Cooling_efficiency Reading",value=0.00, format="%.2f")
Cooling_power = st.sidebar.number_input("Cooling_power Reading",value=0.00, format="%.2f")
Vibration_sensor = st.sidebar.number_input("Vibration_sensor Reading",value=0.00, format="%.2f")
Efficiency_power_signal = st.sidebar.number_input("Efficiency_power_signal Reading",value=0.00, format="%.2f")


# Convert inputs into a dataframe for prediction
input_data = pd.DataFrame({
    'pressure_readings_1': [Pressure_1], 
    'pressure_readings_2': [Pressure_2], 
    'pressure_readings_3': [Pressure_3], 
    'pressure_readings_4': [Pressure_4], 
    'pressure_readings_5': [Pressure_5], 
    'pressure_readings_6': [Pressure_6], 
    'temperature_readings_1': [Temperature_1], 
    'temperature_readings_2': [Temperature_2], 
    'temperature_readings_3': [Temperature_3], 
    'temperature_readings_4': [Temperature_4],
    'flow_sensor_readings_1': [Flow_sensor_1], 
    'flow_sensor_readings_2': [Flow_sensor_2], 
    'stable_efficiency_readings_1': [Stable_efficiency], 
    'cooling_efficiency_readings_1': [Cooling_efficiency], 
    'cooling_power_readings_1': [Cooling_power], 
    'vibration_sensor_readings_1': [Vibration_sensor], 
    'efficiency_power_signal_readings_1': [Efficiency_power_signal]
})

def process(input_data):
    # preprocessing to be in the right format
    input_data = summary_stat_of_features(input_data)
    input_data = split_and_rename_X_summary(input_data)
    input_data = removing_redundant_features_columns(input_data)

    # feature engineering
    create_cooler_conditions_features(input_data)
    create_pump_leakage_features(input_data)
    create_accumulator_condition_features(input_data)

    # incase some values are zero, so it doesn't fail
    if input_data.isnull().sum().sum() > 0:
        st.warning("⚠️ It seems some sensor readings are missing or some readings are zero(0), please clarify before using model prediction.")
        input_data = input_data.fillna(0)  # Replace NaN with zero (you can change this to .mean() or .median())

    # Apply PCA
    X_scaled = scaler.transform(input_data)
    input_data = pca.transform(X_scaled)  # Transform the original dataset

    # convert to pandas dataframe for easy handling
    input_data = convert_numpy_to_pandas(input_data)

    return input_data

def predict(input_data):
    prediction = model.predict(input_data)
    # Convert numerical prediction to condition labels (modify based on your dataset)

    equipment_names = ["Cooler", "Pump", "Accumulator"]
    condition_mapping = {0: "Healthy", 1: "Needs Maintenance"}
    predicted_conditions = [f"{equipment}: {condition_mapping.get(int(pred), 'Unknown Condition')}" 
                        for equipment, pred in zip(equipment_names, prediction[0])]

    return predicted_conditions    

def plot_prediction(predicted_conditions):
    plt.figure(figsize = (9,4))

    equipment_names = ["Cooler", "Pump", "Accumulator"]
    length = [1,1,1]
    stats = ["Needs Maintenance" if "Needs Maintenance" in cond else "Healthy" for cond in predicted_conditions]  

    bars = plt.bar(equipment_names, length, color=["green" if status == "Healthy" else "red" for status in stats])


    plt.yticks([])
    plt.xticks(fontsize=12, fontweight='bold')

    for spine in plt.gca().spines.values():
        spine.set_visible(False)

    for bar,status in zip(bars,stats):
        height = bar.get_height()
        plt.gca().text(bar.get_x() + bar.get_width() / 2, bar.get_height() - 0.4, str(status),
                    ha='center', color='w',fontweight='bold', fontsize=11)  

    # Display in Streamlit
    st.pyplot(plt)


if st.button('__Predict condition__'):
    # preparing data for prediction
    input_data = process(input_data)

    # predict and return results
    predicted_conditions = predict(input_data)

    # Count occurrences of "Needs Maintenance"
    num_maintenance_needed = sum("Needs Maintenance" in cond for cond in predicted_conditions)

    # Determine system status based on the count
    if num_maintenance_needed == 3:
        system_status = "⚠️ Immediate maintenance required!"
        st.error(system_status)
    elif num_maintenance_needed == 2:
        system_status = "⚙️ Schedule maintenance soon."
        st.warning(system_status)
    elif num_maintenance_needed == 1:
        system_status = "System manageable."
        st.warning(system_status)
    else:
        system_status = "✅ System is operating normally."

    
    # plot prediction visuals in streamlit
    plot_prediction(predicted_conditions)

st.write("## Inputted data shown below")
st.markdown("### <span style='font-size:14px;'>After clicking the ""Predict condition"", the inputted data would change to Principal Component Analysis (PCA) data as this was used to develop the  model</span>", unsafe_allow_html=True)
st.write(input_data)   





st.write("The model behind this predictions was developed based on the data of the sensor readings of the stable cycles from the **UCI Hydraulic Test Rig** Dataset for predictive maintenance")        