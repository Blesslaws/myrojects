import streamlit as st

def ip_to_binary(ip):
    binary_output = ""
    parts = ip.split('.')
    for part in parts:
        binary_output += format(int(part), '08b')
    return binary_output

def binary_to_ip(binary):
    ip_output = ""
    for i in range(0, 32, 8):
        ip_output += str(int(binary[i:i+8], 2)) + "."
    return ip_output[:-1]

def binary_to_ascii(binary):
    ascii_output = ""
    for i in range(0, len(binary), 8):
        ascii_output += chr(int(binary[i:i+8], 2))
    return ascii_output

def ascii_to_binary(ascii):
    binary_output = ""
    for char in ascii:
        binary_output += format(ord(char), '08b')
    return binary_output

def calculate_bmi(height, weight):
    bmi = weight / (height/100)**2
    return bmi

st.title("IP Address Converter & BMI Calculator")

ip_address = st.text_input("Enter an IP address (IPv4):")
if ip_address:
    binary_ip_output = ip_to_binary(ip_address)
    st.write("Binary IP address:", binary_ip_output)

    ascii_input = st.text_input("Enter a word or phrase to convert to binary:")
    if ascii_input:
        binary_ascii_output = ascii_to_binary(ascii_input)
        st.write("Binary output:", binary_ascii_output)

        ascii_output = binary_to_ascii(binary_ascii_output)
        st.write("ASCII output:", ascii_output)

    height_input = st.number_input("Enter your height in cm:")
    weight_input = st.number_input("Enter your weight in kg:")
    if height_input and weight_input:
        bmi = calculate_bmi(height_input, weight_input)
        st.write("Your BMI is:", bmi)
