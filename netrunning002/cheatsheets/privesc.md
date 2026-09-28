# Privesc Quick Checklist

## Linux
- `sudo -l`, SUID (GTFOBins), writable /etc/passwd, cron jobs, PATH abuse, kernel version (searchsploit)
- Run LinPEAS, review manually

## Windows
- `whoami /priv`, `systeminfo`, unquoted service paths, AlwaysInstallElevated, scheduled tasks
- Run WinPEAS/PowerUp, review manually
