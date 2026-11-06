import socket
import struct
import sys
from utils.logger import log_info, log_success, log_error

def packet_sniffer():
    log_info("Starting Packet Sniffer...(Press Ctrl+C to stop)")

    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)
    except PermissionError:
        log_error("Permission denied! Packet sniffer requiers root privileges (run with sudo).")
        return
    except Exception as e:
        log_error(f"Faild to create socket: {e}")
        return

    s.bind(('0.0.0.0', 0))
    s.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    try:
        while True:
            raw_data, addr = s.recvfrom(65535)
            log_success(f"TCP Packet Captured | Source: {addr[0]} | Length: {len(raw_data)} bytes ")

    except KeyboardInterrupt:
        log_info("Packet Sniffer stopped by user.")
        sys.exit(0)