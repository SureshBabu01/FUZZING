# EX : python3 argv_scanner.py google.com 20 100

import socket
import sys

def scan_ports(host, start_port, end_port):
    print(f"\nScanning {host} from port {start_port} to {end_port}...\n")
    for port in range(start_port, end_port + 1):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        try:
            s.connect((host, port))
            print(f"[+] Port {port} is OPEN")
        except socket.error:
            pass
        finally:
            s.close()

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python scanner.py <host> <start_port> <end_port>")
        sys.exit(1)
    target_host = sys.argv[1]
    start = int(sys.argv[2])
    end = int(sys.argv[3])
    scan_ports(target_host, start, end)
