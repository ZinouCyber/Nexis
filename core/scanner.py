import socket
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_port(target_ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target_ip, port))
        if result == 0:
            try:
                service = socket.getservbyport(port, "tcp")
            except OSError:
                service = "unknown"
            print(f"[+] Port {port:<5} IS OPEN ({service})", flush=True)
        s.close()
        return port
    except Exception:
        pass
    return None

def run_port_scanner(target_ip, start_port=1, end_port=1024):
    print(f"[*] Starting port scan on {target_ip} (Ports: {start_port}-{end_port})...", flush=True)
    open_ports = []

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = {executor.submit(scan_port, target_ip, port): port for port in range(start_port, end_port + 1) }

        for future in as_completed(futures):
            port = future.result()
            if port:
                open_ports.append(port)

    print("[*] Port scanning completed.")
    return sorted(open_ports)