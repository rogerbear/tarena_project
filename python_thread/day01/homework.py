import os

size = os.path.getsize('cp.txt')
print(size)

pid = os.fork()

if pid < 0:
    print('create process failed!')

elif pid == 0:
    n = size // 2
    child_file = open('child.txt', 'w')
    with open('cp.txt', 'r') as f:
        while True:
            if n < 64:
                data = f.read(n)
                child_file.write(data)
                break
            data = f.read(64)
            child_file.write(data)
            n -= 64
    child_file.close()

else:
    parent_file = open('parent.txt', 'w')
    with open('cp.txt') as f:
        f.seek(size // 2, 0)
        while True:
            data = f.read(64)
            if not data:
                break
            parent_file.write(data)
    parent_file.close()
