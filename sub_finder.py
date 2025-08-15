import socket

9get_domain = "example.com"  
wordlist = ["www", "mail", "ftp", "test", "dev", "api"]  

print(f"[*] Starting subdomain scan on {target_domain}\n")

for sub in wordlist:
    subdomain = f"{sub}.{target_domain}"
    try:
        ip = socket.gethostbyname(subdomain)
        print(f"[+] Found: {subdomain} --> {ip}")
    except socket.gaierror:
        pass  

print("\n[*] Scan complete.")
