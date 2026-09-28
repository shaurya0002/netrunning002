# Defensive Security Basics (Phase 4-ish, run alongside offensive)

## Why bother if I want to be a "hacker"
Every good pentester understands defense — you'll be tested on it (interviews, OSCP-adjacent roles), and blue team roles are easier to break into first.

## Topics
- Log sources: Windows Event Logs, Linux syslog/auth.log, firewall/IDS logs
- SIEM concept (Splunk free tier / ELK stack), basic detection rules
- IDS/IPS: Snort/Suricata basics
- Incident response phases: Prep, Identification, Containment, Eradication, Recovery, Lessons Learned
- Detecting the attacks you learned in `03-offensive/` (this pairing is the fastest way to learn both)

## Practice
- TryHackMe: SOC Level 1 path, Intro to SIEM, Splunk basics
- Set up ELK or Splunk free in a VM, feed it logs from your attack lab, find your own attacks in the logs

## Certs adjacent
Security+ overlaps heavily here.
