import sys

lst = []
old_size = sys.getsizeof(lst)

for i in range(64):
    lst.append(i)
    new_size = sys.getsizeof(lst)
    
    if new_size != old_size:
        print(f"List capacity changed from {old_size} bytes to {new_size} bytes.")
        old_size = new_size
