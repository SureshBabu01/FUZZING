import socket
import threading

target = "scanme.nmap.org"
ports = range(20, 1025)  
timeout = 1.0

print_lock = threading.Lock()

def scan_port(port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        s.connect((target, port))
        try:
            banner = s.recv(1024).decode().strip()
        except:
            banner = "No banner"
        with print_lock:
            print(f"[+] Port {port} is open - {banner}")
        s.close()
    except:
        pass  

threads = []

for port in ports:
    t = threading.Thread(target=scan_port, args=(port,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Scan completed.")
