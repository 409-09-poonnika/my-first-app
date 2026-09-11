import time
import streamlit as st

st.title("🧪 เกมทายตารางธาตุ")
st.write("ทายชื่อธาตุจากสัญลักษณ์และเลขอะตอม")

# กำหนดค่าเริ่มต้น
if "ans1_val" not in st.session_state:
    st.session_state.ans1_val = ""

if "ans2_val" not in st.session_state:
    st.session_state.ans2_val = ""

if "ans3_val" not in st.session_state:
    st.session_state.ans3_val = ""

if "ans4_val" not in st.session_state:
    st.session_state.ans4_val = ""

if "ans5_val" not in st.session_state:
    st.session_state.ans5_val = ""

# ปุ่มเริ่มเกมใหม่
if st.button("🔄 เกมใหม่"):
    st.session_state.ans1_val = ""
    st.session_state.ans2_val = ""
    st.session_state.ans3_val = ""
    st.session_state.ans4_val = ""
    st.session_state.ans5_val = ""
    st.rerun()

st.write("---")

# ข้อ 1
st.subheader("ข้อ 1")
st.write("สัญลักษณ์ **Be** เลขอะตอม **4** คือธาตุอะไร?")
ans1 = st.text_input(
    "คำตอบข้อ 1",
    value=st.session_state.ans1_val
)
st.session_state.ans1_val = ans1

# ข้อ 2
st.subheader("ข้อ 2")
st.write("สัญลักษณ์ **Ge** เลขอะตอม **32** คือธาตุอะไร?")
ans2 = st.text_input(
    "คำตอบข้อ 2",
    value=st.session_state.ans2_val
)
st.session_state.ans2_val = ans2

# ข้อ 3
st.subheader("ข้อ 3")
st.write("สัญลักษณ์ **Eu** เลขอะตอม **63** คือธาตุอะไร?")
ans3 = st.text_input(
    "คำตอบข้อ 3",
    value=st.session_state.ans3_val
)
st.session_state.ans3_val = ans3

# ข้อ 4
st.subheader("ข้อ 4")
st.write("สัญลักษณ์ **W** เลขอะตอม **74** คือธาตุอะไร?")
ans4 = st.text_input(
    "คำตอบข้อ 4",
    value=st.session_state.ans4_val
)
st.session_state.ans4_val = ans4

# ข้อ 5
st.subheader("ข้อ 5")
st.write("สัญลักษณ์ **Fm** เลขอะตอม **100** คือธาตุอะไร?")
ans5 = st.text_input(
    "คำตอบข้อ 5",
    value=st.session_state.ans5_val
)
st.session_state.ans5_val = ans5

st.write("---")

# ปุ่มตรวจคำตอบ
if st.button("✅ ตรวจคำตอบ"):

    # แปลงคำตอบให้เป็นตัวพิมพ์เล็กและตัดช่องว่าง
    u_ans1 = ans1.strip().lower()
    u_ans2 = ans2.strip().lower()
    u_ans3 = ans3.strip().lower()
    u_ans4 = ans4.strip().lower()
    u_ans5 = ans5.strip().lower()

    score = 0

    # ตรวจคำตอบ
    if u_ans1 in ["เบริลเลียม", "beryllium"]:
        score += 1

    if u_ans2 in ["เจอร์เมเนียม", "germanium"]:
        score += 1

    if u_ans3 in ["ยูโรเพียม", "europium"]:
        score += 1

    if u_ans4 in ["ทังสเตน", "tungsten"]:
        score += 1

    if u_ans5 in ["เฟอร์เมียม", "fermium"]:
        score += 1

    # 1. ปุ่มเริ่มเล่นเกม

st.button("🎮 เริ่มเล่นเกม", on_click=reset_game)

#  แถบแสดงเวลานับเวลานับถอยหลัง

if "start" in st.session_state and not st.session_state.get("is_ended", False):

    time_left = int(30 - (time.time() - st.session_state.start))

    if time_left > 0:

        st.error(f"⏳ เหลือเวลา: {time_left} วินาที")

    else:

        st.session_state.is_ended = True

        st.rerun()

st.divider()
    # แสดงผลคะแนน
    if score == 5:
        st.success("🎉 อย่าโหดคร้าบจารย์! ตอบถูกทั้งหมด 5 ข้อ")
    elif score >= 3:
        st.info("👍 So Very Good but พยายามอีกนิสส์")
    else:
        st.warning("ลองทบทวนตารางธาตุแล้วเล่นใหม่อีกครั้ง")

    st.write(f"### คะแนนของคุณ: {score} / 5")

    # แสดงเฉลย
    st.write("### 📖 เฉลย")
    st.write("1. Be = เบริลเลียม (Beryllium)")
    st.write("2. Ge = เจอร์เมเนียม (Germanium)")
    st.write("3. Eu = ยูโรเพียม (Europium)")
    st.write("4. W = ทังสเตน (Tungsten)")
    st.write("5. Fm = เฟอร์เมียม (Fermium)")
