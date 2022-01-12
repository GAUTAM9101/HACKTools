#!/usr/bin/env python

import subprocess
import optparse

parser = optparse.OptionParser()
parser.add_option("-i","--interface", dest="interface", help="Interface to change MAC ADDRESS")
parser.parse_args()

interface = input("Enter the interface :")
new_mac = input("Enter the new MAC address :")

print("Changing MAC address for "+interface+" to "+new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])