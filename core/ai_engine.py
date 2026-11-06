class AIEngine:
    @staticmethod
    def analyze_ports(open_ports):
        """
        Analyze open ports and provide intelligent security recommendations.
        """
        print("[*] AI Engine analyzing target ports...")
        recommendations = []

        port_checks = {
            21: "[!] Port 21 (FTP) open: Vulnerable to anonymous login or cleartext credentials.",
            22: "[i] Port 22 (SSH) open: Ensure strong authentication & disable root login.",
            23: "[i] Port 23 (Telnet) open: Unencrypted protocol! High security risk.",
            25: "[i] Port 25 (SMTP) open: Mail server detected, check for open relay vulnerabilities.",
            53: "[i] Port 53 (DNS) open: Check for DNS zone transfer (AXFR) vulnerabilities.",
            80: "[i] Port 80 (HTTP) open: Web surface active. Test for web app vulnerabilities.",
            110: "[!] Port 110 (POP3) open: Unencrypted email service detected.",
            139: "[!] Port 139 (NetBIOS) open: File sharing active. Potential internal info disclosure.",
            443: "[i] Port 443 (HTTPS) open: Web surface with SSL/TLS active.",
            445: "[!] Port 445 (SMB) open: High-risk service! Test for WannaCry/EternalBlue exploits.",
            3306: "[i] Port 3306 (MySQL) open: Database service active. Check remote access policies.",
            3389: "[!] Port 3389 (RDP) open: Remote Desktop active. Verify lockout policies & BlueKeep risk."
        }

        for port in open_ports:
            if port in port_checks:
                recommendations.append(port_checks[port])

        if not recommendations:
            recommendations.append("[+] No high-risk standard ports identified by AI engine.")

        return recommendations