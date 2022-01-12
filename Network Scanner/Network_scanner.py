#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request = scapy.ARP(pdst=ip) # Sends ARP request
    #scapy.ls(scapy.ARP)
    #print(arp_request.summary())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    #print(broadcast.summary())
    arp_request_broadcast = broadcast/arp_request
    #arp_request_broadcast.show()
    answered_list= scapy.srp(arp_request_broadcast,timeout=1,verbose=False)[0]
    #print(answered_list.summary())

    clients_list = []
    for i in answered_list:
        client_dict = {"ip": i[1].psrc, "mac": i[1].hwsrc}
        clients_list.append(client_dict)
        #print(i[1].psrc + "\t\t" + i[1].hwsrc)
        #print("---------------------------------------------------")
    return(clients_list)
def print_result(results_List):
    print("IP\t\t\tMAC_ADDRESS\n-------------------------------------")
    for client in results_List:
        print(client["ip"] + "\t\t" + client["mac"])

scan_result = scan("10.0.2.1/24")
print_result(scan_result)