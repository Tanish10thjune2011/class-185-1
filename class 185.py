import hashlib
from simplecrypt import encrypt, decrypt

value = "Peter:Hello"
def SHA256():
    result = hashlib.sha256( value.encode() )
    print("SHA256 encrypted data : ",result.hexdigest())
SHA256()
def MD5():
    result = hashlib.md5(value.encode())
    print("MD5 encrypted data : ",result.hexdigest())
MD5()

message = "Peter:Hello"
hex_string = ''
md5_file= open("md5.txt")
md5_file.write(file_hexd)
def encryption():
    global hex_string
    ciphercode = encrypt('AIM', message)
    hex_string = ciphercode.hex()
    print("Encryption", hex_string)
    text_file = fd.askopenfilename(title="Open Text File",filetypes=(("Text Files",
  "*.txt"),))
def decryption():
    global hex_string
    byte_str = bytes.fromhex(hex_string)
    original = decrypt('AIM', byte_str)
    final_message = original.decode("utf-8")
    print("Decryption", final_message)
encryption()
decryption()