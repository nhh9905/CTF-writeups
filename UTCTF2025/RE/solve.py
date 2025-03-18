from pwn import process, context
context.log_level = "CRITICAL"

with open("safe_word", "rb") as f:
    content = list(f.read())

for i in range(0, 0x21):
    content[0x133D8] = i

    with open(f"safe_word_{i}", "wb") as f:
        f.write(bytes(content))

import string
found = ['']
new_found = []
for j in range(len(found[0]), 33):
    print(f"Program {j}")
    for f in found:
        for i in range(128):
            if chr(i) not in string.printable:
                continue    
            print(i)
            p = process(f"./safe_word_{j}")
            # print(p.recv())
            p.sendline((f+chr(i)).encode())
            p.wait_for_close()
            poll = p.poll()
            if poll == 0:
                print(f + chr(i), poll)
                new_found.append(f + chr(i))
            p.close()
    if len(new_found) == 0:
        print("Not Found")
        exit(0)
    print(new_found)
    found = new_found
    new_found = []

print(list(map(lambda x: x.endswith("}"), new_found)))
