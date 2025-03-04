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
        "Kilobytes per second (KBps)": 8e-3,   # 1 KBps = 8 Kbps
        "Megabytes per second (MBps)": 8e-6,   # 1 MBps = 8 Mbps
        "Gigabytes per second (GBps)": 8e-9,   # 1 GBps = 8 Gbps
        "Terabytes per second (TBps)": 8e-12,  # 1 TBps = 8 Tbps
        "Kibibits per second (Kibps)": 1024e-3,  # 1 Kibps = 1024 bps
        "Mebibits per second (Mibps)": 1024e-6,  # 1 Mibps = 1024 Kbps
        "Gibibits per second (Gibps)": 1024e-9,  # 1 Gibps = 1024 Mbps
        "Tebibits per second (Tibps)": 1024e-12, # 1 Tibps = 1024 Gbps
        "Kibibytes per second (KiBps)": 8192e-3, # 1 KiBps = 8 Kibps
        "Mebibytes per second (MiBps)": 8192e-6, # 1 MiBps = 8 Mibps
        "Gibibytes per second (GiBps)": 8192e-9, # 1 GiBps = 8 Gibps
        "Tebibytes per second (TiBps)": 8192e-12 # 1 TiBps = 8 Tibps
    },
    "Digital Storage": {
        "Bits": 1,
        "Kilobits (Kb)": 1e-3,
        "Megabits (Mb)": 1e-6,
        "Gigabits (Gb)": 1e-9,
        "Terabits (Tb)": 1e-12,
        "Petabits (Pb)": 1e-15,
        "Pebibits (Pib)": 1 / (1024**5),
        "Bytes (B)": 8e-1,
        "Kilobytes (KB)": 8e-4,
        "Megabytes (MB)": 8e-7,
        "Gigabytes (GB)": 8e-10,
        "Terabytes (TB)": 8e-13,
        "Petabytes (PB)": 8e-16,
        "Kibibits (Kib)": 1 / 1024,
        "Mebibits (Mib)": 1 / (1024**2),
        "Gibibits (Gib)": 1 / (1024**3),
        "Tebibits (Tib)": 1 / (1024**4),
        "Kibibytes (KiB)": 8 / 1024,
        "Mebibytes (MiB)": 8 / (1024**2),
        "Gibibytes (GiB)": 8 / (1024**3),
        "Tebibytes (TiB)": 8 / (1024**4),
        "Pebibytes (PiB)": 8 / (1024**5),
    },
    "Energy": {
        "Joules (J)": 1,
        "Kilojoules (kJ)": 1e-3,
        "Gram calorie (cal)": 1 / 4.184,
        "Kilocalorie (kcal)": 1 / 4184,
        "Watt hour (Wh)": 1 / 3600,
        "Kilowatt-hour (kWh)": 1 / 3.6e6,
        "Electronvolt (eV)": 1 / 1.60218e-19,
        "British thermal unit (BTU)": 1 / 1055.06,
        "US therm": 1 / 1.055e8,
        "Foot-pound (ft⋅lb)": 1 / 1.35582
    },
    "Frequency": {
        "Hertz": 1,
        "Kilohertz": 1e-3,
        "Megahertz": 1e-6,
        "Gigahertz": 1e-9,
    },
    "Fuel Economy": {
        "Kilometers per liter (km/L)": 1,
        "Miles per US gallon (mpg US)": 2.35215,
        "Miles per gallon (mpg)": 2.825,
        "Liters per 100 kilometers (L/100 km)": 100
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
        "Tonne": 1,
        "Kilogram": 1000,
        "Gram": 1_000_000,
        "Milligram": 1_000_000_000,
        "Microgram": 1_000_000_000_000,
        "Imperial ton": 0.984207,
        "US ton": 1.10231,
        "Stone": 157.473,
        "Pound": 2204.62,
        "Ounce": 35274
    },
    "Plane Angle": {
        "Degree": 1,
        "Radian": 0.0174533,
        "Gradian": 1.11111,
        "Milliradian": 17.4533,
        "Minute of arc": 60,
        "Arcsecond": 3600
    },
    "Pressure": {
        "Pascal": 1,
        "Kilopascal": 0.001,
        "Bar": 1e-5,
        "Standard atmosphere": 9.8692e-6,
        "Torr": 0.00750062,
        "Pound per square inch (PSI)": 0.000145038
    },
    "Speed": {
        "Metre per second": 1,
        "Kilometre per hour": 3.6,
        "Mile per hour": 2.23694,
        "Foot per second": 3.28084,
        "Knot": 1.94384
    },
    "Temperature": {
        "Celsius": "C",
        "Fahrenheit": "F",
        "Kelvin": "K",
    },
    "Time": {
        "Nanosecond": 1e9,
        "Microsecond": 1e6,
        "Millisecond": 1e3,
        "Second": 1,
        "Minute": 1/60,
        "Hour": 1/3600,
        "Day": 1/86400,
        "Week": 1/604800,
        "Month": 1/2.628e6,  # Approximate (30.44 days)
        "Calendar year": 1/3.154e7,  # Approximate (365.25 days)
        "Decade": 1/3.154e8,  # Approximate (10 years)
        "Century": 1/3.154e9  # Approximate (100 years)
    },
    "Volume": {
        "Cubic meter": 1,
        "Liter": 1000,  # 1 cubic meter = 1000 liters
        "Milliliter": 1e6,  # 1 cubic meter = 1,000,000 mL
        "Cubic centimeter": 1e6,  # Equivalent to milliliters
        "Cubic inch": 61023.7,
        "Cubic foot": 35.3147,

        # US Liquid Measures
        "US liquid gallon": 264.172,
        "US liquid quart": 1056.69,
        "US liquid pint": 2113.38,
        "US legal cup": 4166.67,
        "US fluid ounce": 33814,
        "US tablespoon": 67628,
        "US teaspoon": 202884,

        # Imperial (UK) Measures
        "Imperial gallon": 219.969,
        "Imperial quart": 879.877,
        "Imperial pint": 1759.75,
        "Imperial cup": 3519.51,
        "Imperial fluid ounce": 35195.1,
        "Imperial tablespoon": 56312.1,
        "Imperial teaspoon": 168936
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