!/bin/bash

# Script to randomize the MAC address of interface wlo1
# Requires sudo privileges and macchanger installed

INTERFACE="wlo1"

echo "Bringing down the network interface: $INTERFACE"
sudo ip link set $INTERFACE down

echo "Randomizing MAC address..."
sudo macchanger -r $INTERFACE

echo "Bringing up the network interface: $INTERFACE"
sudo ip link set $INTERFACE up

echo "New MAC address:"
ip link show $INTERFACE | grep link/ether

echo "MAC address successfully randomized."
