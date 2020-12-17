#md5 example by TheMaster6417
#to use, type in encode("Your Text Here")

import hashlib

def encode(dio):
    hashed = hashlib.md5(dio.encode())
    print("MD5 Hexidigest:", hashed.hexdigest())
