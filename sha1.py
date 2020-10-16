import hashlib

def hashing(filename):

   hash_value = hashlib.sha1()
   with open(filename,'rb') as file:

       temp = 0
       while temp != b'':
           temp = file.read(1024)
           hash_value.update(temp)
           
   return hash_value.hexdigest()

message = hashing("text1.txt")
print(message)