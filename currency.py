import streamlit as st


EXCHANGE_RATES = {
    "USD": {
        "USD": 1.0,
        "PKR": 278.50,   
        "INR": 83.30,     
        "GBP": 0.79       
    },
    "PKR": {
        "PKR": 1.0,
        "USD": 0.0036,     
        "INR": 0.30,       
        "GBP": 0.0028      
    },
    "INR": {
        "INR": 1.0,
        "USD": 0.012,     
        "PKR": 3.34,      
        "GBP": 0.0095     
    },
    "GBP": {
        "GBP": 1.0,
        "USD": 1.27,       
        "PKR": 353.50,    
        "INR": 105.70    
    }
}

def convert_currency(amount, from_curr, to_curr):
    """Convert currency using hard-coded rates"""
    rate = EXCHANGE_RATES[from_curr][to_curr]
    return amount * rate

st.title("Currency Converter")
st.markdown("Simple currency converter with fixed exchange rates")


col1, col2, col3 = st.columns(3)
with col1:
    amount = st.number_input("Amount", min_value=0.01, value=1.0, step=0.01)
with col2:
    from_curr = st.selectbox("From", ["USD", "PKR", "INR", "GBP"])
with col3:
    to_curr = st.selectbox("To", ["USD", "PKR", "INR", "GBP"])


if st.button("Convert"):
    if from_curr == to_curr:
        st.warning("Please select different currencies for conversion")
    else:
        converted_amount = convert_currency(amount, from_curr, to_curr)
        st.success(f"**{amount:.2f} {from_curr} = {converted_amount:.2f} {to_curr}**")

