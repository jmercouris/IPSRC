IPSRC
========================================================================
IPSRC is a program that allows you to keep track of your home
computer's IP. It allows your server to automatically get its IP,
encrypt it, and broadcast it on a platform of your choice. The currently
supported platforms are GIT and Disk.

Requirements
------------------------------------------------------------------------
+ Python 3.4+
+ Git
+ Public/Private Key Pairs

Usage
------------------------------------------------------------------------
To use IPSRC, clone it to both your server and your client machine. To
configure the server, you might do something like the following (for
an example, please see server_configuration.ini):

.. code-block:: ini

   [public-key]
   path = /path/to/public/key/id_rsa.pub
   [platform-configuration]
   type = git
   repository-path = /path/to/repository

In the above configuration, we have set the platform to be Git. This
means that the server will obtain its IP address, encrypt it, and push
it to a Git repository. The public key must be the client's public
key.

Your client configuration will look something like the following (for
an example, please see client_configuration.ini):

.. code-block:: ini

   [private-key]
   path = /path/to/private/key/id_rsa
   [platform-configuration]
   type = git
   repository-path = /path/to/repository

In the above configuration, we have again set the platform to be Git,
and we have created a repository located at "path/to/repository". It
is important that the platform information on the server/client match
so that the server may broadcast to a location that the client will
look in. In this case, this is where the client will pull from, and
decrypt the IP of the server.

In the above example, you will have to configure the repository
to have a remote origin that it may push/pull to, otherwise the data
will have nowhere to go (to be hosted).

Installing Dependencies
------------------------------------------------------------------------
The python dependencies are listed in requirements.txt. You can install them
with pip via:

    python3 -m pip install -r requirements.txt

Additionally, if this breaks other dependencies on your system, consider
creating a venv:

    # Create a python virtual environment.
    python3 -m venv path/to/IPSRC/venv

    # Enter the virtual environment.
    source path/to/IPSRC/venv/bin/activate

    # Install the requirements in this virtual environment.
    python3 -m pip install -r requirements.txt

    # Execute IPSRC code (python3 server_broadcast.py or client_source.py) with
    the dependencies installed in the venv.
    
    # To exit the venv, run "deactivate"
    deactivate

Usage: On the Server
------------------------------------------------------------------------
You'll want to install all the dependencies located in the
requirements file. You'll then wish to set up a cron job to run
:code:`python server_broadcast.py` at some interval of your choice.

Usage: On the Client
------------------------------------------------------------------------
You'll want to install all the dependencies located in the
requirements file. You'll then want to run :code:`python client_source.py`
whenever you wish to update your server's address on the client.

How it works:
------------------------------------------------------------------------
The server will periodically encrypt its IP and broadcast it to some
source. The place it will be broadcast depends upon the
:code:`[platform-configuration]`. In the above example, we are broadcasting
to a Git repository. 

The server will use the client's public key to encrypt its IP
address. This is so that nobody else may peek inside and see what your
server's IP address is.

The client, when ready, will read from wherever the server is
broadcasting to. In the above example, the client will pull (read)
from a Git repository. The client will then use its private key to
read the encrypted IP.

Extending IPSRC
------------------------------------------------------------------------
To extend IPSRC and add your own platforms, you have to do a few
things. Firstly you must edit :code:`platform_constants.py` to include
your new platform. After, you must create a new platform file, ideally
with the naming convention :code:`platform_new_name`. Within your new
platform, you must implement two functions :code:`broadcast_data` and
:code:`read_data`.

You can include your own directives within the INI file that the user
must include for your new broadcast and read functionality. To see
an example of this, please look at :code:`platform_git.py`.

You should be able to extend IPSRC to use almost any kind of broadcast
or existing service, you might use email, ftp servers, ssh, etc. Any
pull requests for new platforms are always welcome, thanks!
