from cryptography.fernet import Fernet
import hashlib

def getHash(val):
	m = hashlib.md5();
	m.update(val);
	return m.digest();
def encrypt(data):
	key = Fernet.generate_key();
	f = Fernet(key);
	enc = f.encrypt(data);
	print("Encrypt Key:", key, "Ciphertext:", enc);
	print("Generated MD5 Checksum:", getHash(enc));   #Is this where it needs to be? 
	return (key, enc, getHash(enc));
def decrypt(data):
	f = Fernet(data[0]);
	print("Decript Key:", data[0], "Plain text:", f.decrypt(data[1]));
	return f.decrypt(data[1]);
	
