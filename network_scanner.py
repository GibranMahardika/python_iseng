import scapy.all as scapy

def scan(ip):
    # scapy.arping(ip)
    arp_request = scapy.ARP(pdst=ip)
    scapy.ls(scapy.ARP())
    print(arp_request.summary())
    arp_request.show()

    print("\nBroadcast ================================= \n")

    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    scapy.ls(scapy.Ether())
    print("\n",broadcast.summary())
    broadcast.show()

    print("\nARP and Broadcast ================================= \n")

    arp_request_broadcast = broadcast/arp_request
    print("\n", arp_request_broadcast.summary())
    arp_request_broadcast.show()
    
    print("\nSending Packets ================================= \n")
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    # print(answered_list.summary())

    print("IP\t\t\tMac Address\n-----------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)
        # print(element[1].hwsrc)
        # print(" ----------------------------------")


    # print("\nShow the detail ================================= \n")

    # arp_request.show()
    # broadcast.show()
    # arp_request_broadcast.show()


scan("192.168.1.0/24")