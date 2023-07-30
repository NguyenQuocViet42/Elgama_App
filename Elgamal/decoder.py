
import numpy as np
import random
random.seed(40)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Dec_to_Hex(decimal_number, min_chars):
    hex_number = hex(decimal_number)[2:]  # Chuyển đổi thành số hệ 16 và loại bỏ tiền tố "0x"
    padded_hex_number = hex_number.zfill(min_chars)  # Điền đầy 0 nếu cần thiết
    return padded_hex_number

def Hex_to_Dec(Hex_number):
    decimal_number = int(Hex_number, 16)
    return decimal_number

def minimum_hex_chars(dec):
    # Chuyển đổi số dec thành số hex
    hex_number = hex(dec)[2:]

    # Trả về số lượng ký tự hex tối thiểu
    return len(hex_number)

def split_equal_length(string, length):
    # Chia chuỗi thành các phần có độ dài bằng nhau
    return [string[i:i+length] for i in range(0, len(string), length)]

def decode_text(ciphertext, private_key, p):
    BanRo = ''
    min_chars = minimum_hex_chars(p)
    list_c1 = split_equal_length(ciphertext[0], min_chars)
    list_c2 = split_equal_length(ciphertext[1], min_chars)
    for i in range(len(list_c1)):
        c1 = Hex_to_Dec( list_c1[i] )
        c2 = Hex_to_Dec( list_c2[i] )
        
        # Tính a^x mod p
        ax = pow(c1, private_key, p)
        
        # Tính a^(-x) mod p
        ax_inv = pow(ax, -1, p)
        
        # Tính plaintext = (a^(-x) * b) mod p
        plaintext = (ax_inv * c2) % p
        BanRo += chr(plaintext)
    # Trả về giá trị giải mã
    return BanRo