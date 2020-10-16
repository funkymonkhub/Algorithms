import hashlib

def hashing(filename):
    hash_md5 = hashlib.md5()
    with open(filename, "rb") as f:
        for temp in iter(lambda: f.read(4096), b""):
            hash_md5.update(temp)
    return hash_md5.hexdigest()

message = hashing("text1.txt")
print(message)