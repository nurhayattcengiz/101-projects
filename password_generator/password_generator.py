import numpy as np
import string

def generate_password(length, use_upper, use_lower, use_digits, use_symbols):
    character_types = []
    if use_upper:
        character_types.append(string.ascii_uppercase)
    if use_lower:
        character_types.append(string.ascii_lowercase)
    if use_digits:
        character_types.append(string.digits)
    if use_symbols:
        character_types.append(string.punctuation)

    if not character_types:
        return None

# Ensure at least one character from each selected type
    password_chars = [np.random.choice(list(chars)) for chars in character_types]

    remaining_length = length - len(password_chars)
    if remaining_length > 0:
        all_chars = ''.join(character_types)
        password_chars += list(np.random.choice(list(all_chars), size=remaining_length))

    np.random.shuffle(password_chars)
    return ''.join(password_chars)

while True:
    length = int(input("Enter password length: "))
    use_upper = input("Include uppercase letters? (Y/N): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (Y/N): ").lower() == 'y'
    use_digits = input("Include digits? (Y/N): ").lower() == 'y'
    use_symbols = input("Include special characters? (Y/N): ").lower() == 'y'

    password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)

    if password:
        print(f"🔐 Generated Password: {password}")
        with open("passwords.txt", "a", encoding="utf-8") as file:
            file.write(password + "\n")
    else:
        print("⚠️ You must select at least one character type!")

    again = input("Do you want to generate another password? (Y/N): ").lower()
    if again != 'y':
        print("Exiting the program. Goodbye! 💻")
        break
