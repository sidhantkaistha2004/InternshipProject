import random
import string

def generate_password(length):
  """Generates a random password of the specified length."""
  lowercase_letters = string.ascii_lowercase
  uppercase_letters = string.ascii_uppercase
  digits = string.digits
  special_characters = string.punctuation

  # Combine all character sets
  all_characters = lowercase_letters + uppercase_letters + digits + special_characters

  # Ensure at least one character from each category
  password = random.choice(lowercase_letters) + random.choice(uppercase_letters) + random.choice(digits) + random.choice(special_characters)

  # Fill the remaining slots with random characters from the combined set
  password += ''.join(random.sample(all_characters, length - 4))

  # Shuffle the password characters to improve randomness
  random.shuffle(list(password))

  # Combine the shuffled characters back into a string
  password = ''.join(password)

  return password

def main():
  """Prompts the user for input and generates passwords."""
  while True:
    try:
      length = int(input("Enter desired password length (minimum 8 characters): "))
      number = int(input("Enter the number of passwords to generate: "))
      
      if length < 8:
        print("Password length must be at least 8 characters.")
        continue

      break
    except ValueError:
      print("Invalid input. Please enter integers only.")

  for _ in range(number):
    print(generate_password(length))

if _name_ == "_main_":
  main()
