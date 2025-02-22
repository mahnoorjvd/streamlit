import streamlit as st

st.title("Arithmetic Calculator")
st.subheader("Simple Calculator with Basic Operations")


col1, col2 = st.columns(2)

with col1:
    num1 = st.number_input("Enter first number", value=0.0)

with col2:
    num2 = st.number_input("Enter second number", value=0.0)


operation = st.selectbox("Select operation", 
                       ["Addition", "Subtraction", "Multiplication", "Division"])

result = None
try:
    if operation == "Addition":
        result = num1 + num2
    elif operation == "Subtraction":
        result = num1 - num2
    elif operation == "Multiplication":
        result = num1 * num2
    elif operation == "Division":
        if num2 == 0:
            st.error("Cannot divide by zero!")
        else:
            result = num1 / num2
except Exception as e:
    st.error(f"An error occurred: {str(e)}")


if result is not None:
    st.success(f"**Result**: {num1} {operation} {num2} = **{result:.2f}**")


st.markdown("---")
st.markdown("""
<style>
    [data-testid=stSuccess] {  /* Style success messages */
        padding: 20px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)