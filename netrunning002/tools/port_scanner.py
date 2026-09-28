"""
Simple multi-threaded TCP connect port scanner.
FOR USE ONLY AGAINST HOSTS YOU OWN OR ARE AUTHORIZED TO TEST (e.g. your own lab VMs).
Usage: python port_scanner.py <target_ip> <start_port> <end_port>
"""
import socket
import sys
import threading
from queue import Queue

def scan_port(target, port, open_ports, lock):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.5)
            if s.connect_ex((target, port)) == 0:
                with lock:
                    open_ports.append(port)
    except socket.error:
        pass

def worker(q, target, open_ports, lock):
    while not q.empty():
        port = q.get()
        scan_port(target, port, open_ports, lock)
        q.task_done()

def main():
    if len(sys.argv) != 4:
        print("Usage: python port_scanner.py <target_ip> <start_port> <end_port>")
        sys.exit(1)

    target, start, end = sys.argv[1], int(sys.argv[2]), int(sys.argv[3])
    print(f"Scanning {target} ports {start}-{end} (lab use only)...")

    q = Queue()
    for p in range(start, end + 1):
        q.put(p)

    open_ports = []
    lock = threading.Lock()
    threads = [threading.Thread(target=worker, args=(q, target, open_ports, lock)) for _ in range(100)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("Open ports:", sorted(open_ports) if open_ports else "None found")

if __name__ == "__main__":
    main()
