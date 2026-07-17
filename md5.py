import hashlib
import sys

str = input("Enter the value")

str = bytes(str, 'utf-8')
result = hashlib.md5(str);
print("The byte equivalent of hash is :", end="")
print(result.digest())

print("\r")
print("The size of output :",end="")
print(sys.getsizeof(result.digest()))

str = input("Enter the value")

str = bytes(str, 'utf-8')
result = hashlib.md5(str);
print("The byte equivalent of hash is :", end="")
print(result.digest())

print("\r")
print("The size of output :", end="")
print(sys.getsizeof(result.digest()))
