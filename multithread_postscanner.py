import socket
import threading
import sys

def scan_port(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)  
        s.connect((host, port))
        print(f"[+] Port {port} is OPEN")
        s.close()
    except (socket.timeout, socket.error):
        pass  

if len(sys.argv) != 4:
    print(f"Usage: python {sys.argv[0]} <host> <start_port> <end_port>")
    sys.exit(1)

host = sys.argv[1]
start_port = int(sys.argv[2])
end_port = int(sys.argv[3])

print(f"Scanning host {host} from port {start_port} to {end_port}...\n")

threads = []

for port in range(start_port, end_port + 1):
    t = threading.Thread(target=scan_port, args=(host, port))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("\nScan complete.")
