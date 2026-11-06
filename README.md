# Nexis 🚀
A Modular Network Reconnaissance & Analysis Toolkit built with Python.


Nexis is a lightweight, command-line network security tool designed for fast TCP scanning, DNS resolution, and packet sniffing.

**Developed by: Zineddine Mouri | #BuildInPublic**

---

## 🛠 Features

- 🟢 *TCP Port Scanner* (scanner.py): Multi-threaded port scanner for target verification.
- 🟢 *Network Packet Sniffer* (sniffer.py): Live TCP packet capturing using raw sockets.
- 🟢 *DNS Resolver* (resolver.py): Quick domain-to-IP resolution and target diagnostics.
- 🟡 *AI Analysis Engine* (ai_engine.py): (In Development) Smart packet and vulnerability pattern analysis.

---

## 📥 Installation

Clone the repository and run the automated installer:

```bash
git clone https://github.com/your-username/Nexis.git
cd Nexis
chmod +x install.sh
sudo bash install.sh

---

## 💻 Usage

Once installed, *Nexis* can be executed globally from any terminal directory.

```bash
# Display Help Menu
nexis -h

# Run Port Scanner
nexis -t [target_ip] -p 1-1000

# Start Packet Sniffer (Requires Root)
sudo nexis -s

# Resolve Domain to IP (DNS Recon)
nexis -d [target_domain] 

#Run Port Scanner with AI Security Analysis
nexis -t [target_ip] -p 1-1000 -ai