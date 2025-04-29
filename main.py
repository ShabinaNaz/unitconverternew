import streamlit as st
st.title("🌎Unit Converter App")
st.markdown(" ### Converter Lenght, weight And Time Instantly")
st.write("Welcome! select a category, enter a value and get the converted result in real time")

category = st.selectbox("Choose a category", ["Lenght", "weight", "time"])

def convert_Units(category, value,  unit):
    if category == "lenght":
        if unit == "Killometers to Miles":
            return value * 0.621371
        elif unit == "Killometers to Miles":
            return value / 0.621371
        

        elif category == "weight":
            if unit == "Kilograms to pounds":
                return value * 2.20462
            elif unit == "pounds to Kilograms":
                return value / 2.20462
            elif category == "Time":
                if unit == "seconds to minutes":
                    return value / 60
                elif unit == "Minutes to seconds":
                    return value *  60
                elif unit == "Minutes to hours":
                    return value / 60
                elif unit == "Hours to minutes":
                    return value * 60
                elif unit == "Hours to days":
                    return value / 24
                elif unit == "Days to hours":
                    return value * 24
    return 0

if category == "Lenght":
    unit = st.selectbox("Select Conversation", ["Miles to Kilometers","Kilometers to Miles"])          
elif category == "weight":
    unit = st.selectbox("select conversation", ["kilograms to pounds", "pounds to kilograms"])
elif category == "Time":
    unit = st.selectbox("select conversation", ["Seconds to minutes", "Minutes to Seconds", "Minutes to hours", "hours to minutes", "hours to days", "days to hours"])
            
value = st.number_input("Enter the value to convert")

if st.button("convert"):
    result = convert_Units(category,value, unit)
    st.success(f"The result is {result: .2f}")
        
        

