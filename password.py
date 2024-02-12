import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")
    
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Length should be greater than 0.")
    except ValueError as ve:
        print(ve)
        return
    
    password = generate_password(length)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
