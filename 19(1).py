import random
import string
import pickle

ABC = set(random.choice(string.ascii_letters) for i in range(18))

D = set(random.choice(string.digits) for i in range(4))

K = ABC.union(D)

with open("file.bin", "wb") as f:
    pickle.dump(K, f)
    