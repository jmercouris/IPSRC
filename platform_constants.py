import platform_disk


def get_broadcast_function(platform_string):
    if(platform_string == "disk"):
        return platform_disk.broadcast_data


def get_read_function(platform_string):
    if(platform_string == "disk"):
        return platform_disk.read_data
