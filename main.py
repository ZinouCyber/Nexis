#!/usr/bin/env python3
import argparse
import sys
from core.scanner import run_port_scanner
from core.sniffer import packet_sniffer
from core.resolver import DNSResolver
from core.ai_engine import AIEngine
from utils.logger import print_banner, log_error, log_info

def main():
    parser = argparse.ArgumentParser(
        description="Nexis - Advanced Network Recon & Protocol Analysis Toolkit"
    )

    parser.add_argument("-t", "--target", help="Target IP address for port scanning")
    parser.add_argument("-p", "--ports", help="Ports range, e.g., 1-1000 (default: 1-1024)")
    parser.add_argument("-s", "--sniff", action="store_true", help="Start packet sniffer mode")
    parser.add_argument("-d", "--domain", help="Target domain name to resolve into IP" )
    parser.add_argument("-ai", "--analyze", action="store_true", help="Run AI security analysis on open ports")

    args = parser.parse_args()

    print_banner()

    if args.sniff:
        packet_sniffer()

    elif args.target:
        ports = args.ports if args.ports else "1-1024"
        try:
            if "-" in ports:
                start, end = map(int, ports.split("-"))
            else:
                start = end = int(ports)
        except ValueError:
            log_error("Invalid port range format. Use format like 1-1000 or 80.")
            sys.exit(1)
            
        open_ports = run_port_scanner(args.target, start, end)

        if args.analyze and open_ports:
            print("\n[*] Running AI Analysis Engine on open ports...")
            recommendations = AIEngine.analyze_ports(open_ports)
            for rec in recommendations:
                print(rec)
        elif args.analyze and not open_ports:
            print("\n[+] AI Analysis: No open ports found to analyze.")

    elif args.domain:
        ip = DNSResolver.resolve_target(args.domain)
        if not ip:
            sys.exit(1)
    else:
        log_error("No mode selected! Use -t for scanning or -s for sniffing, or -d for domain resolution.")
        parser.print_help()
        sys.exit(1)

if __name__ == "__main__":
    main()