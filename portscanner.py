import socket
import termcolor

def scan(target, ports):
    for port in range(1, ports):
        scan_port(target, port)

def scan_port(ipaddress, port):
    try:
        sock = socket.socket()
        sock.connect((ipaddress, port))
        print("[+] Port Opened" + str(port))
        sock.close()
    except:
        pass

targets = input("[*] Enter Targets to Scan (spit them by ,): ")
ports = int(input("[*] Enter how many Ports you want to Scan: "))
if ',' in targets:
    print("[*] Scanning multiple targets")
    for ip_addr in targets.spit(','):
        scan(ip_addr.strip(' '), ports)
else:
    scan(targets,ports)