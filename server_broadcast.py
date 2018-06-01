from platform_disk import broadcast_data
from cryptography import encrypt_ip
import configparser

if __name__ == "__main__":
    settings = configparser.ConfigParser()
    settings.read('server_configuration.ini')
    public_key_path = settings.get('public-key', 'path')
    
    broadcast_data(encrypt_ip(public_key_path))
