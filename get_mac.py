from napalm import get_network_driver
from napalm.base.exceptions import ConnectionException
import sys

def get_mac(ip_addr):
    
    username,password = input("\nUsername:\n"),input("Password:\n")

    print("Attempting to connect to {}".format(ip_addr))

    try:
    
        driver = get_network_driver('ios')
        ios = driver(ip_addr, username, password)
        ios.open()

    except ConnectionException:

        print("Unable to connect to device {}".format(ip_addr))
        sys.exit()

    print("Connection to {} successful".format(ip_addr))

    ios_output = ios.get_mac_address_table()
    mac_addresses, interfaces = [a_dict['mac'] for a_dict in ios_output], [a_dict['interface'] for a_dict in ios_output]
    data = dict(zip(mac_addresses, interfaces))

    print("Data retrieved successfully")
    
    return data