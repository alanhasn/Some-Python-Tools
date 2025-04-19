#!/usr/bin/env python
import scapy.all as scapy 
import argparse

def get_argument():
    parse = argparse.ArgumentParser()
    parse.add_argument('-t' , '--target', dest='target' , help='Target IP / IP range.')
    option = parse.parse_args()
    return option
    

def scan(ip):
    # ARP request to find the MAC address of the target IP
    arp_requast = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_requast_broadcast = broadcast/arp_requast
    # Send the ARP request and wait for a response
    # The srp function sends and receives packets at layer 2 (Ethernet)
    answered_list = scapy.srp(arp_requast_broadcast , timeout=1,verbose=False)[0] 

    client_list = []
    # answered_list is a list of tuples (sent_packet, received_packet)
    # Loop through the answered_list to extract IP and MAC addresses
    for element in answered_list:
        # element[1].psrc is the source IP address of the response
        # element[1].hwsrc is the source MAC address of the response
        client_dict = {'ip':element[1].psrc,'mac': element[1].hwsrc } 
        client_list.append(client_dict)
    return client_list

# Print the result in a readable format
def print_result(result_list):
    print('IP\t\t\t MAC Address\n------------------------------------')
    for client in result_list:
        print(client['ip'] + '\t\t' +client['mac'])


# Main function to execute the script
if __name__ == '__main__':
    option = get_argument() 
    scan_result=scan(option.target)
    print_result(scan_result)
