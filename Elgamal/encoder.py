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

def encoder_text(plaintext, public_key):
    list_ciphertext_c1 = ''
    list_ciphertext_c2 = ''
    p, g, A = public_key
    min_chars = minimum_hex_chars(p)
    for c in plaintext:
        # if c not in alphabet:
        #     continue
        plaintext_to_int = ord(c)
        
        # Chọn một số nguyên k ngẫu nhiên
        k = random.randint(2, p - 2)
        
        # Tính a = g^k mod p
        c1 = pow(g, k, p)
        # Tính b = h^k * plaintext mod p
        c2 = (pow(A, k, p) * plaintext_to_int) % p
        # Chuyển về Hex
        c1 = Dec_to_Hex(c1, min_chars)
        c2 = Dec_to_Hex(c2, min_chars)
        list_ciphertext_c1 += c1
        list_ciphertext_c2 += c2
    # Trả về cặp giá trị mã hóa (a, b)
    return list_ciphertext_c1, list_ciphertext_c2