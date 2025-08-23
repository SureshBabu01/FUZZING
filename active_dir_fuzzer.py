import requests
import threading
from queue import Queue

print("Tool try to fuzz and get active directory..........")
target_url = "http://testphp.vulnweb.com" 
wordlist_file = "common.txt"  
num_threads = 10

q = Queue()

def fuzz_directory():
    while not q.empty():
        dir_name = q.get()
        url = f"{target_url}/{dir_name}"
        try:
            r = requests.get(url, timeout=3)
            if r.status_code in [200, 301, 302, 403]:
                print(f"[{r.status_code}] Found: {url}")
        except requests.RequestException:
            pass
        finally:
            q.task_done()

with open(wordlist_file, "r") as f:
    for line in f:
        q.put(line.strip())

threads = []
for _ in range(num_threads):
    t = threading.Thread(target=fuzz_directory)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Directory fuzzing completed.")
