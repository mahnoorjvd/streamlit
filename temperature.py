import streamlit as st

def convert_temperature(temp, conversion_type):
    """Convert temperature based on the selected conversion type"""
    try:
        if conversion_type == "Celsius to Fahrenheit":
            return (temp * 9/5) + 32
        elif conversion_type == "Fahrenheit to Celsius":
            return (temp - 32) * 5/9
        elif conversion_type == "Celsius to Kelvin":
            return temp + 273.15
        elif conversion_type == "Kelvin to Celsius":
            return temp - 273.15
    except TypeError:
        return None

st.title("Temperature Converter")
st.subheader("Converts temperature in seconds!")


temp_input = st.text_input("Enter the temperature:")
conversion_type = st.selectbox("Choose conversion type:", 
                             ["Celsius to Fahrenheit",
                              "Fahrenheit to Celsius",
                              "Celsius to Kelvin",
                              "Kelvin to Celsius"])

if st.button("Convert"):
    if temp_input:
        try:
            temp = float(temp_input)
            result = convert_temperature(temp, conversion_type)
            
            if result is not None:
               
                from_unit, to_unit = conversion_type.split(" to ")
                st.success(f"{temp}°{from_unit[0]} = {result:.2f}°{to_unit[0]}")
            else:
                st.error("Invalid input. Please enter a valid number.")
                
        except ValueError:
            st.error("Please enter a valid numerical temperature!")
    else:
        st.warning("Please enter a temperature to convert!")

