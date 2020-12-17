#Example made by theMaster6417
#do encrypt("Your texr here")

import hashlib




def encrypt(dio):
    hashed = hashlib.sha256(dio.encode())
    print("SHA-256 Hexdigest:", hashed.hexdigest())
   
    
