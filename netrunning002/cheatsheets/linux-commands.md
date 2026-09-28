# Linux Quick Reference

```bash
find / -perm -4000 2>/dev/null          # SUID binaries
sudo -l                                 # sudo permissions
cat /etc/crontab; ls -la /etc/cron*     # cron jobs
netstat -tulpn / ss -tulpn              # listening ports
ps aux --sort=-%mem | head              # top processes
grep -r "password" /etc 2>/dev/null     # quick secret grep (lab)
```
