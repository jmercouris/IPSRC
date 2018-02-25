import argparse
import ast
import configparser

import Crypto
from Crypto import Random
from Crypto.PublicKey import RSA

settings = configparser.ConfigParser()
settings.read('server_configuration.ini')

public_key_path = settings.get('public-key', 'path')

with open(public_key_path, 'r') as myfile:
    public_key = myfile.read().replace('\n', '')

print(public_key)
