import subprocess
import argparse
import re

def change_mac(interface, new_mac):
    print(f"Changing MAC address of {interface} to {new_mac}")

    subprocess.call(["sudo", "ifconfig", interface, "down"])
    subprocess.call(["sudo", "ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["sudo", "ifconfig", interface, "up"])

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface]).decode('utf-8')
    mac_address_search_result = re.search(r"(\w\w:\w\w:\w\w:\w\w:\w\w:\w\w)", ifconfig_result)
    
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print("Could not read MAC address.")
        return None

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MAC address spoofer")
    parser.add_argument("interface", help="Interface to change its MAC address")
    parser.add_argument("new_mac", help="New MAC address")

    args = parser.parse_args()

    current_mac = get_current_mac(args.interface)
    print(f"Current MAC address: {current_mac}")

    change_mac(args.interface, args.new_mac)

    current_mac = get_current_mac(args.interface)
    if current_mac == args.new_mac:
        print(f"MAC address successfully changed to {current_mac}")
    else:
        print("MAC address did not get changed.")
