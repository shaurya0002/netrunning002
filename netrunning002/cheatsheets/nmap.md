# Nmap Cheat Sheet

```bash
nmap -sn 192.168.1.0/24                 # host discovery (ping sweep)
nmap -p- <target>                       # all 65535 ports
nmap -sC -sV -p<ports> <target>         # default scripts + version detect
nmap -A <target>                        # aggressive (OS, version, scripts, traceroute)
nmap --script vuln <target>             # vuln-detection scripts
nmap -sU --top-ports 20 <target>        # top UDP ports
nmap -oA output <target>                # save all formats
```
Only run against systems you're authorized to test.
