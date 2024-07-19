import random
import string

def generate_password(length=12, include_uppercase=True, include_numbers=True, include_symbols=True):


  characters = string.ascii_lowercase
  if include_uppercase:
    characters += string.ascii_uppercase
  if include_numbers:
    characters += string.digits
  if include_symbols:
    characters += string.punctuation

  password = ''.join(random.choice(characters) for _ in range(length))
  return password

password = generate_password(length=16, include_symbols=False)
print(f"Сгенерированный пароль: {password}")
