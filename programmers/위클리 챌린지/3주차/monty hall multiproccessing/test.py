import time

st = time.time()

def count(name):
    for i in range(1, 999999999):
        # print(f"{name} : {i}")
        pass
    
num_list = {'P1', 'P2', 'P3', 'P4'}
for num in num_list:
    count(num)

print(f"{time.time() - st} seconds")