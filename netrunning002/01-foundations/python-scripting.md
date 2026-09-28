# Python + Bash for Security (you already know Python — level it up)

## Focus topics
- `socket`, `requests`, `subprocess`, `argparse`, `re`, `json`, `threading`
- File parsing (logs, CSV), regex for log analysis
- HTTP automation with `requests` + `BeautifulSoup`
- Writing small tools: port scanner (lab), subdomain wordlist checker (your own domain), log analyzer, password policy checker
- Libraries to learn: `scapy` (packets), `pwntools` (CTF), `paramiko` (SSH)

## Project ideas (put in `tools/`)
1. Multi-threaded TCP connect scanner (see `tools/port_scanner.py`)
2. SSH auth-log analyzer (see `tools/log_analyzer.py`)
3. Password policy checker (see `tools/password_checker.py`)
4. Simple packet sniffer with scapy (lab only)
5. Web directory checker for **your own** lab apps

## Bash
- One-liners for recon output parsing, loops over IP lists, cron automation

## Resources
- "Black Hat Python" (Seitz) — for concepts, use only in lab
- "Automate the Boring Stuff"
- TryHackMe: Python for Pentesters
