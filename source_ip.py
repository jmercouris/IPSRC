#########################################################################
# This file is used on the client to decode the publicly posted IP      #
#########################################################################

import configparser
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

settings = configparser.ConfigParser()
settings.read('client_configuration.ini')
private_key_path = settings.get('private-key', 'path')

# Open the Private Key - the private key of the client computer
private_key = RSA.importKey(open(private_key_path).read(), "***REMOVED***")

cipher = PKCS1_OAEP.new(private_key)

# Write the Encrypted IP to a File - to be uploaded privately
with open("encrypted_ip", 'rb') as encrypted_ip:
    data = encrypted_ip.read()

print(cipher.decrypt(data).decode("utf-8"))
