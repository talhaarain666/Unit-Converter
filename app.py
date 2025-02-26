import streamlit as st

unit_conversions = {
    "Area": {
        "Square Meters": 1,
        "Square Kilometers": 0.000001,
        "Square Centimeters": 10000,
        "Square Millimeters": 1_000_000,
        "Square Miles": 3.861e-7,
        "Square Yards": 1.19599,
        "Square Feet": 10.7639,
        "Square Inches": 1550.0031,
        "Hectares": 0.0001,
        "Acres": 0.000247105,
    },
    "Data Transfer Rate": {
        "Bits per second (bps)": 1,
        "Kilobits per second (Kbps)": 1e-3,
        "Megabits per second (Mbps)": 1e-6,
        "Gigabits per second (Gbps)": 1e-9,
        "Terabits per second (Tbps)": 1e-12,
    },
    "Digital Storage": {
        "Bytes": 1,
        "Kilobytes (KB)": 1e-3,
        "Megabytes (MB)": 1e-6,
        "Gigabytes (GB)": 1e-9,
        "Terabytes (TB)": 1e-12,
    },
    "Energy": {
        "Joules": 1,
        "Kilojoules": 0.001,
        "Calories": 0.239006,
        "Kilocalories": 0.000239006,
        "Watt-hours": 0.000277778,
    },
    "Frequency": {
        "Hertz": 1,
        "Kilohertz": 1e-3,
        "Megahertz": 1e-6,
        "Gigahertz": 1e-9,
    },
    "Fuel Economy": {
        "Kilometers per liter": 1,
        "Miles per gallon": 2.35215,
    },
    "Length": {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Micrometers": 1_000_000,
        "Nanometers": 1_000_000_000,
        "Miles": 0.000621371,
        "Nautical Miles": 0.000539957,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701,
    },
    "Mass": {
        "Kilograms": 1,
        "Grams": 1000,
        "Milligrams": 1_000_000,
        "Pounds": 2.20462,
        "Ounces": 35.274,
    },
    "Plane Angle": {
        "Degrees": 1,
        "Radians": 0.0174533,
        "Gradians": 1.11111,
    },
    "Pressure": {
        "Pascals": 1,
        "Kilopascals": 0.001,
        "Bars": 1e-5,
        "Atmospheres": 9.8692e-6,
        "Millimeters of Mercury": 0.00750062,
        "Pounds per square inch (PSI)": 0.000145038,
    },
    "Speed": {
        "Meters per second": 1,
        "Kilometers per hour": 3.6,
        "Miles per hour": 2.23694,
        "Knots": 1.94384,
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K",
    },
    "Time": {
        "Seconds": 1,
        "Minutes": 1/60,
        "Hours": 1/3600,
        "Days": 1/86400,
    },
    "Volume": {
        "Liters": 1,
        "Milliliters": 1000,
        "Cubic meters": 0.001,
        "Cubic centimeters": 1000,
        "Cubic inches": 61.0237,
        "Cubic feet": 0.0353147,
        "Gallons": 0.264172,
    }
}

def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32

st.title("Unit Converter")
st.markdown("<h1 style='text-align: center; color: #4A90E2;'>🔄 Unit Converter</h1>", unsafe_allow_html=True)


category = st.selectbox("Select a category", list(unit_conversions.keys()))

units = list(unit_conversions[category].keys())

col1, col2, col3 = st.columns([1.2, 0.5, 1.2])

with col1:
    from_unit = st.selectbox("From", units)

with col2:
    st.markdown("<h4 style='text-align: center;'>➡️</h4>", unsafe_allow_html=True)

with col3:
    to_unit = st.selectbox("To", units)


value = st.number_input("Enter Value", min_value=0.0, format="%.6f")

if st.button("Convert"):
    if category == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    else:
        result = value * unit_conversions[category][to_unit] / unit_conversions[category][from_unit]
    
    formula = f"({value} × {unit_conversions[category][to_unit]}) / {unit_conversions[category][from_unit]}"
    st.success(f"Converted Value: {result} {to_unit}")
    st.markdown(f"### 📏 Formula Used: `{formula}`")

