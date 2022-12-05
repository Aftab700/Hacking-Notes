
### PowerView 

https://github.com/PowerShellMafia/PowerSploit/blob/master/Recon/PowerView.ps1

[PowerView Cheat Sheet](https://gist.github.com/HarmJ0y/184f9822b195c52dd50c379ed3117993)

```
powershell -ep bypass

Get-NetDomain

Get-NetDomainController

Get-DomainPolicy

(Get-DomainPolicy)."system access"

Get-NetUser
Get-NetUser | select cn

Get-UserProperty

Get-UserProperty -Properties pwdlastset

Get-UserProperty -Properties logoncount

Get-UserProperty -Properties badpwdcount

Get-NetComputer

Get-NetComputer -FullData

Get-NetComputer -FullData | select OperatingSystem

Get-NetGroup

Get-NetGroup -GroupName "Domain Admins"

Get-NetGroup -GroupName *admin*

Get-NetGroupMember -GroupName "Domain Admins" 

Invoke-ShareFinder

Get-NetGPO

Get-NetGPO | select displayname, whenchanged
```

---

### BloodHound

https://github.com/BloodHoundAD/BloodHound/blob/master/Collectors/SharpHound.ps1



