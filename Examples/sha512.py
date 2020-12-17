#Example made by theMaster6417
#do encrypt("Your texr here")

import hashlib




def encrypt(dio):
    hashed = hashlib.sha512(dio.encode())
    print("SHA-512 Hexdigest:", hashed.hexdigest())
   
    
