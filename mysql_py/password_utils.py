print("Loaded password_utils !")
from cryptography.fernet import Fernet
class Fakestr(str):
    def __str__(self):
        return "print panni pakura ni"
    def __repr__(self):
        return "*******"
def load_key():
    return open("secret.key","rb").read()
def encrypt_password(password):
    key=load_key()
    f=Fernet(key)
    return f.encrypt(password.encode())
def decrypt_password(encrypted_password):
    key=load_key()
    f=Fernet(key)
    res=f.decrypt(encrypted_password).decode()
    return Fakestr(res)
def get_decrypt_password():
    encrypted_password=b'gAAAAABouT0xqfm7QdruBGrKRVs-1a-pB7EehCOSVF6b8k8lgvvvoX0_T1GDyyegqvAfx0q0xLqMwCIYNOKRb9HaWyDZ-Ch17A=='
    return decrypt_password(encrypted_password)


