import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    try:
        length = int(input("enter the desired length of your password: "))
        if length <= 0:
            print("invalid input! Your password length can't be less or equal to 0")
            return

        password = generate_password(length)
        print("Generated Password: ", password)
    except ValueError:
        print("Please enter a valid number.")
if __name__=="__main__":
    main()