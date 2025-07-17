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

# Example Lottie animation (calculator)
lottie_url = "https://assets2.lottiefiles.com/packages/lf20_2ks3pjua.json"  # You can change this to any Lottie URL
top_animation = load_lottieurl(lottie_url)

if top_animation:
    st_lottie(top_animation, height=200, key="calculator-animation")

st.title("Advanced Calculator")

# Sidebar for history
def get_history():
    if 'history' not in st.session_state:
        st.session_state['history'] = []
    return st.session_state['history']

history = get_history()

operation = st.selectbox(
    "Select operation:",
    [
        "Add", "Subtract", "Multiply", "Divide", "Exponent (x^y)", "Modulus (x % y)",
        "Square Root", "Sine (degrees)", "Cosine (degrees)", "Tangent (degrees)", "Logarithm (base 10)"
    ]
)

if operation in ["Add", "Subtract", "Multiply", "Divide", "Exponent (x^y)", "Modulus (x % y)"]:
    num1 = st.number_input("Enter first number:", value=0.0, format="%f")
    num2 = st.number_input("Enter second number:", value=0.0, format="%f")
else:
    num1 = st.number_input("Enter the number:", value=0.0, format="%f")
    num2 = None

if st.button("Calculate"):
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
        st.success(output)
        history.append(output)
    except Exception as e:
        st.error(f"Error: {e}")

st.sidebar.header("Calculation History")
if history:
    for item in reversed(history):
        st.sidebar.write(item)
else:
    st.sidebar.write("No calculations yet.")
