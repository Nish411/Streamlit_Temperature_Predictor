import streamlit as st

st.title("Infrared Thermography")
st.caption("Oral Temperature Prediction")

st.markdown("**Temperature readings from Thermal Image in Degrees Celsius**")

T_RC1 = st.number_input("Enter T_RC1:", value=34.0, step=0.1, min_value=30.0, max_value=45.0)

if st.button("Predict Oral Temperature"):
    predicted = round(0.9856 * T_RC1 + 4.1231, 10)
    st.success(f"Predicted Oral Temperature in fast mode is: {predicted} Degree Celsius")
