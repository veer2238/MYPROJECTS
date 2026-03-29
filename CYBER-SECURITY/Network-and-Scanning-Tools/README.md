# Network & Scanning Tools

This section covers essential tools used for network scanning, traffic analysis, and debugging connections in cyber security.

---

## Disclaimer
Use these tools only in authorized lab environments or systems you have explicit permission to test.

---

## Tools Covered
- Nmap
- Wireshark
- Netcat

---

# 1. Nmap (Network Mapper)

## Description
Nmap is a powerful tool used for network discovery and port scanning to identify open ports, services, and vulnerabilities.

---

## Key Features
- Port scanning  
- Service detection  
- OS detection  
- Network mapping  

---

## Basic Commands

### Scan a Single Host
```bash
nmap 192.168.1.1




Scan Multiple Ports

nmap -p 1-1000 192.168.1.1


Service Version Detection
nmap -sV 192.168.1.1

OS Detection
nmap -O 192.168.1.1


Example

nmap -sV scanme.nmap.org


2. Wireshark
Description
Wireshark is a network protocol analyzer used to capture and inspect packets in real-time.
Key Features
Live packet capture
Protocol analysis
Filter traffic
Detect suspicious activity
Basic Usage
Open Wireshark
Select network interface (WiFi/Ethernet)
Start capture
Apply filters
Common Filters
http
tcp.port == 80
ip.addr == 192.168.1.1
Example Use Case
Capture login request
Analyze headers
Identify sensitive data


3. Netcat (nc)
Description
Netcat is a versatile networking tool used for connection testing, port listening, and data transfer.
Key Features
Port scanning
Banner grabbing
Debugging network services
Basic Commands
Start Listener
nc -lvp 4444
Connect to Server
nc 192.168.1.1 4444
Banner Grabbing
nc example.com 80
Example
nc scanme.nmap.org 80
Then type:
GET / HTTP/1.1
Host: scanme.nmap.org


Practice Questions

Scan your local network using Nmap
Identify open ports on a target system
Capture network traffic using Wireshark
Use Nmap to detect services (-sV)
Apply filters in Wireshark to find HTTP traffic
Use Netcat to connect to an open port
Perform full network scan (nmap -A)
Analyze captured packets to find login data
Use Netcat for banner grabbing


Theory Questions
What is port scanning?
Difference between TCP and UDP?
What is packet sniffing?
How does Nmap detect services?
What are risks of open ports?
