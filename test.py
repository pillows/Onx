import aes

a = aes.AES()

b = a.encrypt("Dog", "123", 128)
print b
