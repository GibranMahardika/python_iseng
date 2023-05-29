import subprocess 
import optparse
import re

def GetArguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        # code to handle error
        parser.error("[-] Please specify an interface, use --help for some more info.")
    elif not options.new_mac:
        # code to handle error
        parser.error("[-] Please specify a mac, use --help for some more info.")
    return options
    # NOTES = = = = = = = =
    # the option variable is going to contain values of wlan0 and 00:11:22:33:44:55
    # the option variable is contains the values of the user inputs
    # the arguments variable is going contain --interface --mac

def ChangeMac(interface, new_mac):
    print("[+] Changin MAC Address for " + interface + " to " + new_mac)
    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

# v1
# interface = input("interface > ")
# new_mac = input("new MAC > ")

# v2
# interface = options.interface
# new_mac = options.new_mac

def GetCurrentMac(interface):
    ifconfig_result = subprocess.check_output(["sudo","ifconfig", interface])
    # options.interface is an argument

    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("[-] Could not read MAC address")

options = GetArguments()

current_mac = GetCurrentMac(options.interface)
print("Current MAC = " + str(current_mac))

ChangeMac(options.interface, options.new_mac)

current_mac = GetCurrentMac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully change to " + current_mac)
else:
    print("[-] MAC address did not get changed.")
# how to run the code
# python3 mac_changer.py --interface wlan0 --mac 00:00:00:00:00:11, or
# python3 mac_changer.py -i wlan0 -m 00:00:00:00:00:11