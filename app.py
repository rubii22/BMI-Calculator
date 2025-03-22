import streamlit as st

# 🌟 Page Configurations
st.set_page_config(page_title="BMI Calculator", layout="centered")

# 🎨 Custom CSS for Better UI
st.markdown(
    """
    <style>
    body { background-color: #f4f4f4; font-family: Arial, sans-serif; }
    .big-font { font-size:24px !important; font-weight: bold; color: #333; }
    .result { font-size:28px !important; font-weight: bold; text-align: center; }
    .tip { font-size:18px !important; font-style: italic; color: #555; }
    </style>
    """,
    unsafe_allow_html=True
)

# 🏋️‍♂️ Title & Subtitle
st.title("🏋️‍♂️ Advanced BMI Calculator")
st.write("Calculate your **Body Mass Index (BMI)** and receive health recommendations instantly! 🚀")

# 📝 User Inputs
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("⚖️ Enter your weight (kg)", min_value=1.0, step=0.1)
with col2:
    height = st.number_input("📏 Enter your height (m)", min_value=0.5, step=0.01)

age = st.slider("🎂 Select your age", 1, 120, 25)
gender = st.radio("🚻 Select your gender", ["Male", "Female"])

# 🔢 BMI Calculation
def calculate_bmi(weight, height):
    return round(weight / (height ** 2), 2) if height > 0 else 0

# 📌 Get BMI Category & Color
def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight 😔", "#f1c40f"
    elif 18.5 <= bmi < 24.9:
        return "Normal ✅", "#2ecc71"
    elif 25 <= bmi < 29.9:
        return "Overweight ⚠️", "#f39c12"
    else:
        return "Obese 🚨", "#e74c3c"

# 🎯 Calculate BMI
if st.button("💪 Calculate BMI"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        category, color = get_bmi_category(bmi)

        # 🌟 Display Results
        st.markdown(f"<p class='big-font'>Your BMI is:</p>", unsafe_allow_html=True)
        st.markdown(f"<p class='result' style='color:{color};'>{bmi} ({category})</p>", unsafe_allow_html=True)

        # 📊 Progress Bar Representation
        st.progress(min(int(bmi * 4), 100))

        # 💡 Personalized Health Tips
        st.subheader("💡 Health Recommendations:")
        if bmi < 18.5:
            st.markdown("<p class='tip'>🍽️ Try consuming more nutrient-dense foods and maintain a balanced diet.</p>", unsafe_allow_html=True)
        elif 18.5 <= bmi < 24.9:
            st.markdown("<p class='tip'>✅ Great job! Keep maintaining a healthy lifestyle with proper exercise and diet.</p>", unsafe_allow_html=True)
        elif 25 <= bmi < 29.9:
            st.markdown("<p class='tip'>🏃 Consider increasing your physical activity and monitoring calorie intake.</p>", unsafe_allow_html=True)
        else:
            st.markdown("<p class='tip'>🚨 It is advised to consult a healthcare provider for personalized guidance.</p>", unsafe_allow_html=True)

    else:
        st.error("❌ Please enter valid weight and height values!")
