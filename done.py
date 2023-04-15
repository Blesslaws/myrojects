import streamlit as st

# Function to convert IP address to binary
def ip_to_bin(ip_address):
    # Check if IP address is IPv4 or IPv6
    if "." in ip_address:
        # IPv4 to binary
        binary_ip = ""
        for octet in ip_address.split("."):
            binary_octet = bin(int(octet))[2:].zfill(8)
            binary_ip += binary_octet
        return binary_ip
    elif ":" in ip_address:
        # IPv6 to binary
        binary_ip = ""
        for hextet in ip_address.split(":"):
            binary_hextet = bin(int(hextet, 16))[2:].zfill(16)
            binary_ip += binary_hextet
        return binary_ip
    else:
        return "Invalid IP address"

# Function to convert binary to IP address
def bin_to_ip(binary_ip):
    # Check if binary IP is IPv4 or IPv6
    if len(binary_ip) == 32:
        # Binary to IPv4
        octets = [binary_ip[i:i+8] for i in range(0, 32, 8)]
        ipv4_address = ".".join(str(int(octet, 2)) for octet in octets)
        return ipv4_address
    elif len(binary_ip) == 128:
        # Binary to IPv6
        hextets = [binary_ip[i:i+16] for i in range(0, 128, 16)]
        ipv6_address = ":".join(hex(int(hextet, 2))[2:] for hextet in hextets)
        return ipv6_address
    else:
        return "Invalid binary IP address"

# Function to convert text to binary
def text_to_bin(text):
    binary_text = ""
    for char in text:
        binary_char = bin(ord(char))[2:].zfill(8)
        binary_text += binary_char
    return binary_text

# Function to convert binary to text
def bin_to_text(binary_text):
    text = ""
    for i in range(0, len(binary_text), 8):
        byte = binary_text[i:i+8]
        char = chr(int(byte, 2))
        text += char
    return text

# Function to calculate BMI
def calculate_bmi(height, weight):
    bmi = weight / (height/100) ** 2
    return bmi

# Function to calculate GPA
def calculate_gpa(grades):
    gpa_dict = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0}
    total_credit = 0
    total_grade_point = 0
    for grade, credit in grades.items():
        if grade not in gpa_dict:
            return "Invalid grade input"
        total_credit += credit
        total_grade_point += gpa_dict[grade] * credit
    gpa = total_grade_point / total_credit
    return gpa

# Streamlit app
def app():
    st.title("Conversion, BMI and GPA Calculator")

    # Conversion choice
conversion_choice = st.selectbox("Select conversion", ["IP to binary", "Binary to IP", "Words to binary", "Binary to words", "Calculate BMI", "Calculate GPA"])
