import hashlib

def get_uuid(name):
    return hashlib.md5(name.encode()).hexdigest()
