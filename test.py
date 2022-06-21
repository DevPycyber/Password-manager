from cryptography.fernet import Fernet

def encrypt_password(password):
	key = Fernet.generate_key()
	f = Fernet(key)
	token = f.encrypt(b, str(password))
	return token

def decrypt_password(encypted_password, key):
	plaintext_password = f.decrypt(encrypted_password)
	
	
	
