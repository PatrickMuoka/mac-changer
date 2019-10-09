#!usr/bin/env python3

import subprocess
import optparse


def argument_parser():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="mac", help="Add new MAC address")
    return parser.parse_args()


def mac_changer(interface, mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac])
    subprocess.call(["ifconfig", interface, "up"])


(option, argument) = argument_parser()
mac_changer(option.interface, option.mac)
