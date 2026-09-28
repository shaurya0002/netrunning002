# Privilege Escalation

## Linux
- Enumeration: `sudo -l`, SUID binaries (GTFOBins), cron jobs, writable services, PATH hijacking, kernel exploits (last resort)
- Automate first pass with LinPEAS, then verify manually

## Windows
- `whoami /priv`, unquoted service paths, weak service permissions, AlwaysInstallElevated, scheduled tasks, stored credentials
- Automate first pass with WinPEAS/PowerUp, then verify manually

## Practice
- TryHackMe: Linux PrivEsc, Windows PrivEsc, Common Linux Privesc
- HTB Easy/Medium boxes, always try manual enumeration before running automated scripts blind

## Cheat sheet → `cheatsheets/privesc.md`
