#########################################################################
# This file is used on the client to decode the publicly posted IP      #
#########################################################################

import getpass

import configparser
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def decrypt_ip(data, passphrase):
    """This function will decrypt a message using the users private key
    and return a string of their IP Address
    
    :param data: The data to decrypt
    :param passphrase: the RSA private key passphrase
    
    :returns: The decrypted IP Address
    :rtype: String
    
    """
    settings = configparser.ConfigParser()
    settings.read('client_configuration.ini')
    private_key_path = settings.get('private-key', 'path')
    
    # Open the Private Key - the private key of the client computer
    private_key = RSA.importKey(open(private_key_path).read(), passphrase)
    
    cipher = PKCS1_OAEP.new(private_key)
    
    return cipher.decrypt(data).decode("utf-8")


def read_from_disk():
    """Read the encrypted IP from disk
    
    :returns: returns the encrypted IP
    :rtype: bytes
    
    """
    
    with open("encrypted_ip", 'rb') as encrypted_ip:
        data = encrypted_ip.read()
    return data


if __name__ == "__main__":
    print(decrypt_ip(read_from_disk(), getpass.getpass()))
