"""
Simple auth-log analyzer: flags repeated failed SSH login attempts (brute-force indicator).
Usage: python log_analyzer.py /path/to/auth.log
Run against YOUR OWN system logs (e.g. your lab VM's /var/log/auth.log).
"""
import sys
import re
from collections import Counter

FAILED_RE = re.compile(r"Failed password for (invalid user )?(\S+) from (\S+)")

def analyze(path, threshold=5):
    ip_counts = Counter()
    user_counts = Counter()

    with open(path, "r", errors="ignore") as f:
        for line in f:
            m = FAILED_RE.search(line)
            if m:
                user, ip = m.group(2), m.group(3)
                ip_counts[ip] += 1
                user_counts[user] += 1

    print("=== Suspicious IPs (>= threshold failed logins) ===")
    for ip, count in ip_counts.most_common():
        if count >= threshold:
            print(f"{ip}: {count} failed attempts")

    print("\n=== Most targeted usernames ===")
    for user, count in user_counts.most_common(10):
        print(f"{user}: {count}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python log_analyzer.py <path_to_auth_log>")
        sys.exit(1)
    analyze(sys.argv[1])
