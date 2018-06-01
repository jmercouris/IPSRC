##############################################################################
# This file provides an example of the broadcast API one must follow.        #
# One must implement two functions, broadcast_data, and read_data. These     #
# two functions will allow the server and the client to broadcast            #
# and source the data they need.                                             #
#                                                                            #
# The user will also need to update platform_disk to include new information #
# about the broadcast and read functions                                     #
##############################################################################


def broadcast_data(encrypted_message):
    """Write the encrypted_message to disk
    
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
