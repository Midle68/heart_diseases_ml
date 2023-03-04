import streamlit as st
import pandas as pd
import pickle


def load():
    with open("./main.pcl", "rb") as model_file:
        return pickle.load(model_file)


st.title("Heart Disease Detection App")
st.markdown("**:red[Warning!]** The app shows only the _probable risk_ of having a heart disease."
            "\n**For an accurate diagnosis refer to the specialist!**")
st.markdown("Fill in the following information and press 'Result' button to see the result:")

gender = st.radio("Gender:", ('Male', 'Female'), key='gender')
age = st.slider('Age:', 0, 100, 0, key='age')
height = st.number_input('Height (in cm):', 140, 250, step=5, key='height')
weight = st.number_input("Weight (in kg):", min_value=40, max_value=300, key='weight')
ap_hi = st.number_input('High Blood Pressure:', 0, 300, key='ap_hi')
ap_lo = st.number_input('Low Blood Pressure:', 0, 200, key='ap_lo')
cholesterol = st.selectbox('Cholesterol Level:', (range(1, 4)), key='cholesterol')
gluc = st.selectbox('Glucose Level:', (range(1, 4)), key='gluc')
smoke = st.checkbox('Do you smoke?', key='smoke')
alco = st.checkbox('Do you drink alcohol?', key='alco')
active = st.checkbox('Are you an active person?', key='active')

gender = 0 if gender == 'Male' else 1
smoke = 1 if smoke else 0
alco = 1 if alco else 0
active = 1 if active else 0
bmi = weight / ((height / 100) ** 2)

model = load()

df = pd.DataFrame(
    [[age, ap_hi, ap_lo, cholesterol, gluc, bmi, gender, smoke, alco, active]],
    columns=['age', 'ap_hi', 'ap_lo', 'cholesterol', 'gluc', 'bmi', 'female', 'smoke', 'alco', 'active']
)
pred = model.predict_proba(df)[:, 1] * 100
percent = pred.round(2)

st.markdown(f"### The risk of having a heart disease: {percent[0]}%.")