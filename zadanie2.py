import base64


def encode(text):
    message_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    return base64_bytes.decode('ascii')

def decode(text):
    base64_bytes = text.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    return message_bytes.decode('ascii')


print("wpisz tekst do zaszyfrowania")
text = input()
print(text)
encoded = encode(text)
decoded = decode(encoded)
print(f"wiadomość zaszyfrowana\n{encoded}")
print(f"wiadomość odszyfrowana\n{decoded}")
