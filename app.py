import streamlit as st
import math

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
        "Kilobytes (KB)": 1/1024,
        "Megabytes (MB)": 1/(1024**2),
        "Gigabytes (GB)": 1/(1024**3),
        "Terabytes (TB)": 1/(1024**4),
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
    """Convert temperature values between units"""
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
    return value

def get_temperature_formula(value, from_unit, to_unit):
    """Get the temperature conversion formula as a string"""
    if from_unit == to_unit:
        return f"{value}"
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return f"({value} × 9/5) + 32"
        elif to_unit == "Kelvin":
            return f"{value} + 273.15"
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return f"({value} - 32) × 5/9"
        elif to_unit == "Kelvin":
            return f"({value} - 32) × 5/9 + 273.15"
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return f"{value} - 273.15"
        elif to_unit == "Fahrenheit":
            return f"({value} - 273.15) × 9/5 + 32"
    return f"{value}"

def format_number_for_formula(num):
    """Format numbers to be more readable in the formula"""
    if isinstance(num, (int, float)):

        if num == 0:
            return "0"
        if num == 1:
            return "1"
        
        if num == int(num):
            return str(int(num))
        
        special_fractions = {
            1/60: "1/60",
            1/3600: "1/3600",
            1/86400: "1/86400",
            1/1024: "1/1024",
            1/(1024**2): "1/1048576",  # 1024²
            1/(1024**3): "1/1073741824",  # 1024³
            1/(1024**4): "1/1099511627776"  # 1024⁴
        }
        
        for fraction_value, fraction_str in special_fractions.items():
            if abs(num - fraction_value) < 1e-10:
                return fraction_str
        
        if abs(num) < 0.001 or abs(num) > 10000:
            sci = f"{num:.6e}"
            parts = sci.split('e')
            base = float(parts[0])
            exp = int(parts[1])
            
            # Format as 10^exp for cleaner display
            if abs(base - 1.0) < 1e-10:
                return f"10^{exp}"
            else:
                base_formatted = f"{base:.6f}".rstrip('0').rstrip('.')
                return f"{base_formatted} × 10^{exp}"
        
        # For decimal values
        return f"{num:.6f}".rstrip('0').rstrip('.')
    
    return str(num)

def generate_conversion_formula(value, from_unit, to_unit, category):
    """Generate a human-readable conversion formula"""
    # For same unit, just return the value
    if from_unit == to_unit:
        return f"{value}"
    
    # For temperature, use special formulas
    if category == "Temperature":
        return get_temperature_formula(value, from_unit, to_unit)
    
    # Get conversion factors
    from_factor = unit_conversions[category][from_unit]
    to_factor = unit_conversions[category][to_unit]
    
    # Calculate the conversion factor between the units
    conversion_factor = to_factor / from_factor
    
    # Format the conversion factor
    formatted_factor = format_number_for_formula(conversion_factor)
    
    # Create a readable formula
    return f"{value} × {formatted_factor}"

def smart_round(number):
    """Intelligently round numbers based on their magnitude"""
    # If it's an integer or very close to one, return it as an integer
    if abs(number - round(number)) < 1e-10:
        return int(round(number))
    
    # For very small numbers, keep more decimal places
    if abs(number) < 0.001:
        return round(number, 10)
    
    # For small numbers, keep 6 decimal places
    if abs(number) < 0.1:
        return round(number, 6)
    
    # For medium numbers, keep 4 decimal places
    if abs(number) < 1000:
        return round(number, 4)
    
    # For large numbers, keep fewer decimal places
    if abs(number) < 10000:
        return round(number, 2)
    
    # For very large numbers, round to nearest integer
    return round(number)

def format_result_for_display(number):
    """Format the result for display, handling special cases"""
    # For integers, display without decimal
    if number == int(number):
        return str(int(number))
    
    # Apply smart rounding first
    rounded = smart_round(number)
    
    # For scientific notation territory, use exponential format
    if abs(rounded) < 0.0001 or abs(rounded) > 1000000:
        # Use exponential notation but make it cleaner
        return f"{rounded:.6g}"
    
    # For regular numbers, format nicely
    result_str = f"{rounded}"
    # If it looks like a float representation, make sure it's clean
    if '.' in result_str:
        # Remove trailing zeros after decimal point
        result_str = result_str.rstrip('0').rstrip('.')
    
    return result_str

st.set_page_config(
    page_title="Unit Converter",
    page_icon="🔄",
    layout="centered"
)

st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: 700;
        text-align: center;
        color: #4A90E2;
        margin-bottom: 2rem;
        text-shadow: 1px 1px 2px rgba(0,0,0,0.1);
    }
    .convert-button {
        width: 100%;
        background-color: #4A90E2;
        color: white;
        font-weight: 600;
    }
    .tooltip-icon {
        color: #888;
        font-size: 16px;
        cursor: help;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-header'>🔄 Unit Converter</h1>", unsafe_allow_html=True)

with st.container():
    
    category = st.selectbox("Select a measurement category:", list(unit_conversions.keys()))

    units = list(unit_conversions[category].keys())

    col1, col2, col3 = st.columns([1.2, 0.5, 1.2])

    with col1:
        from_unit = st.selectbox("From:", units)

    with col2:
        st.markdown("<div style='display: flex; justify-content: center; align-items: center; height: 100%;'><h3>➡️</h3></div>", unsafe_allow_html=True)

    with col3:
        to_unit = st.selectbox("To:", units)

    value = st.number_input(
        "Enter value to convert:", 
        value=1.0, 
        step=0.1,
        format="%g"
    )

    convert_clicked = st.button("Convert", type="primary", use_container_width=True)
    
    if convert_clicked:

        if category == "Temperature":
            result = convert_temperature(value, from_unit, to_unit)
        else:
            from_factor = unit_conversions[category][from_unit]
            to_factor = unit_conversions[category][to_unit]
            result = value * to_factor / from_factor
        
        formula = generate_conversion_formula(value, from_unit, to_unit, category)
        
        formatted_result = format_result_for_display(result)
        
        st.markdown(f"<h2 style='text-align: center; margin-bottom: 0.5rem;'>{formatted_result} {to_unit}</h2>", unsafe_allow_html=True)
        
        st.markdown(f"<p style='text-align: center; font-weight: 500; margin-bottom: 0;'>Formula: {formula}</p>", unsafe_allow_html=True)
        
if category == "Temperature":
    st.info("ℹ️ Temperature conversions use specific formulas rather than simple multiplication factors.")
elif category == "Digital Storage":
    st.info("ℹ️ Digital storage conversions use base-2 (1024) rather than base-10 (1000).")