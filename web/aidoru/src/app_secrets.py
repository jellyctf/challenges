import hashlib

# Public visibility true/false
TALENTS = {
    "rie": True,
    "panko": True,
    "lumi": True,
    "jelly": False,
    "uruka": True,
    "lia": True
}

def get_uuid(name):
    return hashlib.md5(name.encode()).hexdigest()