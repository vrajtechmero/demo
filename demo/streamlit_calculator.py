import streamlit as st
from streamlit_lottie import st_lottie
import requests
from calculator import add, subtract, multiply, divide, exponent, modulus, sqrt, sine, cosine, tangent, logarithm

# Function to load Lottie animation from a URL
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Lottie animation URLs
lottie_calculator = "https://assets2.lottiefiles.com/packages/lf20_2ks3pjua.json"
lottie_sidebar = "https://assets2.lottiefiles.com/packages/lf20_9cyyl8i4.json"  # fun sidebar animation
lottie_success = "https://assets2.lottiefiles.com/packages/lf20_jbrw3hcz.json"   # checkmark animation

# Load animations
calc_animation = load_lottieurl(lottie_calculator)
sidebar_animation = load_lottieurl(lottie_sidebar)
success_animation = load_lottieurl(lottie_success)

# Layout: Top animation and title
st.markdown("""
    <style>
    .main-title {text-align: center; font-size: 2.5rem; font-weight: bold; color: #4F8BF9; margin-bottom: 0;}
    .subtitle {text-align: center; color: #888; margin-top: 0;}
    .stButton>button {background-color: #4F8BF9; color: white; font-weight: bold; border-radius: 8px;}
    .stNumberInput>div>input {border-radius: 8px;}
    </style>
""", unsafe_allow_html=True)

if calc_animation is not None:
    st_lottie(calc_animation, height=180, key="calculator-animation")
st.markdown('<div class="main-title">Advanced Calculator</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A beautiful, interactive calculator with animations</div>', unsafe_allow_html=True)

# Sidebar: Animation and history
with st.sidebar:
    if sidebar_animation is not None:
        st_lottie(sidebar_animation, height=120, key="sidebar-animation")
    st.header("Calculation History")
    def get_history():
        if 'history' not in st.session_state:
            st.session_state['history'] = []
        return st.session_state['history']
    history = get_history()
    if history:
        for item in reversed(history):
            st.write(item)
    else:
        st.write("No calculations yet.")

# Main calculator UI in a card-like container
st.markdown("""
    <div style='background: #f7fafd; border-radius: 16px; padding: 2rem 1.5rem; margin-top: 1.5rem; box-shadow: 0 2px 8px #e3e8f0;'>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    operation = st.selectbox(
        "Select operation:",
        [
            "Add", "Subtract", "Multiply", "Divide", "Exponent (x^y)", "Modulus (x % y)",
            "Square Root", "Sine (degrees)", "Cosine (degrees)", "Tangent (degrees)", "Logarithm (base 10)"
        ]
    )
with col2:
    st.markdown("<div style='height: 2.2em'></div>", unsafe_allow_html=True)  # spacing
    if operation in ["Add", "Subtract", "Multiply", "Divide", "Exponent (x^y)", "Modulus (x % y)"]:
        num1 = st.number_input("Enter first number:", value=0.0, format="%f", key="num1")
        num2 = st.number_input("Enter second number:", value=0.0, format="%f", key="num2")
    else:
        num1 = st.number_input("Enter the number:", value=0.0, format="%f", key="num1_single")
        num2 = None

st.markdown("</div>", unsafe_allow_html=True)  # close card

# Calculate button and result
if st.button("Calculate", use_container_width=True):
    try:
        if operation == "Add":
            result = add(num1, num2)
            output = f"{num1} + {num2} = {result}"
        elif operation == "Subtract":
            result = subtract(num1, num2)
            output = f"{num1} - {num2} = {result}"
        elif operation == "Multiply":
            result = multiply(num1, num2)
            output = f"{num1} * {num2} = {result}"
        elif operation == "Divide":
            result = divide(num1, num2)
            output = f"{num1} / {num2} = {result}"
        elif operation == "Exponent (x^y)":
            result = exponent(num1, num2)
            output = f"{num1} ^ {num2} = {result}"
        elif operation == "Modulus (x % y)":
            result = modulus(num1, num2)
            output = f"{num1} % {num2} = {result}"
        elif operation == "Square Root":
            result = sqrt(num1)
            output = f"sqrt({num1}) = {result}"
        elif operation == "Sine (degrees)":
            result = sine(num1)
            output = f"sin({num1}°) = {result}"
        elif operation == "Cosine (degrees)":
            result = cosine(num1)
            output = f"cos({num1}°) = {result}"
        elif operation == "Tangent (degrees)":
            result = tangent(num1)
            output = f"tan({num1}°) = {result}"
        elif operation == "Logarithm (base 10)":
            result = logarithm(num1)
            output = f"log10({num1}) = {result}"
        else:
            output = "Invalid operation."
        if success_animation is not None:
            st_lottie(success_animation, height=80, key="success-animation")
        st.success(output)
        history.append(output)
    except Exception as e:
        st.error(f"Error: {e}") 
