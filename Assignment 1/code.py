import hashlib
import time
start_time = time.time()
s = input()
flag = 0
i = 1
target = "0x00000FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF"
while flag == 0:
    f = s + str(i)
    hashed_string = hashlib.sha256(f.encode('utf-8')).hexdigest()
    
    if(target > hashed_string):
        flag=1
    else:
        i+=1
current_time = time.time()
print("The smallest nonce is :", i)

print("The time taken by the program to get the nonce value is :", current_time - start_time, "seconds")
