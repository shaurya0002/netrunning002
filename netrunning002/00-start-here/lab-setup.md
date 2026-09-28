# Lab Setup

## Hardware minimum
- 16 GB RAM ideal (8 GB works with 1–2 VMs), 100+ GB free disk, virtualization enabled in BIOS

## Software
1. **Hypervisor:** VirtualBox (free) or VMware Workstation Player
2. **Attacker VM:** Kali Linux (or Parrot OS) — use the prebuilt VM image
3. **Targets (vulnerable on purpose):**
   - Metasploitable 2/3
   - DVWA, OWASP Juice Shop, WebGoat (Docker)
   - VulnHub machines
   - Windows 10/11 eval VM + Windows Server eval (for Active Directory later)
4. **Tools:** Docker, Git, VS Code, Burp Suite Community, Wireshark

## Network rules
- Put lab VMs on **Host-Only** or **Internal Network** (never bridged with vulnerable machines)
- Take a **snapshot** of every clean VM

## Accounts to create (all free tiers)
- TryHackMe, Hack The Box, PortSwigger Web Security Academy, PicoCTF, GitHub, HackerOne/Bugcrowd (later)

## Setup checklist
- [ ] Virtualization enabled
- [ ] Kali VM + snapshot
- [ ] Metasploitable VM on host-only network
- [ ] Juice Shop + DVWA running in Docker
- [ ] Burp Suite proxy working with browser
- [ ] Windows eval VM
- [ ] Accounts created

## Quick commands
```bash
# Juice Shop
docker run -d -p 3000:3000 bkimminich/juice-shop
# DVWA
docker run -d -p 8080:80 vulnerables/web-dvwa
# Kali update
sudo apt update && sudo apt full-upgrade -y
```
