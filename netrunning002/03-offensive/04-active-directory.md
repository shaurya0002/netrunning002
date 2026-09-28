# Active Directory Attacks (Phase 4)

## Must know
- AD structure: domain, forest, OU, GPO, trust
- Kerberos auth flow, NTLM, LDAP
- Attacks: Kerberoasting, AS-REP roasting, pass-the-hash, pass-the-ticket, DCSync, ACL abuse, BloodHound for attack path mapping
- Tools: Impacket suite, BloodHound/SharpHound, Rubeus, CrackMapExec/NetExec, Mimikatz (lab only, will be flagged by AV — use in isolated lab)

## Build your own AD lab
- Windows Server (eval) as Domain Controller + 1–2 Windows client VMs
- Guides: "GOAD" (Game of Active Directory) — vulnerable AD lab you deploy yourself

## Practice
- TryHackMe: Active Directory Basics, Attacking Kerberos, Breaching AD
- HTB: Active Directory-focused boxes (Forest, Sauna, etc.)
