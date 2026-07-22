# app.py

import streamlit as st
import numpy as np
import joblib

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Hospital Readmission Prediction",
    page_icon="🏥",
    layout="wide"
)

# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------

model = joblib.load("model.pkl")
scaler = joblib.load("scaler.pkl")

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.main {
    background: linear-gradient(to right, #141E30, #243B55);
}

.title {
    text-align: center;
    color: #00E5FF;
    font-size: 55px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: white;
    font-size: 22px;
    margin-bottom: 30px;
}

.box {
    background-color: rgba(255,255,255,0.08);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 0px 15px rgba(0,0,0,0.4);
}

.stSelectbox label {
    color: white !important;
    font-size: 18px !important;
    font-weight: bold !important;
}

.stButton>button {
    width: 100%;
    height: 60px;
    background: linear-gradient(to right, #00c6ff, #0072ff);
    color: white;
    font-size: 24px;
    font-weight: bold;
    border-radius: 15px;
    border: none;
}

.stButton>button:hover {
    background: linear-gradient(to right, #fc466b, #3f5efb);
    color: white;
}

.result1 {
    background-color: #00C853;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    color: white;
    font-size: 30px;
    font-weight: bold;
}

.result2 {
    background-color: #FF1744;
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    color: white;
    font-size: 30px;
    font-weight: bold;
}

.footer {
    text-align: center;
    color: white;
    margin-top: 40px;
    font-size: 18px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    "<div class='title'>🏥 Hospital Readmission Prediction</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Predict Whether a Patient Will Be Readmitted Within 30 Days</div>",
    unsafe_allow_html=True
)

# ---------------------------------------------------
# FORM SECTION
# ---------------------------------------------------

st.markdown("<div class='box'>", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

# ---------------------------------------------------
# COLUMN 1
# ---------------------------------------------------

with col1:

    age = st.selectbox(
        "👤 Select Patient Age",
        [i for i in range(1, 101)]
    )

    length_of_stay_days = st.selectbox(
        "🏥 Length Of Stay In Hospital",
        [i for i in range(1, 31)]
    )

    num_diagnoses = st.selectbox(
        "🩺 Number Of Diagnoses",
        [i for i in range(1, 16)]
    )

# ---------------------------------------------------
# COLUMN 2
# ---------------------------------------------------

with col2:

    num_medications = st.selectbox(
        "💊 Number Of Medications",
        [i for i in range(1, 51)]
    )

    prev_admissions = st.selectbox(
        "📋 Previous Admissions",
        [i for i in range(0, 21)]
    )

    glucose_level = st.selectbox(
        "🧪 Glucose Level",
        [i for i in range(50, 301)]
    )

# ---------------------------------------------------
# COLUMN 3
# ---------------------------------------------------

with col3:

    bmi = st.selectbox(
        "⚖️ Body Mass Index (BMI)",
        [i for i in range(10, 51)]
    )

    has_diabetes = st.selectbox(
        "🩸 Does Patient Have Diabetes?",
        ["No", "Yes"]
    )

    discharge_type = st.selectbox(
        "📄 Discharge Type",
        [0, 1, 2]
    )

st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# CONVERT VALUES
# ---------------------------------------------------

diabetes = 1 if has_diabetes == "Yes" else 0

# ---------------------------------------------------
# PREDICT BUTTON
# ---------------------------------------------------

st.markdown("<br>", unsafe_allow_html=True)

predict = st.button("🔍 Predict Patient Readmission")

# ---------------------------------------------------
# PREDICTION SECTION
# ---------------------------------------------------

if predict:

    input_data = np.array([[
        age,
        length_of_stay_days,
        num_diagnoses,
        num_medications,
        prev_admissions,
        glucose_level,
        bmi,
        diabetes,
        discharge_type
    ]])

    scaled_data = scaler.transform(input_data)

    prediction = model.predict(scaled_data)[0]

    probability = model.predict_proba(scaled_data)[0][1]

    st.markdown("<br>", unsafe_allow_html=True)

    if prediction == 1:

        st.markdown(
            f"""
            <div class='result2'>
            ⚠️ HIGH CHANCE OF PATIENT READMISSION<br><br>
            Prediction Probability : {probability:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class='result1'>
            ✅ LOW CHANCE OF PATIENT READMISSION<br><br>
            Prediction Probability : {probability:.2f}
            </div>
            """,
            unsafe_allow_html=True
        )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown(
    """
    <div class='footer'>
    🚀 Developed Using Streamlit | Machine Learning | Random Forest
    </div>
    """,
    unsafe_allow_html=True
)