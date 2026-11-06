import socket

class DNSResolver:
    @staticmethod
    def resolve_target(target):
        """
        Resolve a domain name to its corresponding IP address.
        """
        print(f"[*] Resolving target: {target}")
        try:
            ip_address = socket.gethostbyname(target)
            print(f"[+] Target IP Address: {ip_address}")
            return ip_address
        except socket.gaierror as e:
            print(f"[-] Resolution failed: Could not resolve {target}. Check the domain name.")
            return None