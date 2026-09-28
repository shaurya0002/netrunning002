# Offensive: Reconnaissance & Enumeration

## Passive recon
- OSINT: whois, DNS records, Shodan, Google dorking, certificate transparency (crt.sh)
- Subdomain enumeration: subfinder, amass (on **your own domain or authorized scope only**)

## Active recon
- Port scanning: `nmap -sC -sV -p- <target>` (lab targets only)
- Service enumeration: SMB (`enum4linux`, `smbclient`), HTTP (`gobuster`/`ffuf` for dirs), SNMP, FTP anonymous login
- Banner grabbing with `nc`/`nmap` scripts

## Practice
- TryHackMe: Nmap, Network Services 1&2, Vulnversity
- Full recon against Metasploitable in your lab, document every open port/service

## Cheat sheet → see `cheatsheets/nmap.md`
