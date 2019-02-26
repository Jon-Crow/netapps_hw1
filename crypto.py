from cryptography.fernet import Fernet
import hashlib

def getHash(val):
	m = hashlib.md5();
	m.update(val);
	return m.digest();
def encrypt(data):
	key = Fernet.generate_key();
	f = Fernet(key);
	enc = f.encrypt(data.encode('utf-8'));
	return (key, enc, getHash(enc));
def decrypt(data):
	f = Fernet(data[0]);
	return f.decrypt(data[1]);
	
