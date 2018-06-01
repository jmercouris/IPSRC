#########################################################################
# This file is used on the Server for the Server to encrypt its IP and  #
# post it publicly online.                                              #
#########################################################################

import ipgetter
import configparser
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

settings = configparser.ConfigParser()
settings.read('server_configuration.ini')
public_key_path = settings.get('public-key', 'path')

# Open the Public Key - the public key of the client computer
public_key = RSA.importKey(open(public_key_path).read())

cipher = PKCS1_OAEP.new(public_key)

message = ipgetter.myip()
encrypted_message = cipher.encrypt(message.encode("utf-8"))

# Write the Encrypted IP to a File - to be uploaded publicly
with open("encrypted_ip", 'wb') as encrypted_ip:
    encrypted_ip.write(encrypted_message)
