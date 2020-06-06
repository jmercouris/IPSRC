######################################################################################
#  This file contains functions which are used to encrypt and decrypt the server ip  #
######################################################################################

from ipgetter2 import ipgetter1 as ipgetter
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def encrypt_ip(public_key_path):
    """This function will encrypt a message using the users public key and
    return a set of bytes representing the encrypted IP
    
    :returns: The IP Address of the machine calling this function, encrypted
    :rtype: bytes = b'...' a sequence of octets
    
    """
    # Open the Public Key - the public key of the client computer
    public_key = RSA.importKey(open(public_key_path).read())
    cipher = PKCS1_OAEP.new(public_key)
    message = ipgetter.myip()
    encrypted_message = cipher.encrypt(message.encode("utf-8"))
    
    return encrypted_message


def decrypt_ip(private_key_path, data, passphrase):
    """This function will decrypt a message using the users private key
    and return a string of their IP Address
    
    :param data: The data to decrypt
    :param passphrase: the RSA private key passphrase
    
    :returns: The decrypted IP Address
    :rtype: String
    
    """
    # Open the Private Key - the private key of the client computer
    private_key = RSA.importKey(open(private_key_path).read(), passphrase)
    cipher = PKCS1_OAEP.new(private_key)
    
    return cipher.decrypt(data).decode("utf-8")
