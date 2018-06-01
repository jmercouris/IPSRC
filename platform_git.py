##########################################################################
# This file provides an example of the broadcast API using Git           #
##########################################################################

import configparser
from git import Repo


def broadcast_data(encrypted_message):
    """Write the encrypted_message to the git repository
    
    :param encrypted_message: bytes = b'...' a sequence of octets
    :returns:None
    :rtype: None
    
    """
    settings = configparser.ConfigParser()
    settings.read('server_configuration.ini')
    
    repository_path = settings.get('platform-configuration', 'repository-path')
    
    with open("{}/encrypted".format(repository_path), 'wb') as encrypted_ip:
        encrypted_ip.write(encrypted_message)
    
    repo = Repo(repository_path)
    repo.index.add(["{}/encrypted".format(repository_path)])
    repo.index.commit("update")
    
    origin = repo.remote(name='origin')
    origin.push()


def read_data():
    """Read the encrypted IP from the git repository
    
    :returns: returns the encrypted IP
    :rtype: bytes
    
    """
    settings = configparser.ConfigParser()
    settings.read('server_configuration.ini')
    
    repository_path = settings.get('platform-configuration', 'repository-path')
    repo = Repo(repository_path)
    origin = repo.remote(name='origin')
    origin.pull()
    
    with open("{}/encrypted".format(repository_path), 'rb') as encrypted_ip:
        data = encrypted_ip.read()
    
    return data
