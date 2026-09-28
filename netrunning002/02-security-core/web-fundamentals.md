# Web Fundamentals & OWASP Top 10

## Web basics
- HTTP methods, headers, cookies (HttpOnly, Secure, SameSite), CORS, CSP, same-origin policy
- Sessions, JWT, OAuth flows, REST/GraphQL, WebSockets
- Frontend (HTML/JS/DOM) and backend (SQL, templates, file handling)

## OWASP Top 10 (learn each: cause → exploit in lab → fix)
1. Broken Access Control (IDOR, privilege escalation)
2. Cryptographic Failures
3. Injection (SQLi, command injection, XSS in older lists)
4. Insecure Design
5. Security Misconfiguration
6. Vulnerable & Outdated Components
7. Identification & Authentication Failures
8. Software & Data Integrity Failures
9. Logging & Monitoring Failures
10. SSRF

## Labs
- **PortSwigger Web Security Academy** (free, best resource): SQLi, XSS, CSRF, auth, access control, SSRF, file upload, path traversal
- Juice Shop + DVWA locally
- TryHackMe: OWASP Top 10, Burp Suite, Web Fundamentals

## Tools
- Burp Suite Community, browser dev tools, `curl`, ffuf (for your own lab targets)
