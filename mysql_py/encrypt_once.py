from password_utils import encrypt_password
from cryptography.fernet import Fernet
def Generate_key():
    key=Fernet.generate_key()
    with open("secret.key","wb") as file:
        file.write(key)
    print("key saved to secret.key")
if __name__=="__main__":
    Generate_key()
    encrypted=encrypt_password("root")
    print("Encrypted key (copy this password_utils) :")
    print(encrypted)