import subprocess 
import optparse

def GetArguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="new MAC address")
    return parser.parse_args()
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

(options, arguments) = GetArguments()
ChangeMac(options.interface, options.new_mac)

# how to run the code
# python3 mac_changer.py --interface wlan0 --mac 00:00:00:00:00:11, or
# python3 mac_changer.py -i wlan0 -m 00:00:00:00:00:11