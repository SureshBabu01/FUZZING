import socket

target = "scanme.nmap.org"          
ports = [21, 22, 23, 25, 53, 80, 110, 143, 443, 8080] 
timeout = 1                  

print(f"[*] Starting port scan on {target}\n")

for port in ports:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout)
    try:
        s.connect((target, port))
        print(f"[+] Port {port} is OPEN")
        s.close()
    except (socket.timeout, socket.error):
        pass  

print("\n[*] Scan complete.")
