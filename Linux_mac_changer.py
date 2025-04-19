# ============Importing the libraries========================
# this is the library for parse the option from the user
import optparse
# this is the library for execute the command in the terminal
import subprocess
# this is the library for use the regular expression to get the mac address from the ifconfig command
import re


# this func for get the arg from the user
def get_arguments():
    # thats the class to Parse the option and here we do the parser var to content them
    parser = optparse.OptionParser() 
    # the help var here for describe the option when i write the --help option in our programm 
    parser.add_option('-i','--interface' ,dest='interface' , help='Interface to Change Its MAC') # add the first option in our program 
    parser.add_option('-m','--mac' ,dest='new_mac' , help='New MAC address') 
    (options,arguments) = parser.parse_args() # here we return  the option the user is intered in the option var and the argument in the argument var

    if not options.interface : # if the interface option is not or its not writen show this message
        parser.error('[-] Please Specify an interface , use --help to more info.')
    elif not options.new_mac:# if the new_mac options is not or its not writen show this message
        parser.error('[-] Please Specify a new_mac , use --help to more info.') 
    return options       
                                                                       
# this func for change the mac
def change_mac(interface , new_mac): 

    print("[+] Changing MAC address for " + interface + " to " + new_mac)
    # execute the command to change the mac
    subprocess.call(['ifconfig' , interface , 'down'])
    subprocess.call(['ifconfig' , interface , 'hw' , 'ether' , new_mac])
    subprocess.call(['ifconfig' , interface , 'up'])

    # here we check if the command is executed or not and show the message to the user
def get_current_mac(interface):
    try:
        # Execute the 'ifconfig' command to get information about the network interface
        # The 'stderr=subprocess.STDOUT' option redirects error messages to the standard output stream
        ifconfig_result = subprocess.check_output(["ifconfig", interface], stderr=subprocess.STDOUT, universal_newlines=True)
     
    except subprocess.CalledProcessError as e:  
        print(f"Error: Unable to get MAC address for interface {interface}")
        print(f"Command output: {e.output.strip()}")
        return None


    mac_address_search_result = re.search(r'\w\w:\w\w:\w\w:\w\w:\w\w:\w\w', ifconfig_result)
    if mac_address_search_result: 
        return mac_address_search_result.group(0)
    else:
        print(f"[-] Could not read the MAC address for interface {interface}")
        return None

options = get_arguments()
current_mac=get_current_mac(options.interface)

if current_mac is None:
    print(f"[-] Could not read the MAC address for interface {options.interface}")
    exit(1)
if current_mac == options.new_mac:
    print(f"[-] The MAC address is already set to {current_mac}. No changes needed.")
    exit(0)

print('Current MAC = ', current_mac)

change_mac(options.interface , options.new_mac) 

current_mac=get_current_mac(options.interface)

if current_mac == options.new_mac:
    print('[+] The MAC address successfully changed to '+ current_mac)
else:
    print('[-] MAC address did not get changed ')    
