import subprocess
import argparse
import re

def GetArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_argument("-m", "--mac", dest="new_mac", help="new MAC address")
    args = parser.parse_args()
    
    if not args.interface:
        parser.error("[-] Please specify an interface, use --help for more info.")
    elif not args.new_mac:
        parser.error("[-] Please specify a MAC address, use --help for more info.")
    
    return args

def ChangeMac(interface, new_mac):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac)
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def GetCurrentMac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode())
    
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address")

options = GetArguments()
current_mac = GetCurrentMac(options.interface)
print("Current MAC =", current_mac)
