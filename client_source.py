#########################################################################################
# This file is used on the client to source the encrypted IP address from the internet. #
# You can change the way the IP sourced by change the import below "platform_disk" to   #
# any medium that you would like to use.                                                #
#########################################################################################

import getpass
from platform_constants import get_read_function
from cryptography import decrypt_ip
import configparser

if __name__ == "__main__":
    settings = configparser.ConfigParser()
    settings.read('client_configuration.ini')
    private_key_path = settings.get('private-key', 'path')
    
    platform_type = settings.get('platform-configuration', 'type')
    read_function = get_read_function(platform_type)
    
    print(decrypt_ip(private_key_path, read_function(), getpass.getpass()))
