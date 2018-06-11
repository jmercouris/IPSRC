##########################################
# This file provides broadcast over MQTT #
##########################################
"""
    Author: David Young <github: ohnoitsyou>

    MQTT requires the following platform-configuration variables

    host: The hostname of the MQTT broker
    username: the username to use to connect to the broker
    password: the password to use to connect to the broker (Optional: defaults to None)
    channel: the channel on which the password will be writen / read from
"""
import configparser
import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe


def broadcast_data(encrypted_message):
    """Write the encrypted_message to the MQTT broker on the selected channel

    :param encrypted_message: bytes = b'...' a sequence of octets
    :returns: None
    :rtype: None

    """
    settings = configparser.ConfigParser({'password': None})
    settings.read('server_configuration.ini')

    mqtt_host = settings.get('platform-configuration', 'host')
    mqtt_username = settings.get('platform-configuration', 'username')
    mqtt_password = settings.get('platform-configuration', 'password')
    mqtt_channel = settings.get('platform-configuration', 'channel')

    auth = {'username': mqtt_username, 'password': mqtt_password}
    publish.single(mqtt_channel, payload=encrypted_message,
                   auth=auth, hostname=mqtt_host, retain=True)


def read_data():
    """Read the encrypted IP from the MQTT broker

    :returns: returns the encrypted IP
    :rtype: bytes

    """
    settings = configparser.ConfigParser({'password': None})
    settings.read('server_configuration.ini')

    mqtt_host = settings.get('platform-configuration', 'host')
    mqtt_username = settings.get('platform-configuration', 'username')
    mqtt_password = settings.get('platform-configuration', 'password')
    mqtt_channel = settings.get('platform-configuration', 'channel')

    auth = {'username': mqtt_username, 'password': mqtt_password}
    data = subscribe.simple(mqtt_channel, hostname=mqtt_host, auth=auth)

    return data.payload
