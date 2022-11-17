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

---

### Domains

Domains are used to group and manage objects in an organization


Domains:
- An administrative boundary for applying policies to groups of objects
- A replication boundary for replicating data between domain controllers
- An authentication and authorization boundary that provides a way to limit the scope of access to resources

---

### Trees

A domain tree is a hierarchy of domains in AD DS

All domains in the tree:
- Share a contiguous namespace with the parent domain
- Can have additional child domains
- By default, create a two-way transitive trust with other domains

---

### Forests

A forest is a collection of one or more domain trees

Forests:
- Share a common schema
- Share a common configuration partition
- Share a common global catalog to enable searching
- Enable trusts between all domains in the forest
- Share the Enterprise Admins and Schema Admins groups

---

### Organizational Units (Ous)

OUS are Active Directory containers that can contain users, groups, computers, and other OUS

OUS are used to:
- Represent your organization hierarchically and logically
- Manage a collection of objects in a consistent way
- Delegate permissions to administer groups of objects
- Apply policies

---

### Trusts

Trusts provide a mechanism for users to gain access to resources in another domain

| Types of Trusts | Description | Diagram |
|------|-------|-----|
|  Directional   |  The trust direction flows from trusting domain to the trusted domain    |  <img width="93" alt="image" src="https://user-images.githubusercontent.com/79740895/202502616-b269191c-3a11-4ff5-a091-f22d3a567f07.png"> |
|  Transitive   |  The trust relationship is extended beyond a two-domain trust to include other trusted domains    | <img width="168" alt="image" src="https://user-images.githubusercontent.com/79740895/202502880-94fd1485-0c9f-43f0-971c-f42cac65b93f.png">      |

- All domains in a forest trust all other domains in the forest
- Trusts can extend outside the forest

---

### Objects

| Object | Description |
|------|------|
|User | Enables network resource access for a user |
| InetOrgPerson | Similar to a user account <br/> Used for compatibility with other directory services |
| Contacts | Used primarily to assign e-mail addresses to external users <br/> Does not enable network access |
| Groups | Used to simplify the administration of access control |
| Computers | Enables authentication and auditing of computer access to resources |
| Printers | Used to simplify the process of locating and connecting to printers |
| Shared folders | Enables users to search for shared folders based on properties |

---


