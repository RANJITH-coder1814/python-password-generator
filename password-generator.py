import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def main():
    print("==== Python Password Generator ====")
    
    try:
        length = int(input("Enter desired password length: "))
        
        if length < 4:
            print("Password length should be at least 4 characters.")
        else:
            password = generate_password(length)
            print("\nGenerated Password:", password)
    
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    main()
