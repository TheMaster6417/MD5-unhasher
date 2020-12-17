#Example made by theMaster6417
#do encrypt("Your texr here")

import hashlib




def encrypt(dio):
    hashed = hashlib.sha1(dio.encode())
    print("SHA-1 Hexdigest:", hashed.hexdigest())
   
    
