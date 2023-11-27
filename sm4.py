from Crypto.Cipher import SM4
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.strxor import strxor

def sm4_encrypt(plaintext, key, iv):
    cipher = SM4.new(key, SM4.MODE_CBC, iv)
    ciphertext = cipher.encrypt(pad(plaintext.encode(), SM4.block_size))
    return ciphertext

def sm4_decrypt(ciphertext, key, iv):
    cipher = SM4.new(key, SM4.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext)
    return unpad(decrypted_data, SM4.block_size).decode()

# 将秘钥和盐值转换为字节类型
key = bytes.fromhex("b8b00596d6ac4d13")
iv = bytes.fromhex("9047efcf9aa73b06")

# 待加密的明文
plaintext = "Hello, this is a test message."

# 加密
ciphertext = sm4_encrypt(plaintext, key, iv)
print("加密后的结果:", ciphertext.hex())

# 解密
decrypted_text = sm4_decrypt(ciphertext, key, iv)
print("解密后的结果:", decrypted_text)