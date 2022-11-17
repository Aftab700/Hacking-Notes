### What is Active Directory?


- Directory service developed by Microsoft to manage Windows domain networks
- Stores information related to object, such as Computers, Users, Printers, etc.
  - Think about it as a phone book for Windows
- Authenticates using Kerberos tickets.
  - Non-Windows devices, such as Linux machines, firewalls, etc. can also authenticate to Active Directory via RADIUS or LDAP

---

### Why Active Directory?

- Active Directory is the most commonly used identity management service in the world
  - 95% of Fortune 1000 companies implement the service in their networks
- Can be exploited without ever attacking patchable exploits.
  - Instead, we abuse features, trusts, components, and more.

---

### Domain Controllers

A domain controller is a server with the AD DS server role installed that has specifically been promoted to a domain controller

Domain controllers:
- Host a copy of the AD DS directory store
- Provide authentication and authorization services
- Replicate updates to other domain controllers in the domain and forest
- Allow administrative access to manage user accounts and network resources


---

### AD DS Data Store
The AD DS data store contains the database files and processes that store and manage directory information for users, services, and applications

The AD DS data store:
- Consists of the Ntds.dit file
- Is stored by default in the %SystemRoot%\NTDS folder on all domain controllers
- Is accessible only through the domain controller processes and protocols

---

### AD DS Schema

The AD DS Schema:

- Defines every type of object that can be stored in the directory
- Enforce rules regarding object creation and configuration


 | Object Types | Function | Examples |
|---|---|---|
| Class Object  | What objects can be created in the directory | User <br /> Computer |
|Attribute Object |Information that can be attached to an object | Display name |


