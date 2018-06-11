import platform_disk
import platform_git
import platform_mqtt


def get_broadcast_function(platform_string):
    if(platform_string == "disk"):
        return platform_disk.broadcast_data
    if(platform_string == "git"):
        return platform_git.broadcast_data
    if(platform_string == "mqtt"):
        return platform_mqtt.broadcast_data


def get_read_function(platform_string):
    if(platform_string == "disk"):
        return platform_disk.read_data
    if(platform_string == "git"):
        return platform_git.read_data
    if(platform_string == "mqtt"):
        return platform_mqtt.read_data
