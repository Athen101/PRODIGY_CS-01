def encrypt(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                encrypted_char = chr((ord(char) - 65 + shift) % 26 + 65)
            else:
                encrypted_char = chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_message += encrypted_char
        else:
            encrypted_message += char
    return encrypted_message

def decrypt(message, shift):
    decrypted_message = ""
    for char in message:
        if char.isalpha():
            if char.isupper():
                decrypted_char = chr((ord(char) - 65 - shift) % 26 + 65)
            else:
                decrypted_char = chr((ord(char) - 97 - shift) % 26 + 97)
            decrypted_message += decrypted_char
        else:
            decrypted_message += char
    return decrypted_message

# Example usage
message = input("Enter your message: ")
shift = int(input("Enter the shift value: "))

encrypted_message = encrypt(message, shift)
print("Encrypted message:", encrypted_message)

decrypted_message = decrypt(encrypted_message, shift)
print("Decrypted message:", decrypted_message)