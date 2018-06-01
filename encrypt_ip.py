#########################################################################
# This file is used on the Server for the Server to encrypt its IP      #
#########################################################################

import ipgetter
import configparser
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def encrypt_ip():
    """This function will encrypt a message using the users public key and
    return a set of bytes representing the encrypted IP
    
    :returns: The IP Address of the machine calling this function, encrypted
    :rtype: bytes = b'...' a sequence of octets
    
    """
    settings = configparser.ConfigParser()
    settings.read('server_configuration.ini')
    public_key_path = settings.get('public-key', 'path')
    
    # Open the Public Key - the public key of the client computer
    public_key = RSA.importKey(open(public_key_path).read())
    
    cipher = PKCS1_OAEP.new(public_key)
    
    message = ipgetter.myip()
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    
    return encrypted_message


def write_to_disk(encrypted_message):
    """Write the encrypted_message to a file
    
    :param encrypted_message: bytes = b'...' a sequence of octets
    :returns:None
    :rtype: None
    
    """
    with open("encrypted_ip", 'wb') as encrypted_ip:
        encrypted_ip.write(encrypted_message)


if __name__ == "__main__":
    write_to_disk(encrypt_ip())
