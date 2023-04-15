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

def calculate_gpa(grades):
    grade_points = {"A+": 4.0, "A": 4.0, "A-": 3.7, "B+": 3.3, "B": 3.0, "B-": 2.7, "C+": 2.3, "C": 2.0, "C-": 1.7, "D+": 1.3, "D": 1.0, "F": 0.0}
    total_credits = 0
    total_grade_points = 0
    for grade, credits in grades.items():
        total_credits += credits
        total_grade_points += grade_points[grade] * credits
    gpa = total_grade_points / total_credits
    return round(gpa, 2)

st.title("IP Address Converter & BMI Calculator")

conversion_choice = st.selectbox("What do you want to convert?", ["IP address to binary", "Binary to IP address", "Word/phrase to binary", "Binary to word/phrase", "Calculate BMI", "Calculate GPA"])

if conversion_choice == "IP address to binary":
    ip_address = st.text_input("Enter an IP address (IPv4):")
    if ip_address:
        binary_ip_output = ip_to_binary(ip_address)
        st.write("Binary IP address:", binary_ip_output)

elif conversion_choice == "Binary to IP address":
    binary_ip_input = st.text_input("Enter a binary IP address:")
    if binary_ip_input:
        ip_output = binary_to_ip(binary_ip_input)
        st.write("IP address:", ip_output)

elif conversion_choice == "Word/phrase to binary":
    ascii_input = st.text_input("Enter a word or phrase to convert to binary:")
    if ascii_input:
        binary_ascii_output = ascii_to_binary(ascii_input)
        st.write("Binary output:", binary_ascii_output)

elif conversion_choice == "Binary to word/phrase":
    binary_ascii_input = st.text_input("Enter a binary word or phrase:")
    if binary_ascii_input:
        ascii_output = binary_to_ascii(binary_ascii_input)
        st.write("ASCII output:", ascii_output)

elif conversion_choice == "Calculate BMI":
    height_input = st.number_input("Enter your height in cm:")
    weight_input = st.number_input("Enter your weight in kg:")
    if height_input and weight_input:
        bmi = calculate_bmi(height_input, weight_input)
        st.write("Your BMI is:", bmi)

elif conversion_choice == "Calculate GPA":
    grades = {}
    total_subjects = int(st.number_input("Enter the total number of subjects:"))

    for i in range(total_subjects):
        grade = st.selectbox(f"Select grade for subject {i+1}:", ["A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "F"])
        credits = st.number_input(f"Enter credits for subject {i+1}:")
        grades[grade] = credits
    if grades:
        gpa = calculate_gpa(grades)
        st.write("Your GPA is:", gpa)