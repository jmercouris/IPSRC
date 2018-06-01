##########################################################################
# This file provides an example of the broadcast API using Git           #
##########################################################################


def broadcast_data(encrypted_message):
    """Write the encrypted_message to the git repository
    
    :param encrypted_message: bytes = b'...' a sequence of octets
    :returns:None
    :rtype: None
    
    """
    with open("encrypted_ip", 'wb') as encrypted_ip:
        encrypted_ip.write(encrypted_message)


def read_data():
    """Read the encrypted IP from the git repository
    
    :returns: returns the encrypted IP
    :rtype: bytes
    
    """
    with open("encrypted_ip", 'rb') as encrypted_ip:
        data = encrypted_ip.read()
    return data
