import streamlit as st

# Function to perform calculation
def calculate(operation, num1, num2):
    if operation == 'Add':
        result = num1 + num2
    elif operation == 'Subtract':
        result = num1 - num2
    elif operation == 'Multiply':
        result = num1 * num2
    elif operation == 'Divide':
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"
    return result

# Streamlit UI
st.title("Simple Calculator")

# Input fields
num1 = st.number_input("Enter Number 1:", value=0.0)
num2 = st.number_input("Enter Number 2:", value=0.0)

# Operation buttons
operation = st.selectbox("Choose an operation:", ['Add', 'Subtract', 'Multiply', 'Divide'])

# Button to calculate
if st.button("Calculate"):
    result = calculate(operation, num1, num2)
    st.write(f"Result: {result}")
