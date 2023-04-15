import streamlit as st


def ipv4_to_binary(ipv4_address):
    octets = ipv4_address.split('.')
    binary_octets = [format(int(octet), '08b') for octet in octets]
    binary_ip = ''.join(binary_octets)
    return binary_ip


def ipv6_to_binary(ipv6_address):
    hex_groups = ipv6_address.split(':')
    binary_groups = [format(int(group, 16), '016b') for group in hex_groups]
    binary_ip = ''.join(binary_groups)
    return binary_ip


def binary_to_ipv4(binary_ip):
    octets = [binary_ip[i:i+8] for i in range(0, 32, 8)]
    ipv4_address = '.'.join([str(int(octet, 2)) for octet in octets])
    return ipv4_address


def binary_to_ipv6(binary_ip):
    hex_groups = [binary_ip[i:i+16] for i in range(0, 128, 16)]
    hex_ipv6 = ':'.join([hex(int(group, 2))[2:].zfill(4) for group in hex_groups])
    ipv6_address = ''
    for i in range(8):
        ipv6_address += hex_ipv6[0 + i*5:4 + i*5] + ':'
    ipv6_address = ipv6_address[:-1]
    return ipv6_address


def word_to_binary(words):
    ascii_codes = [ord(char) for word in words for char in word]
    binary_codes = [format(code, '08b') for code in ascii_codes]
    binary_string = ''.join(binary_codes)
    return binary_string


def binary_to_word(binary_string):
    ascii_codes = [int(binary_string[i:i+8], 2) for i in range(0, len(binary_string), 8)]
    word = ''.join([chr(code) for code in ascii_codes])
    return word


# Streamlit interface
st.title("Binary Converter")

ip_input = st.text_input("Enter an IP address:")
binary_ip_output = ""
if ip_input:
    if '.' in ip_input:  # IPv4 address
        binary_ip_output = ipv4_to_binary(ip_input)
    elif ':' in ip_input:  # IPv6 address
        binary_ip_output = ipv6_to_binary(ip_input)
    st.write(f"Binary representation of {ip_input}: {binary_ip_output}")

word_input = st.text_input("Enter a word or phrase:")
binary_word_output = ""
if word_input:
    binary_word_output = word_to_binary(word_input)
    st.write(f"Binary representation of {word_input}: {binary_word_output}")

binary_input = st.text_input("Enter a binary code:")
word_output = ""
if binary_input:
    word_output = binary_to_word(binary_input)
    st.write(f"Word representation of binary code {binary_input}: {word_output}")

ip_output = ""
if binary_ip_output:
    if len(binary_ip_output) == 32:  # IPv4 address
        ip_output = binary_to_ipv4(binary_ip_output)
    elif len(binary_ip_output) == 128:  # IPv6 address
        ip_output = binary_to_ipv6(binary_ip_output)
    st.write(f"IP address represented by binary code {binary_ip_output}: {ip_output}")
