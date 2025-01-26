
text = input("Enter the string to encrypt: ")
shift_value = int(input("Enter the distance: "))
encrypted_text = ""
for character in text:
    original_ascii = ord(character)
    shifted_ascii = original_ascii + shift_value
    if shifted_ascii > ord('z'):
        shifted_ascii = ord('a') + (shift_value - (ord('z') - original_ascii + 1))
    encrypted_text += chr(shifted_ascii)
print("Encrypted string:", encrypted_text)

cipher_text = input("Enter the string to decrypt: ")
reverse_shift = int(input("Enter the distance: "))
decrypted_text = ""
for character in cipher_text:
    original_ascii = ord(character)
    shifted_ascii = original_ascii - reverse_shift
    if shifted_ascii < ord('a'):
        shifted_ascii = ord('z') - (reverse_shift - (ord('a') - original_ascii - 1))
    decrypted_text += chr(shifted_ascii)
print("Decrypted string:", decrypted_text)


text = input("Enter the string to encrypt: ")
shift_value = int(input("Enter the distance: "))
encrypted_text = ""
for character in text:
    original_ascii = ord(character)
    shifted_ascii = original_ascii + shift_value
    if shifted_ascii > ord('z'):
        shifted_ascii = ord('a') + (shift_value - (ord('z') - original_ascii + 1))
    encrypted_text += chr(shifted_ascii)
print("Encrypted string:", encrypted_text)

cipher_text = input("Enter the string to decrypt: ")
reverse_shift = int(input("Enter the distance: "))
decrypted_text = ""
for character in cipher_text:
    original_ascii = ord(character)
    shifted_ascii = original_ascii - reverse_shift
    if shifted_ascii < ord('a'):
        shifted_ascii = ord('z') - (reverse_shift - (ord('a') - original_ascii - 1))
    decrypted_text += chr(shifted_ascii)
print("Decrypted string:", decrypted_text)

