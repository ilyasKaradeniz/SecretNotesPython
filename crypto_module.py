import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def get_key(p):
    pw = p.encode('utf-8')
    salt = b'd56f4g65ad65h6a5f65sda6g516s5f651s65d1fv6se5r4f'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(pw))
    f = Fernet(key)
    return f
def encrypt_note(n, p):
    f = get_key(p)
    m = n.encode('utf-8')
    return f.encrypt(m)

def decrypt_note(n, p):
    f = get_key(p)
    m = f.decrypt(n)
    return m.decode('utf-8')
