import streamlit as st

st.title("คำนวณค่า BMI")
st.write("โปรแกรมคำนวณดัชนีมวลกาย")

weight = st.number_input(
    "น้ำหนัก (กิโลกรัม)",
    min_value=1.0,
    max_value=300.0,
    value=60.0
)

height = st.number_input(
    "ส่วนสูง (เซนติเมตร)",
    min_value=50.0,
    max_value=250.0,
    value=170.0
)

if st.button("คำนวณ BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.success(f"ค่า BMI ของคุณคือ {bmi:.2f}")

    if bmi < 18.5:
        st.info("อยู่ในเกณฑ์น้ำหนักน้อย")
    elif bmi < 23:
        st.success("อยู่ในเกณฑ์ปกติ")
    elif bmi < 25:
        st.warning("อยู่ในเกณฑ์น้ำหนักเกิน")
    elif bmi < 30:
        st.warning("อยู่ในเกณฑ์อ้วนระดับ 1")
    else:
        st.error("อยู่ในเกณฑ์อ้วนระดับ 2")
