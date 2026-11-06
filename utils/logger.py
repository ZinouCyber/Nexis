import sys

def print_banner():
    banner = r"""
  _  _           _      
 | \| |_____  () _  
 | .` / -_\ \/ / | ' \ 
 |_|\_\___/_/\_\_|_||_|
                         
    """
    print("=" * 55)
    print(banner)
    print(" [*] Nexis - Advanced Network & Protocol Toolkit")
    print(" [*] Developed by Zineddine Mouri | #BuildInPublic")
    print("=" * 55)

def log_info(message):
    print(f"[*] {message}")

def log_success(message):
    print(f"[+] {message}")

def log_error(message):
    print(f"[!] {message}", file=sys.stderr)