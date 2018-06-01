##############################################################
# Using the disk as medium for broadcasting/reading the data #
##############################################################


def broadcast_data(encrypted_message):
    """Write the encrypted_message to a file
    
    :param encrypted_message: bytes = b'...' a sequence of octets
    :returns:None
    :rtype: None
    
    """
    with open("encrypted_ip", 'wb') as encrypted_ip:
        encrypted_ip.write(encrypted_message)


def read_data():
    """Read the encrypted IP from disk
    
    :returns: returns the encrypted IP
    :rtype: bytes
    
    """
    
    with open("encrypted_ip", 'rb') as encrypted_ip:
        data = encrypted_ip.read()
    return data
